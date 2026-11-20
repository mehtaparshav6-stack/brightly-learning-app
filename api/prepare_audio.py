"""Prepare complete tracks before a session to avoid waiting on first playback.

Example: python -m api.prepare_audio --kind rhymes --id twinkle --language en --mode sung
"""
import argparse
import os
from pathlib import Path

from . import narration


def main():
    parser=argparse.ArgumentParser(description='Prepare one published Brightly audio track.')
    parser.add_argument('--kind',choices=['lessons','stories','rhymes','poems'],required=True)
    parser.add_argument('--id',required=True,help='ID of the published curriculum item')
    parser.add_argument('--language',choices=['en','hi','mr'],required=True)
    parser.add_argument('--mode',choices=['spoken','sung'],default='spoken')
    args=parser.parse_args()
    if args.mode=='sung' and args.kind!='rhymes':
        parser.error('Sung playback is available for rhymes.')
    database=Path(os.environ.get('BRIGHTLY_DB_PATH',Path(__file__).resolve().parents[1]/'brightly.sqlite3'))
    try:
        text=narration.published_text(args.kind,args.id,args.language)
        audio=narration.render_audio(text,args.language,database.parent/'.brightly-audio',lambda:None,args.mode)
    except (ValueError,narration.VoiceUnavailable,OSError) as error:
        parser.exit(1,str(error)+'\n')
    print(f'Prepared {args.kind}/{args.id} ({args.language}, {args.mode}), {len(audio):,} bytes.')
    print(narration.cache_path(text,args.language,database.parent/'.brightly-audio',args.mode))


if __name__=='__main__':
    main()
