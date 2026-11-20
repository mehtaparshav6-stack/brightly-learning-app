"""Server-owned daily learning, Sunseeds, shields, and missions."""
import json
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

SHIELD_PRICE = 40
SHIELD_CAP = 3
BADGE_REWARD = 15


class JourneyError(ValueError):
    pass


def schema(con):
    con.executescript('''
    CREATE TABLE IF NOT EXISTS journey_wallets(child_id INTEGER PRIMARY KEY REFERENCES children(id) ON DELETE CASCADE, balance INTEGER NOT NULL CHECK(balance>=0), shields INTEGER NOT NULL CHECK(shields>=0 AND shields<=3), best_streak INTEGER NOT NULL DEFAULT 0, timezone TEXT NOT NULL, checked_through TEXT NOT NULL);
    CREATE TABLE IF NOT EXISTS journey_days(child_id INTEGER NOT NULL REFERENCES children(id) ON DELETE CASCADE, day TEXT NOT NULL, status TEXT NOT NULL DEFAULT 'open', lesson_target INTEGER NOT NULL, challenge_level INTEGER NOT NULL, PRIMARY KEY(child_id,day));
    CREATE TABLE IF NOT EXISTS journey_events(child_id INTEGER NOT NULL REFERENCES children(id) ON DELETE CASCADE, day TEXT NOT NULL, kind TEXT NOT NULL, event_key TEXT NOT NULL, detail TEXT NOT NULL, PRIMARY KEY(child_id,day,kind,event_key));
    CREATE TABLE IF NOT EXISTS journey_ledger(child_id INTEGER NOT NULL REFERENCES children(id) ON DELETE CASCADE, entry_key TEXT NOT NULL, amount INTEGER NOT NULL, reason TEXT NOT NULL, day TEXT NOT NULL, PRIMARY KEY(child_id,entry_key));
    ''')


def valid_zone(name):
    try:
        ZoneInfo(name)
        return name
    except (ZoneInfoNotFoundError, ValueError, TypeError):
        return 'UTC'


def local_day(zone, now=None):
    return (now or datetime.now(timezone.utc)).astimezone(ZoneInfo(zone)).date()


def credit(con, child, key, amount, reason, day):
    cursor = con.execute('INSERT OR IGNORE INTO journey_ledger VALUES(?,?,?,?,?)', (child, key, amount, reason, str(day)))
    if cursor.rowcount:
        con.execute('UPDATE journey_wallets SET balance=balance+? WHERE child_id=?', (amount, child))
    return bool(cursor.rowcount)


def ensure(con, child, zone='UTC', now=None):
    zone = valid_zone(zone)
    today = local_day(zone, now)
    cursor = con.execute('INSERT OR IGNORE INTO journey_wallets(child_id,balance,shields,timezone,checked_through) VALUES(?,0,1,?,?)', (child, zone, str(today-timedelta(days=1))))
    if cursor.rowcount:
        credit(con, child, 'welcome', 20, 'welcome', today)
    wallet = con.execute('SELECT * FROM journey_wallets WHERE child_id=?', (child,)).fetchone()
    today = local_day(wallet['timezone'], now)
    reconcile(con, child, today, wallet)
    return today


def day_config(con, child, day, challenge=1):
    target = (2, 3, 5)[day.toordinal() % 3]
    con.execute('INSERT OR IGNORE INTO journey_days VALUES(?,?,?,?,?)', (child, str(day), 'open', target, max(1,min(3,challenge))))
    return con.execute('SELECT * FROM journey_days WHERE child_id=? AND day=?', (child, str(day))).fetchone()


def reconcile(con, child, today, wallet):
    checked = datetime.strptime(wallet['checked_through'], '%Y-%m-%d').date()
    yesterday = today-timedelta(days=1)
    if checked >= yesterday:
        return
    statuses = {row['day']:row['status'] for row in con.execute("SELECT day,status FROM journey_days WHERE child_id=? AND status IN ('learned','protected')", (child,))}
    shields = wallet['shields']
    cursor = checked+timedelta(days=1)
    # Only an already-running streak can use shields. Buying later never repairs an old gap.
    while cursor <= yesterday:
        key = str(cursor)
        if statuses.get(key) not in ('learned','protected'):
            if statuses.get(str(cursor-timedelta(days=1))) not in ('learned','protected') or not shields:
                break
            day_config(con, child, cursor)
            con.execute("UPDATE journey_days SET status='protected' WHERE child_id=? AND day=?", (child, key))
            statuses[key] = 'protected'
            shields -= 1
        cursor += timedelta(days=1)
    con.execute('UPDATE journey_wallets SET shields=?,checked_through=? WHERE child_id=?', (shields,str(yesterday),child))


def record(con, child, kind, event_key, detail=None, zone='UTC', now=None):
    today = ensure(con, child, zone, now)
    config=day_config(con, child, today)
    detail = detail or {}
    old = con.execute('SELECT detail FROM journey_events WHERE child_id=? AND day=? AND kind=? AND event_key=?', (child,str(today),kind,event_key)).fetchone()
    if old:
        if kind == 'game':
            previous = json.loads(old['detail'])
            if detail.get('score',0) > previous.get('score',0):
                con.execute('UPDATE journey_events SET detail=? WHERE child_id=? AND day=? AND kind=? AND event_key=?', (json.dumps(detail),child,str(today),kind,event_key))
        missions(con,child,today,config)
        return
    con.execute('INSERT INTO journey_events VALUES(?,?,?,?,?)', (child,str(today),kind,event_key,json.dumps(detail)))
    if kind in ('lesson','game'):
        con.execute("UPDATE journey_days SET status='learned' WHERE child_id=? AND day=?", (child,str(today)))
        streak(con,child,today)
    cap = {'lesson':5,'game':5,'reading':3}[kind]
    count = con.execute('SELECT COUNT(*) FROM journey_ledger WHERE child_id=? AND day=? AND reason=?', (child,str(today),kind)).fetchone()[0]
    if count < cap:
        amount = 12 if kind=='lesson' else 3 if kind=='reading' else 6+2*detail.get('score',0)+3*(detail.get('level',1)-1)
        credit(con, child, f'{kind}/{today}/{event_key}', amount, kind, today)
    missions(con,child,today,config)


def streak(con, child, today):
    days = {row['day']:row['status'] for row in con.execute("SELECT day,status FROM journey_days WHERE child_id=? AND status IN ('learned','protected')", (child,))}
    cursor = today if str(today) in days else today-timedelta(days=1)
    count = 0
    while str(cursor) in days:
        count += days[str(cursor)] == 'learned'
        cursor -= timedelta(days=1)
    con.execute('UPDATE journey_wallets SET best_streak=MAX(best_streak,?) WHERE child_id=?', (count,child))
    return count,days


def missions(con, child, today, config):
    events = [dict(row) for row in con.execute('SELECT kind,event_key,detail FROM journey_events WHERE child_id=? AND day=?', (child,str(today)))]
    lesson_count = sum(row['kind']=='lesson' for row in events)
    games = [json.loads(row['detail']) for row in events if row['kind']=='game']
    readings = sum(row['kind']=='reading' for row in events)
    rows = [
        ('little-steps','📚',config['lesson_target'],lesson_count,20,
         {'en':f"Complete {config['lesson_target']} different lessons",'hi':f"{config['lesson_target']} अलग पाठ पूरे करें",'mr':f"{config['lesson_target']} वेगळे धडे पूर्ण करा"}),
        ('playful-mind','🧩',1,len(games),10,{'en':'Finish one mini game','hi':'एक छोटा खेल पूरा करें','mr':'एक छोटा खेळ पूर्ण करा'}),
        ('story-time','📖',1,readings,6,{'en':'Finish a story, poem, or song together','hi':'साथ में एक कहानी, कविता या गीत पूरा करें','mr':'सोबत एक गोष्ट, कविता किंवा गीत पूर्ण करा'}),
        ('brave-practice','🪁',1,sum(game.get('level',1)>=config['challenge_level'] and game.get('score',0)>=2 for game in games),18,
         {'en':f"Earn two stars in a difficulty {config['challenge_level']} game",'hi':f"कठिनाई {config['challenge_level']} के खेल में दो सितारे पाएँ",'mr':f"पातळी {config['challenge_level']} च्या खेळात दोन तारे मिळवा"}),
    ]
    result=[]
    for key,icon,target,current,reward,title in rows:
        done=current>=target
        if done:
            credit(con,child,f'mission/{today}/{key}',reward,'mission',today)
        result.append(dict(id=key,icon=icon,target=target,current=min(current,target),reward=reward,title=title,completed=done))
    return result,events


def badges(best, protected, mission_count):
    rows=[]
    for target in (3,7,14,30):
        rows.append((f'streak-{target}','☀',target,best,
                     dict(en=f'{target}-day sunshine',hi=f'{target} दिन की धूप',mr=f'{target} दिवसांचे ऊन'),
                     dict(en=f'Learn on {target} days in one protected streak.',hi=f'एक सुरक्षित क्रम में {target} दिन सीखें।',mr=f'एका सुरक्षित मालिकेत {target} दिवस शिका.')))
    rows.extend([
        ('shield-friend','🛡',1,protected,dict(en='A little protection',hi='छोटी सी सुरक्षा',mr='थोडे संरक्षण'),dict(en='Protect a missed day with a shield.',hi='शील्ड से छूटा हुआ एक दिन बचाएँ।',mr='शील्डने चुकलेला एक दिवस वाचवा.')),
        ('mission-spark','✧',5,mission_count,dict(en='Mission spark',hi='मिशन की चमक',mr='मोहिमेची चमक'),dict(en='Complete five daily missions.',hi='पाँच दैनिक मिशन पूरे करें।',mr='पाच रोजच्या मोहिमा पूर्ण करा.')),
        ('mission-traveller','🧭',20,mission_count,dict(en='Mission traveller',hi='मिशन का यात्री',mr='मोहिमांचा प्रवासी'),dict(en='Complete twenty daily missions.',hi='बीस दैनिक मिशन पूरे करें।',mr='वीस रोजच्या मोहिमा पूर्ण करा.')),
    ])
    return [dict(id=key,icon=icon,name=title['en'],title=title,goal=goal,current=min(current,target),target=target,earned=current>=target,reward=BADGE_REWARD) for key,icon,target,current,title,goal in rows]


def snapshot(con, child, base_badges=(), challenge=1, zone='UTC', now=None):
    today=ensure(con,child,zone,now)
    config=day_config(con,child,today,challenge)
    daily,events=missions(con,child,today,config)
    current,statuses=streak(con,child,today)
    wallet=con.execute('SELECT * FROM journey_wallets WHERE child_id=?',(child,)).fetchone()
    protected=sum(status=='protected' for status in statuses.values())
    mission_count=con.execute("SELECT COUNT(*) FROM journey_ledger WHERE child_id=? AND reason='mission'",(child,)).fetchone()[0]
    extra_badges=badges(wallet['best_streak'],protected,mission_count)
    for badge in [*base_badges,*extra_badges]:
        if badge['earned']:
            credit(con,child,'badge/'+badge['id'],BADGE_REWARD,'badge',today)
    balance=con.execute('SELECT balance FROM journey_wallets WHERE child_id=?',(child,)).fetchone()[0]
    recent=[dict(row) for row in con.execute('SELECT amount,reason,day FROM journey_ledger WHERE child_id=? ORDER BY rowid DESC LIMIT 8',(child,))]
    earned_today=con.execute('SELECT COALESCE(SUM(amount),0) FROM journey_ledger WHERE child_id=? AND day=? AND amount>0',(child,str(today))).fetchone()[0]
    calendar=[dict(day=str(day),status=statuses.get(str(day),'open' if day==today else 'rest'),today=day==today) for day in [today-timedelta(days=offset) for offset in range(6,-1,-1)]]
    return dict(day=str(today),timezone=wallet['timezone'],streak=current,best=wallet['best_streak'],learned_today=statuses.get(str(today))=='learned',balance=balance,shields=wallet['shields'],shield_price=SHIELD_PRICE,shield_cap=SHIELD_CAP,protected_days=protected,calendar=calendar,missions=daily,earned_today=earned_today,recent=recent,reading_keys=[row['event_key'] for row in events if row['kind']=='reading'],badges=extra_badges)


def buy_shield(con, child, request_id, zone='UTC', now=None):
    today=ensure(con,child,zone,now)
    key='purchase/'+request_id
    if con.execute('SELECT 1 FROM journey_ledger WHERE child_id=? AND entry_key=?',(child,key)).fetchone():
        return
    wallet=con.execute('SELECT * FROM journey_wallets WHERE child_id=?',(child,)).fetchone()
    if wallet['shields']>=SHIELD_CAP:
        raise JourneyError('Your shield pouch is full.')
    if wallet['balance']<SHIELD_PRICE:
        raise JourneyError('You need more Sunseeds for a shield.')
    con.execute('UPDATE journey_wallets SET balance=balance-?,shields=shields+1 WHERE child_id=?',(SHIELD_PRICE,child))
    con.execute('INSERT INTO journey_ledger VALUES(?,?,?,?,?)',(child,key,-SHIELD_PRICE,'shield',str(today)))
