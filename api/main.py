from __future__ import annotations

import hashlib
import hmac
import os
import re
import secrets
import sqlite3
import time
import json
from datetime import date, datetime, timedelta, timezone
from contextlib import contextmanager
from pathlib import Path

from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from .content import LANGUAGES, LESSONS, RHYMES, STORIES, POEMS, PERFORMANCES
from . import narration
from . import journey
from .achievements import achievements
from .game_levels import BASE, game_bank, public_games, game_progress

ROOT = Path(__file__).resolve().parents[1]
GAMES = BASE
DB = Path(os.environ.get("BRIGHTLY_DB_PATH", ROOT / "brightly.sqlite3"))
app = FastAPI(title="Brightly")


@app.middleware('http')
async def revalidate_frontend(request: Request, call_next):
    response=await call_next(request)
    if request.url.path.startswith('/assets/'):
        response.headers['Cache-Control']='no-cache'
    elif response.headers.get('content-type','').startswith('text/html'):
        response.headers['Cache-Control']='no-store'
    return response


@contextmanager
def database():
    DB.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(DB, timeout=10)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys=ON")
    try:
        yield con
        con.commit()
    finally:
        con.close()


with database() as con:
    con.executescript("""
    CREATE TABLE IF NOT EXISTS parents(id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT NOT NULL UNIQUE, salt TEXT NOT NULL, password_hash TEXT NOT NULL);
    CREATE TABLE IF NOT EXISTS sessions(token_hash TEXT PRIMARY KEY, parent_id INTEGER NOT NULL REFERENCES parents(id) ON DELETE CASCADE, csrf TEXT NOT NULL, expires INTEGER NOT NULL);
    CREATE TABLE IF NOT EXISTS children(id INTEGER PRIMARY KEY, parent_id INTEGER NOT NULL REFERENCES parents(id) ON DELETE CASCADE, name TEXT NOT NULL, age INTEGER NOT NULL, language TEXT NOT NULL, avatar TEXT NOT NULL);
    CREATE TABLE IF NOT EXISTS completions(child_id INTEGER NOT NULL REFERENCES children(id) ON DELETE CASCADE, lesson_id TEXT NOT NULL, score INTEGER NOT NULL, completed_at INTEGER NOT NULL, PRIMARY KEY(child_id,lesson_id));
    CREATE TABLE IF NOT EXISTS game_results(child_id INTEGER NOT NULL REFERENCES children(id) ON DELETE CASCADE, game_id TEXT NOT NULL, score INTEGER NOT NULL, played_at INTEGER NOT NULL);
    CREATE TABLE IF NOT EXISTS login_attempts(email TEXT PRIMARY KEY, attempts INTEGER NOT NULL, first_at INTEGER NOT NULL);
    CREATE TABLE IF NOT EXISTS daily_habits(child_id INTEGER NOT NULL REFERENCES children(id) ON DELETE CASCADE, day TEXT NOT NULL, habit TEXT NOT NULL, PRIMARY KEY(child_id,day,habit));
    CREATE TABLE IF NOT EXISTS reading_progress(child_id INTEGER NOT NULL REFERENCES children(id) ON DELETE CASCADE, kind TEXT NOT NULL, item_id TEXT NOT NULL, language TEXT NOT NULL, completed_at INTEGER NOT NULL, PRIMARY KEY(child_id,kind,item_id,language));
    CREATE TABLE IF NOT EXISTS narration_usage(parent_id INTEGER NOT NULL REFERENCES parents(id) ON DELETE CASCADE, day TEXT NOT NULL, requests INTEGER NOT NULL, PRIMARY KEY(parent_id,day));
    """)
    if "recovery_hash" not in {row[1] for row in con.execute("PRAGMA table_info(parents)")}:
        con.execute("ALTER TABLE parents ADD COLUMN recovery_hash TEXT")
    if "attempt_id" not in {row[1] for row in con.execute("PRAGMA table_info(game_results)")}:
        con.execute("ALTER TABLE game_results ADD COLUMN attempt_id TEXT")
    if "game_level" not in {row[1] for row in con.execute("PRAGMA table_info(game_results)")}:
        con.execute("ALTER TABLE game_results ADD COLUMN game_level INTEGER NOT NULL DEFAULT 1")
    con.execute("CREATE UNIQUE INDEX IF NOT EXISTS game_attempt_unique ON game_results(child_id,attempt_id)")
    journey.schema(con)


def fail(message: str, status: int = 400):
    raise HTTPException(status, message)


def hash_password(password: str, salt: str) -> str:
    return hashlib.pbkdf2_hmac("sha256", password.encode(), bytes.fromhex(salt), 310_000).hex()


def session_for(request: Request, mutation=False):
    token = request.cookies.get("brightly_session", "")
    if not token:
        fail("Please sign in to continue.", 401)
    digest = hashlib.sha256(token.encode()).hexdigest()
    with database() as con:
        row = con.execute("SELECT s.*,p.name,p.email FROM sessions s JOIN parents p ON p.id=s.parent_id WHERE s.token_hash=? AND s.expires>?", (digest, int(time.time()))).fetchone()
    if not row:
        fail("Your session has expired. Please sign in again.", 401)
    if mutation and not hmac.compare_digest(request.headers.get("x-csrf-token", ""), row["csrf"]):
        fail("Security check failed. Refresh the page and try again.", 403)
    return row


def child_for(parent_id: int, child_id: int):
    with database() as con:
        child = con.execute("SELECT * FROM children WHERE id=? AND parent_id=?", (child_id, parent_id)).fetchone()
    if not child:
        fail("Child profile not found.", 404)
    return child


def current_level(completed: set[str]) -> int:
    return min(5, 1 + len(completed) // 2)


def child_summary(child, zone='UTC'):
    with database() as con:
        con.execute('BEGIN IMMEDIATE')
        done = con.execute("SELECT lesson_id,score,completed_at FROM completions WHERE child_id=? ORDER BY completed_at DESC", (child["id"],)).fetchall()
        games = con.execute("SELECT game_id,score,played_at,game_level FROM game_results WHERE child_id=? ORDER BY played_at DESC,rowid DESC", (child["id"],)).fetchall()
        readings = con.execute("SELECT kind,item_id,language,completed_at FROM reading_progress WHERE child_id=? ORDER BY completed_at DESC",(child["id"],)).fetchall()
        completed = {r["lesson_id"] for r in done}
        stars = len(done) * 3 + sum(r["score"] for r in games)
        progress=game_progress(games)
        badges=achievements(completed,games,readings)
        daily=journey.snapshot(con,child['id'],badges,max(item['unlocked'] for item in progress.values()),zone)
        badges=[*badges,*daily.pop('badges')]
    return {"id":child["id"],"name":child["name"],"age":child["age"],"language":child["language"],"avatar":child["avatar"],"level":current_level(completed),"stars":stars,"completed":list(completed),"completions":[dict(r) for r in done],"games":[dict(r) for r in games],"readings":[dict(row) for row in readings],"badges":badges,"game_progress":progress,"journey":daily}


def create_session(parent_id: int, response: Response):
    token = secrets.token_urlsafe(32)
    csrf = secrets.token_urlsafe(24)
    with database() as con:
        con.execute("DELETE FROM sessions WHERE expires<?", (int(time.time()),))
        con.execute("INSERT INTO sessions VALUES(?,?,?,?)", (hashlib.sha256(token.encode()).hexdigest(), parent_id, csrf, int(time.time()) + 60*60*24*7))
    response.set_cookie("brightly_session", token, httponly=True, secure=os.environ.get("BRIGHTLY_HTTPS") == "1", samesite="lax", max_age=60*60*24*7)
    return csrf


class Signup(BaseModel):
    name: str = Field(min_length=2, max_length=80)
    email: str = Field(min_length=5, max_length=254)
    password: str = Field(min_length=8, max_length=128)


class Login(BaseModel):
    email: str
    password: str


class ResetPassword(BaseModel):
    email: str
    recovery_code: str
    new_password: str = Field(min_length=8, max_length=128)


class ChildInput(BaseModel):
    name: str = Field(min_length=1, max_length=40)
    age: int = Field(ge=3, le=7)
    language: str
    avatar: str = "sun"


class ChildLanguage(BaseModel):
    language: str = Field(pattern='^(en|hi|mr)$')


class Answers(BaseModel):
    answers: list[int] = Field(min_length=1, max_length=1)


class GameCheck(BaseModel):
    game_level: int = Field(default=1, ge=1, le=3)
    game_id: str
    question: int = Field(ge=0, le=2)
    answer: int | list[int]
    language: str = 'en'


class HabitCheck(BaseModel):
    habit: str
    checked: bool
    day: date


class GameScore(BaseModel):
    game_level: int = Field(default=1, ge=1, le=3)
    game_id: str
    attempt_id: str | None = Field(default=None, min_length=8, max_length=100)
    answers: list[int | list[int]] = Field(default_factory=list, max_length=3)
    board: list[str] = Field(default_factory=list, max_length=12)
    moves: list[int] = Field(default_factory=list, max_length=12)


@app.post("/api/signup")
def signup(body: Signup, response: Response):
    email = body.email.strip().lower()
    if not re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", email):
        fail("Enter a valid email address.")
    salt = secrets.token_hex(16)
    recovery_code = secrets.token_urlsafe(24)
    try:
        with database() as con:
            cursor = con.execute("INSERT INTO parents(name,email,salt,password_hash,recovery_hash) VALUES(?,?,?,?,?)", (body.name.strip(), email, salt, hash_password(body.password, salt), hashlib.sha256(recovery_code.encode()).hexdigest()))
            parent_id = cursor.lastrowid
    except sqlite3.IntegrityError:
        fail("An account with this email already exists.", 409)
    csrf = create_session(parent_id, response)
    return {"parent":{"id":parent_id,"name":body.name.strip(),"email":email},"csrf":csrf,"recovery_code":recovery_code}


@app.post("/api/login")
def login(body: Login, response: Response):
    email = body.email.strip().lower()
    now = int(time.time())
    with database() as con:
        attempt = con.execute("SELECT attempts,first_at FROM login_attempts WHERE email=?", (email,)).fetchone()
        if attempt and attempt["attempts"] >= 5 and now - attempt["first_at"] < 900:
            fail("Too many attempts. Please wait 15 minutes and try again.", 429)
        parent = con.execute("SELECT * FROM parents WHERE email=?", (email,)).fetchone()
    if not parent or not hmac.compare_digest(hash_password(body.password, parent["salt"]), parent["password_hash"]):
        with database() as con:
            if attempt and now - attempt["first_at"] < 900:
                con.execute("UPDATE login_attempts SET attempts=attempts+1 WHERE email=?", (email,))
            else:
                con.execute("INSERT INTO login_attempts VALUES(?,?,?) ON CONFLICT(email) DO UPDATE SET attempts=excluded.attempts,first_at=excluded.first_at", (email, 1, now))
        fail("Email or password is incorrect.", 401)
    with database() as con:
        con.execute("DELETE FROM login_attempts WHERE email=?", (email,))
    csrf = create_session(parent["id"], response)
    return {"parent":{"id":parent["id"],"name":parent["name"],"email":parent["email"]},"csrf":csrf}


@app.post("/api/reset-password")
def reset_password(body: ResetPassword):
    email = body.email.strip().lower()
    with database() as con:
        parent = con.execute("SELECT * FROM parents WHERE email=?", (email,)).fetchone()
        digest = hashlib.sha256(body.recovery_code.strip().encode()).hexdigest()
        if not parent or not parent["recovery_hash"] or not hmac.compare_digest(digest, parent["recovery_hash"]):
            fail("Email or recovery code is incorrect.", 400)
        salt = secrets.token_hex(16)
        new_code = secrets.token_urlsafe(24)
        con.execute("UPDATE parents SET salt=?,password_hash=?,recovery_hash=? WHERE id=?", (salt, hash_password(body.new_password,salt), hashlib.sha256(new_code.encode()).hexdigest(), parent["id"]))
        con.execute("DELETE FROM sessions WHERE parent_id=?", (parent["id"],))
        con.execute("DELETE FROM login_attempts WHERE email=?", (email,))
    return {"recovery_code":new_code}


@app.get("/api/session")
def session(request: Request):
    row = session_for(request)
    return {"parent":{"id":row["parent_id"],"name":row["name"],"email":row["email"]},"csrf":row["csrf"]}


@app.post("/api/logout")
def logout(request: Request, response: Response):
    row = session_for(request, True)
    with database() as con:
        con.execute("DELETE FROM sessions WHERE token_hash=?", (row["token_hash"],))
    response.delete_cookie("brightly_session")
    return {"ok":True}


@app.get("/api/children")
def children(request: Request):
    parent = session_for(request)
    with database() as con:
        rows = con.execute("SELECT * FROM children WHERE parent_id=? ORDER BY id", (parent["parent_id"],)).fetchall()
    return [child_summary(row,request.headers.get('x-time-zone','UTC')) for row in rows]


@app.post("/api/children")
def add_child(body: ChildInput, request: Request):
    parent = session_for(request, True)
    if body.language not in LANGUAGES:
        fail("Choose English, Hindi, or Marathi.")
    with database() as con:
        count = con.execute("SELECT COUNT(*) FROM children WHERE parent_id=?", (parent["parent_id"],)).fetchone()[0]
        if count >= 8:
            fail("An account can have up to eight child profiles.")
        cursor = con.execute("INSERT INTO children(parent_id,name,age,language,avatar) VALUES(?,?,?,?,?)", (parent["parent_id"], body.name.strip(), body.age, body.language, body.avatar[:24]))
        child = con.execute("SELECT * FROM children WHERE id=?", (cursor.lastrowid,)).fetchone()
    return child_summary(child,request.headers.get('x-time-zone','UTC'))


@app.put("/api/children/{child_id}")
def update_child(child_id: int, body: ChildInput, request: Request):
    parent = session_for(request, True)
    child_for(parent["parent_id"], child_id)
    if body.language not in LANGUAGES:
        fail("Choose English, Hindi, or Marathi.")
    with database() as con:
        con.execute("UPDATE children SET name=?,age=?,language=?,avatar=? WHERE id=?", (body.name.strip(), body.age, body.language, body.avatar[:24], child_id))
        child = con.execute("SELECT * FROM children WHERE id=?", (child_id,)).fetchone()
    return child_summary(child)


@app.put('/api/children/{child_id}/language')
def update_child_language(child_id: int, body: ChildLanguage, request: Request):
    parent=session_for(request,True)
    child_for(parent['parent_id'],child_id)
    with database() as con:
        con.execute('UPDATE children SET language=? WHERE id=?',(body.language,child_id))
    return {'language':body.language}


@app.delete("/api/children/{child_id}")
def delete_child(child_id: int, request: Request):
    parent = session_for(request, True)
    child_for(parent["parent_id"], child_id)
    with database() as con:
        con.execute("DELETE FROM children WHERE id=?", (child_id,))
    return {"ok":True}


class ShieldPurchase(BaseModel):
    request_id: str = Field(min_length=8,max_length=100,pattern='^[a-zA-Z0-9_-]+$')


@app.get('/api/children/{child_id}/journey')
def learning_journey(child_id: int,request: Request):
    parent=session_for(request)
    child=child_for(parent['parent_id'],child_id)
    return child_summary(child,request.headers.get('x-time-zone','UTC'))


@app.post('/api/children/{child_id}/shields')
def buy_streak_shield(child_id: int,body: ShieldPurchase,request: Request):
    parent=session_for(request,True)
    child=child_for(parent['parent_id'],child_id)
    try:
        with database() as con:
            con.execute('BEGIN IMMEDIATE')
            journey.buy_shield(con,child_id,body.request_id,request.headers.get('x-time-zone','UTC'))
    except journey.JourneyError as error:
        fail(str(error))
    return child_summary(child)


@app.get("/api/content")
def content(request: Request):
    session_for(request)
    return {"lessons":[{k:v for k,v in lesson.items() if k!="answer"} for lesson in LESSONS],"stories":STORIES,"rhymes":RHYMES,"poems":POEMS,"performances":PERFORMANCES,"games":public_games(),"narration":{"ai_available":narration.available(),"provider":'edge' if narration.bundled_enabled() else narration.provider(),"singing_available":False}}


class ReadingComplete(BaseModel):
    kind: str
    item_id: str = Field(max_length=80)
    language: str


@app.post('/api/children/{child_id}/readings')
def finish_reading(child_id: int, body: ReadingComplete, request: Request):
    parent=session_for(request,True)
    child=child_for(parent['parent_id'],child_id)
    collections={'stories':STORIES,'rhymes':RHYMES,'poems':POEMS,'performances':PERFORMANCES}
    item=next((item for item in collections.get(body.kind,[]) if item['id']==body.item_id),None)
    if not item or body.language not in item.get('available_languages',['en','hi','mr']):
        fail('Reading or language not found.',404)
    with database() as con:
        con.execute('BEGIN IMMEDIATE')
        con.execute('INSERT INTO reading_progress VALUES(?,?,?,?,?) ON CONFLICT(child_id,kind,item_id,language) DO NOTHING',
            (child_id,body.kind,body.item_id,body.language,int(time.time())))
        journey.record(con,child_id,'reading',f'{body.kind}:{body.item_id}:{body.language}',zone=request.headers.get('x-time-zone','UTC'))
    return child_summary(child)


class NarrationRequest(BaseModel):
    kind: str = Field(max_length=12)
    item_id: str = Field(max_length=60)
    language: str = Field(max_length=5)
    mode: str = 'spoken'
    part: str = Field(default='text', max_length=20)
    question: int = Field(default=0, ge=0, le=2)
    option: int | None = Field(default=None, ge=0, le=9)
    level: int = Field(default=1, ge=1, le=3)


@app.post('/api/narration')
def narrate(body: NarrationRequest, request: Request):
    parent = session_for(request, True)
    if body.mode not in ('spoken','sung') or (body.mode=='sung' and body.kind!='rhymes'):
        fail('Choose a supported playback style.')
    try:
        text = narration.published_text(body.kind, body.item_id, body.language, body.part, body.question, body.option, body.level)
    except ValueError as error:
        fail(str(error), 404)

    def reserve_generation():
        today = date.today().isoformat()
        with database() as con:
            con.execute('BEGIN IMMEDIATE')
            con.execute('DELETE FROM narration_usage WHERE day<>?', (today,))
            own = con.execute('SELECT requests FROM narration_usage WHERE parent_id=? AND day=?', (parent['parent_id'], today)).fetchone()
            total = con.execute('SELECT COALESCE(SUM(requests),0) FROM narration_usage WHERE day=?', (today,)).fetchone()[0]
            if (own and own['requests'] >= 20) or total >= 60:
                fail('AI narration has reached today’s limit. Use the device voice for now.', 429)
            con.execute('INSERT INTO narration_usage VALUES(?,?,1) ON CONFLICT(parent_id,day) DO UPDATE SET requests=requests+1', (parent['parent_id'], today))

    try:
        audio = narration.render_audio(text, body.language, DB.parent / '.brightly-audio', reserve_generation, mode=body.mode)
    except (narration.VoiceUnavailable, OSError) as error:
        fail('AI narration is unavailable. You can use the device voice instead.', 503)
    return Response(audio, media_type='audio/mpeg', headers={'Cache-Control': 'private, no-store'})


def valid_game_answer(game_id, answer, level=1):
    if game_bank(game_id, level).get('type') == 'sequence':
        return isinstance(answer, list) and len(answer) == 3 and all(type(i) is int for i in answer) and sorted(answer) == [0, 1, 2]
    return type(answer) is int and answer in (0, 1, 2)


@app.post("/api/children/{child_id}/lessons/{lesson_id}/complete")
def complete(child_id: int, lesson_id: str, body: Answers, request: Request):
    parent = session_for(request, True)
    child = child_for(parent["parent_id"], child_id)
    lesson = next((x for x in LESSONS if x["id"] == lesson_id), None)
    if not lesson:
        fail("Lesson not found.", 404)
    summary = child_summary(child)
    if lesson["level"] > summary["level"]:
        fail("Finish more lessons to unlock this one.", 403)
    correct = body.answers[0] == lesson["answer"]
    if correct:
        with database() as con:
            con.execute('BEGIN IMMEDIATE')
            con.execute("INSERT INTO completions VALUES(?,?,?,?) ON CONFLICT(child_id,lesson_id) DO NOTHING", (child_id, lesson_id, 1, int(time.time())))
            journey.record(con,child_id,'lesson',lesson_id,zone=request.headers.get('x-time-zone','UTC'))
    return {"correct":correct,"correct_answer":lesson["answer"],"child":child_summary(child)}


def ensure_game_level(child, game_id, level):
    unlocked = child_summary(child)['game_progress'][game_id]['unlocked']
    if level > unlocked:
        fail('Earn two stars at the previous difficulty to unlock this level.',403)


@app.post("/api/children/{child_id}/games/check")
def check_game(child_id: int, body: GameCheck, request: Request):
    parent = session_for(request, True)
    child = child_for(parent["parent_id"], child_id)
    if body.game_id not in GAMES or body.language not in LANGUAGES:
        fail("Unknown game or language.")
    ensure_game_level(child, body.game_id, body.game_level)
    game = game_bank(body.game_id, body.game_level)
    if not valid_game_answer(body.game_id, body.answer, body.game_level):
        fail('Choose a valid answer for this game.')
    correct = game["answers"][body.question]
    return {"correct":body.answer == correct,"correct_answer":correct,"explanation":game["explanations"][body.language][body.question],"explanations":{language:games[body.question] for language,games in game["explanations"].items()}}


@app.post("/api/children/{child_id}/games")
def save_game(child_id: int, body: GameScore, request: Request):
    parent = session_for(request, True)
    child = child_for(parent["parent_id"], child_id)
    if body.game_id != 'memory' and body.game_id not in GAMES:
        fail("Unknown game.")
    ensure_game_level(child, body.game_id, body.game_level)
    if body.game_id == "memory":
        symbols = ["☀","✿","♡","★","☂","♬"][:{1:3,2:4,3:6}[body.game_level]]
        valid_board = sorted(body.board) == sorted(symbols * 2)
        valid_moves = sorted(body.moves) == list(range(len(symbols) * 2))
        matched = valid_board and valid_moves and all(body.board[body.moves[i]] == body.board[body.moves[i+1]] for i in range(0,len(body.moves),2))
        if not matched:
            fail("Match all the pairs before saving this game.")
        score = 3
    else:
        key = game_bank(body.game_id,body.game_level)["answers"]
        if len(body.answers) != 3 or any(not valid_game_answer(body.game_id,answer,body.game_level) for answer in body.answers):
            fail("Answer all three questions to finish the game.")
        score = sum(answer == correct for answer,correct in zip(body.answers,key))
    with database() as con:
        con.execute("BEGIN IMMEDIATE")
        existing = con.execute("SELECT game_id,score,game_level FROM game_results WHERE child_id=? AND attempt_id=?",(child_id,body.attempt_id)).fetchone() if body.attempt_id else None
        if existing and (existing['game_id'] != body.game_id or existing['score'] != score or existing['game_level'] != body.game_level):
            fail("This game attempt was already saved with different answers.",409)
        con.execute("INSERT OR IGNORE INTO game_results(child_id,game_id,score,played_at,attempt_id,game_level) VALUES(?,?,?,?,?,?)", (child_id, body.game_id, score, int(time.time()),body.attempt_id,body.game_level))
        journey.record(con,child_id,'game',f'{body.game_id}:{body.game_level}',dict(score=score,level=body.game_level),zone=request.headers.get('x-time-zone','UTC'))
    return {**child_summary(child),"game_result":{"score":score,"total":3,"level":body.game_level}}


def habit_summary(child_id, today):
    with database() as con:
        rows=con.execute('SELECT day,habit FROM daily_habits WHERE child_id=? ORDER BY day DESC',(child_id,)).fetchall()
    days={row['day'] for row in rows}
    cursor=today if today.isoformat() in days else today-timedelta(days=1)
    streak=0
    while cursor.isoformat() in days:
        streak+=1
        cursor-=timedelta(days=1)
    return {'day':today.isoformat(),'checked':[r['habit'] for r in rows if r['day']==today.isoformat()],'streak':streak,'days_practiced':len(days)}


@app.get('/api/children/{child_id}/habits')
def get_habits(child_id: int, request: Request, day: date):
    parent=session_for(request)
    child_for(parent['parent_id'],child_id)
    return habit_summary(child_id,day)


@app.post('/api/children/{child_id}/habits')
def set_habit(child_id: int, body: HabitCheck, request: Request):
    parent=session_for(request,True)
    child_for(parent['parent_id'],child_id)
    if body.habit not in ('hands','tidy','kind','teeth'):
        fail('Unknown habit.')
    if abs((body.day-datetime.now(timezone.utc).date()).days)>1:
        fail('Check in for today using your local date.')
    with database() as con:
        if body.checked:
            con.execute('INSERT OR IGNORE INTO daily_habits VALUES(?,?,?)',(child_id,body.day.isoformat(),body.habit))
        else:
            con.execute('DELETE FROM daily_habits WHERE child_id=? AND day=? AND habit=?',(child_id,body.day.isoformat(),body.habit))
    return habit_summary(child_id,body.day)


DIST = ROOT / "web" / "dist"
if DIST.exists():
    app.mount("/assets", StaticFiles(directory=DIST / "assets"), name="assets")


@app.get("/{path:path}")
def frontend(path: str):
    if not DIST.exists():
        fail("Frontend not built. Run npm ci and npm run build inside web/.", 503)
    file = DIST / path
    if path and file.is_file() and file.resolve().is_relative_to(DIST.resolve()):
        return FileResponse(file)
    return FileResponse(DIST / "index.html")
