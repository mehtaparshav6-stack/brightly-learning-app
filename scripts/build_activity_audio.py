"""Bundle neural lesson/game readings; deduplicate repeated choices and instructions."""
import asyncio
import json
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
os.environ['BRIGHTLY_TTS_PROVIDER'] = 'edge'
from api import narration
from api.activity_voice import activity_requests


async def main():
    directory = ROOT / 'media' / 'narration'
    directory.mkdir(parents=True, exist_ok=True)
    tracks, unique = [], {}
    for request in activity_requests():
        text = narration.published_text(**request)
        path = narration.cache_path(text, request['language'], directory)
        tracks.append({**request, 'file': path.name})
        unique[path.name] = (text, request['language'], path)
    semaphore = asyncio.Semaphore(12)
    failures, ready = [], []

    async def prepare(text, language, path):
        async with semaphore:
            for attempt in range(3):
                try:
                    if not path.is_file():
                        data = await asyncio.wait_for(narration.neural_audio(text, language), timeout=100)
                        temporary = path.with_suffix('.tmp')
                        temporary.write_bytes(data)
                        temporary.replace(path)
                    ready.append(path.name)
                    print(f'READY {len(ready)}/{len(unique)} {language} {path.name[:12]}', flush=True)
                    return
                except Exception as error:
                    if attempt < 2:
                        await asyncio.sleep(2)
                    else:
                        failures.append(dict(file=path.name, language=language, error=type(error).__name__))
                        print(f'FAILED {path.name}: {type(error).__name__}', flush=True)

    await asyncio.gather(*(prepare(*values) for values in unique.values()))
    (directory / 'activities.json').write_text(json.dumps(dict(provider='Microsoft Edge neural speech', tracks=tracks, unique_files=len(unique), failures=failures), ensure_ascii=False, indent=2) + '\n')
    print(f'COMPLETE {len(ready)} unique tracks for {len(tracks)} activity controls; {len(failures)} failures', flush=True)
    if failures:
        sys.exit(1)


if __name__ == '__main__':
    asyncio.run(main())
