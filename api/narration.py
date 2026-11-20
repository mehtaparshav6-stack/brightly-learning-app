"""Optional AI narration for published curriculum only; no child data is sent."""
import asyncio
import importlib.util
import hashlib
import json
import os
import threading
import urllib.error
import urllib.request
from pathlib import Path

from .content import LESSONS, STORIES, RHYMES, POEMS, LANGUAGES

MODEL = os.environ.get('BRIGHTLY_TTS_MODEL', 'gpt-4o-mini-tts')
VOICE = os.environ.get('BRIGHTLY_TTS_VOICE', 'marin')
STYLE = ('Read exactly the provided text, in its original language, as a warm, gentle storyteller for young children. '
         'Use a sweet, calm, natural voice, clear pronunciation and short pauses between sentences. '
         'Be quietly expressive, never loud, startling, squeaky or exaggerated. Do not add words or sound effects.')
LOCK = threading.Lock()

def singing_configured():
    return bool(os.environ.get('ELEVENLABS_API_KEY', '').strip())


class VoiceUnavailable(Exception):
    pass


def provider():
    selected = os.environ.get('BRIGHTLY_TTS_PROVIDER','edge')
    if selected=='auto':
        return 'openai' if os.environ.get('OPENAI_API_KEY','').strip() else 'edge'
    return selected


def configured():
    if provider()=='edge':
        return importlib.util.find_spec('edge_tts') is not None or (Path(__file__).resolve().parents[1]/'media'/'narration'/'index.json').is_file()
    return provider()=='openai' and bool(os.environ.get('OPENAI_API_KEY','').strip())


def bundled_enabled():
    return os.environ.get('BRIGHTLY_USE_BUNDLED_AUDIO','1')!='0'


def available():
    return configured() or (bundled_enabled() and (Path(__file__).resolve().parents[1]/'media'/'narration'/'index.json').is_file())


async def neural_audio(text, language):
    import edge_tts
    voices={'en':'en-GB-SoniaNeural','hi':'hi-IN-SwaraNeural','mr':'mr-IN-AarohiNeural'}
    reading=edge_tts.Communicate(text,voices[language],rate='-7%',pitch='+0Hz')
    audio=bytearray()
    async for part in reading.stream():
        if part['type']=='audio':
            audio.extend(part['data'])
            if len(audio)>16*1024*1024:
                raise VoiceUnavailable('The reading is too long.')
    if len(audio)<1024:
        raise VoiceUnavailable('The speech service returned no audio.')
    return bytes(audio)



def published_text(kind, item_id, language, part='text', question=0, option=None, level=1):
    if language not in LANGUAGES:
        raise ValueError('Unknown language.')
    if kind=='games' or (kind=='lessons' and part!='text'):
        from .activity_voice import activity_text
        return activity_text(kind,item_id,language,part,question,option,level)
    if part!='text':
        raise ValueError('Reading part not found.')
    collection = {'lessons': LESSONS, 'stories': STORIES, 'rhymes': RHYMES, 'poems': POEMS}.get(kind)
    item = next((item for item in collection or [] if item['id'] == item_id), None)
    if not item or language not in item.get('available_languages',list(item['title'])):
        raise ValueError('Reading or language not found.')
    field = {'lessons': 'story', 'stories': 'text', 'rhymes': 'lines', 'poems': 'lines'}[kind]
    body = item[field][language]
    text = item['title'][language] + '.\n' + ('\n'.join(body) if isinstance(body, list) else body)
    if len(text) > 4000:
        raise ValueError('Reading is too long for this voice.')
    return text


def cache_path(text, language, directory, mode='spoken', voice_provider=None):
    selected=voice_provider or provider()
    model,voice=('gpt-4o-mini-tts','marin') if selected=='edge' else (MODEL,VOICE)
    key = hashlib.sha256(json.dumps([model, voice, STYLE, text, language, mode, selected, 'performance-v3'], ensure_ascii=False).encode()).hexdigest()
    return Path(directory) / (key + '.mp3')


def render_audio(text, language, directory, allow_generation, mode='spoken'):
    bundled=cache_path(text,language,Path(__file__).resolve().parents[1]/'media'/'narration',mode,voice_provider='edge')
    if mode=='spoken' and bundled_enabled() and bundled.is_file():
        return bundled.read_bytes()
    if not (singing_configured() if mode=='sung' else configured()):
        raise VoiceUnavailable('The requested voice service is not configured.')
    path = cache_path(text, language, directory, mode)
    # A single generation at a time avoids duplicate bills for simultaneous clicks.
    if not LOCK.acquire(timeout=2):
        raise VoiceUnavailable('The storyteller is preparing another reading. Please try again shortly.')
    try:
        if path.is_file():
            return path.read_bytes()
        allow_generation()
        if mode=='spoken' and provider()=='edge':
            try:
                audio=asyncio.run(asyncio.wait_for(neural_audio(text,language),timeout=75))
            except Exception as error:
                raise VoiceUnavailable('The neural voice service is unavailable. Try again shortly.') from error
            save_audio(path,audio)
            return audio
        if mode == 'sung':
            endpoint = 'https://api.elevenlabs.io/v1/music?output_format=mp3_44100_128'
            headers = {'xi-api-key': os.environ['ELEVENLABS_API_KEY'].strip(), 'Content-Type':'application/json'}
            lyrics = text.split('\n')[1:]
            duration = max(18000,min(85000,len(lyrics)*5500))
            body = dict(model_id='music_v1',composition_plan={
                'positive_global_styles':['gentle nursery song','warm natural adult singing voice',
                    'clear '+LANGUAGES[language]+' diction','simple original singable melody','soft acoustic accompaniment',
                    'foreground vocals','unhurried tempo'],
                'negative_global_styles':['spoken narration','shouting','distortion','heavy drums','imitating a known singer'],
                'sections':[dict(section_name='Verse',positive_local_styles=['sing every supplied lyric line once in order'],
                    negative_local_styles=['extra lyrics','spoken introduction'],duration_ms=duration,lines=lyrics)]})
        else:
            endpoint = 'https://api.openai.com/v1/audio/speech'
            headers = {'Authorization':'Bearer '+os.environ['OPENAI_API_KEY'].strip(),'Content-Type':'application/json'}
            body = dict(model=MODEL,voice=VOICE,input=text,instructions=STYLE,response_format='mp3',speed=1)
        req = urllib.request.Request(endpoint,data=json.dumps(body).encode(),method='POST',headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=150 if mode=='sung' else 60) as response:
                audio = response.read(16 * 1024 * 1024 + 1)
                if not response.headers.get('Content-Type', '').startswith('audio/') or not audio or len(audio) > 16 * 1024 * 1024:
                    raise VoiceUnavailable('The voice service returned invalid audio.')
        except (urllib.error.URLError, TimeoutError, OSError) as error:
            raise VoiceUnavailable('The AI voice is unavailable. Use the device voice or try again later.') from error
        save_audio(path,audio)
        return audio
    finally:
        LOCK.release()


def save_audio(path,audio,limit_cache=True):
    path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_suffix('.tmp')
    temporary.write_bytes(audio)
    temporary.replace(path)
    if not limit_cache:
        return
    files=sorted(path.parent.glob('*.mp3'),key=lambda file:file.stat().st_mtime,reverse=True)
    size=0
    for index,file in enumerate(files):
        size+=file.stat().st_size
        if index>=512 or size>512*1024*1024:
            file.unlink(missing_ok=True)
