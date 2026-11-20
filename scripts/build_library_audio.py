"""Prepare bundled neural narration for the published reading library."""
import asyncio
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from api.content import STORIES,RHYMES,POEMS
from api import narration


async def main():
    directory=ROOT/'media'/'narration'
    directory.mkdir(parents=True,exist_ok=True)
    semaphore=asyncio.Semaphore(6)
    completed=[]
    failures=[]

    async def prepare(kind,item,language):
        text=narration.published_text(kind,item['id'],language)
        file=narration.cache_path(text,language,directory)
        async with semaphore:
            for attempt in range(3):
                try:
                    if not file.is_file():
                        audio=await asyncio.wait_for(narration.neural_audio(text,language),timeout=100)
                        narration.save_audio(file,audio,limit_cache=False)
                    completed.append(dict(kind=kind,item_id=item['id'],language=language,file=file.name,bytes=file.stat().st_size))
                    print(f"READY {kind}/{item['id']} {language} ({len(completed)})",flush=True)
                    return
                except Exception as error:
                    if attempt<2:
                        await asyncio.sleep(2)
                    else:
                        failures.append(dict(kind=kind,item_id=item['id'],language=language,error=type(error).__name__))
                        print(f"FAILED {kind}/{item['id']} {language}: {type(error).__name__}",flush=True)

    await asyncio.gather(*(prepare(kind,item,lang) for kind,items in [('stories',STORIES),('rhymes',RHYMES),('poems',POEMS)] for item in items for lang in item.get('available_languages',list(item['title']))))
    (directory/'index.json').write_text(json.dumps(dict(provider='Microsoft Edge neural speech',voices=dict(en='en-GB-SoniaNeural',hi='hi-IN-SwaraNeural',mr='mr-IN-AarohiNeural'),tracks=completed,failures=failures),ensure_ascii=False,indent=2)+'\n')
    print(f'COMPLETE {len(completed)} tracks; {len(failures)} failures',flush=True)
    if failures:
        sys.exit(1)


if __name__=='__main__':
    asyncio.run(main())
