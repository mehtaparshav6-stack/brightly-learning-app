"""Run with: .venv/bin/python -m unittest discover -s tests -v."""
import http.cookiejar
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import MagicMock, patch
import urllib.error
import urllib.request

ROOT=Path(__file__).resolve().parents[1]

class LearningFlow(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp=tempfile.TemporaryDirectory()
        with socket.socket() as sock:
            sock.bind(('127.0.0.1',0)); cls.port=sock.getsockname()[1]
        cls.server=subprocess.Popen([sys.executable,'-m','uvicorn','api.main:app','--host','127.0.0.1','--port',str(cls.port)],cwd=ROOT,env={**os.environ,'BRIGHTLY_DB_PATH':str(Path(cls.tmp.name)/'test.sqlite3'),'OPENAI_API_KEY':'','ELEVENLABS_API_KEY':'','BRIGHTLY_TTS_PROVIDER':'openai','BRIGHTLY_USE_BUNDLED_AUDIO':'0'},stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        cls.base=f'http://127.0.0.1:{cls.port}/api'
        for _ in range(80):
            try:
                urllib.request.urlopen(cls.base+'/session')
            except urllib.error.HTTPError:
                return
            except OSError:
                time.sleep(.1)
        cls.server.terminate(); raise RuntimeError('Test server did not start')
    @classmethod
    def tearDownClass(cls):
        cls.server.terminate(); cls.server.wait(timeout=5); cls.tmp.cleanup()
    def call(self,path,body=None,method=None,client=None,csrf=None):
        request=urllib.request.Request(self.base+path,data=json.dumps(body).encode() if body is not None else None,method=method or ('POST' if body is not None else 'GET'),headers={'Content-Type':'application/json','x-csrf-token':csrf if csrf is not None else self.csrf})
        try:
            response=(client or self.client).open(request)
            return response.status,json.load(response)
        except urllib.error.HTTPError as error:
            return error.code,json.load(error)
    def setUp(self):
        self.client=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()));self.csrf=''
        _,account=self.call('/signup',{'name':'Test Parent','email':f'{time.time_ns()}@example.com','password':'testpassword123'})
        self.csrf=account['csrf']
        status,self.child=self.call('/children',{'name':'Learner','age':5,'language':'en','avatar':'sun'})
        self.assertEqual(status,200);self.path=f'/children/{self.child["id"]}'
    def test_game_feedback_scoring_and_retry_idempotence(self):
        for lang in ['en','hi','mr']:
            status,wrong=self.call(self.path+'/games/check',{'game_id':'habit','question':0,'answer':1,'language':lang})
            self.assertEqual(status,200);self.assertFalse(wrong['correct']);self.assertEqual(wrong['correct_answer'],0);self.assertTrue(wrong['explanation'])
        _,right=self.call(self.path+'/games/check',{'game_id':'habit','question':0,'answer':0})
        self.assertTrue(right['correct'])
        for answers,score in [([1,0,0],0),([0,0,0],1),([0,1,2],3)]:
            body={'game_id':'habit','answers':answers,'attempt_id':f'test-attempt-{score}'}
            status,result=self.call(self.path+'/games',body)
            self.assertEqual(status,200);self.assertEqual(result['game_result']['score'],score)
            _,again=self.call(self.path+'/games',body)
            self.assertEqual(again['stars'],result['stars']);self.assertEqual(len(again['games']),len(result['games']))
        self.assertEqual(self.call(self.path+'/games/check',{'game_id':'habit','question':3,'answer':0})[0],422)
        self.assertEqual(self.call(self.path+'/games',{'game_id':'memory','board':['☀']*6,'moves':list(range(6))})[0],400)
    def test_lessons_unlock_and_keep_first_completion(self):
        self.assertEqual(self.call(self.path+'/lessons/sharing/complete',{'answers':[2]})[0],403)
        _,wrong=self.call(self.path+'/lessons/please/complete',{'answers':[0]})
        self.assertFalse(wrong['correct']);self.assertEqual(wrong['child']['completed'],[])
        _,first=self.call(self.path+'/lessons/please/complete',{'answers':[1]})
        _,repeat=self.call(self.path+'/lessons/please/complete',{'answers':[1]})
        self.assertEqual(first['child']['completions'],repeat['child']['completions'])
        self.assertEqual(repeat['child']['stars'],3)
        _,second=self.call(self.path+'/lessons/thanks/complete',{'answers':[0]})
        self.assertEqual(second['child']['level'],2)
        self.assertEqual(self.call(self.path+'/lessons/sharing/complete',{'answers':[2]})[0],200)
    def test_catalog_complete_and_no_answers_exposed(self):
        _,catalog=self.call('/content')
        self.assertEqual(len(catalog['lessons']),50)
        self.assertEqual(len({l['id'] for l in catalog['lessons']}),50)
        for lesson in catalog['lessons']:
            self.assertNotIn('answer',lesson)
            for key in ('title','story','question','options'):
                self.assertEqual(set(lesson[key]),{'en','hi','mr'})
        for game in catalog['games'].values():
            self.assertNotIn('answers',game)
            self.assertEqual(set(game['levels']),{'1','2','3'})
            for level in game['levels'].values():
                self.assertNotIn('answers',level)
                self.assertNotIn('explanations',level)
                for lang in ('en','hi','mr'):
                    self.assertEqual(len(level['questions'][lang]),3)
    def test_sequence_and_achievement_progress(self):
        _, result = self.call(self.path+'/games/check', {'game_id':'sequence','question':0,'answer':[0,1,2],'language':'hi'})
        self.assertFalse(result['correct'])
        self.assertEqual(result['correct_answer'], [1,2,0])
        self.assertTrue(result['explanations']['hi'])
        self.assertEqual(self.call(self.path+'/games/check', {'game_id':'sequence','question':0,'answer':[1,1,0]})[0],400)
        for game, answers in [('sequence',[[1,2,0]]*3),('habit',[0,1,2]),('count',[1,0,2]),('patterns',[0,1,2])]:
            status, result = self.call(self.path+'/games', {'game_id':game,'answers':answers})
            self.assertEqual(status,200)
            self.assertEqual(result['game_result']['score'],3)
        badges = {badge['id']: badge for badge in result['badges']}
        self.assertTrue(badges['first-game']['earned'])
        self.assertTrue(badges['triple-spark']['earned'])
        self.assertEqual(badges['game-explorer']['current'],4)
        self.assertFalse(badges['memory-friend']['earned'])
        self.assertEqual(set(badges['first-game']['title']),{'en','hi','mr'})

    def test_narration_uses_published_items_and_authentication(self):
        data = {'kind':'stories','item_id':'lion-mouse','language':'hi'}
        self.assertEqual(self.call('/narration', data, csrf='bad')[0],403)
        self.assertEqual(self.call('/narration', data)[0],503)
        self.assertEqual(self.call('/narration', {**data,'item_id':'unknown'})[0],404)
        _, catalog = self.call('/content')
        self.assertFalse(catalog['narration']['ai_available'])
        self.assertEqual(len(catalog['stories']),24)
        self.assertEqual(len(catalog['rhymes']),11)
        for item, field in [(story,'text') for story in catalog['stories']]+[(rhyme,'lines') for rhyme in catalog['rhymes']]:
            self.assertTrue({'en','hi'} <= set(item[field]))
    def test_child_language_is_saved_and_private(self):
        self.assertEqual(self.call(self.path+'/language',{'language':'hi'},method='PUT',csrf='wrong')[0],403)
        self.assertEqual(self.call(self.path+'/language',{'language':'hi'},method='PUT')[0],200)
        _,children=self.call('/children')
        self.assertEqual(children[0]['language'],'hi')
        self.assertEqual(children[0]['name'],'Learner')
        self.assertEqual(children[0]['completed'],[])
        self.assertEqual(self.call(self.path+'/language',{'language':'unknown'},method='PUT')[0],422)
        other=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
        _,account=self.call('/signup',{'name':'Other','email':f'{time.time_ns()}@example.com','password':'testpassword123'},client=other)
        self.assertEqual(self.call(self.path+'/language',{'language':'en'},method='PUT',client=other,csrf=account['csrf'])[0],404)

    def test_journey_rewards_purchases_and_private_wallet(self):
        _,start=self.call(self.path+'/journey')
        self.assertEqual((start['journey']['streak'],start['journey']['balance'],start['journey']['shields']),(0,20,1))
        _,wrong=self.call(self.path+'/lessons/please/complete',{'answers':[0]})
        self.assertEqual(wrong['child']['journey']['streak'],0)
        _,right=self.call(self.path+'/lessons/please/complete',{'answers':[1]})
        wallet=right['child']['journey']
        self.assertEqual(wallet['streak'],1)
        self.assertGreaterEqual(wallet['balance'],47)
        _,repeat=self.call(self.path+'/lessons/please/complete',{'answers':[1]})
        self.assertEqual(repeat['child']['journey']['balance'],wallet['balance'])
        purchase={'request_id':'a-test-shield-123'}
        self.assertEqual(self.call(self.path+'/shields',purchase,csrf='wrong')[0],403)
        status,bought=self.call(self.path+'/shields',purchase)
        self.assertEqual(status,200)
        self.assertEqual(bought['journey']['balance'],wallet['balance']-40)
        self.assertEqual(bought['journey']['shields'],2)
        self.assertEqual(bought['stars'],right['child']['stars'])
        _,retried=self.call(self.path+'/shields',purchase)
        self.assertEqual(retried['journey'],bought['journey'])
        self.assertEqual(self.call(self.path+'/shields',{'request_id':'insufficient-funds'})[0],400)
        other=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
        _,account=self.call('/signup',{'name':'Other','email':f'{time.time_ns()}@example.com','password':'testpassword123'},client=other)
        self.assertEqual(self.call(self.path+'/journey',client=other,csrf=account['csrf'])[0],404)
        self.assertEqual(self.call(self.path+'/shields',purchase,client=other,csrf=account['csrf'])[0],404)

    def test_parallel_shield_purchases_cannot_overspend(self):
        import concurrent.futures
        self.call(self.path+'/lessons/please/complete',{'answers':[1]})
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
            responses=list(pool.map(lambda index:self.call(self.path+'/shields',{'request_id':f'parallel-purchase-{index}'}),range(2)))
        self.assertEqual(sorted(status for status,_ in responses),[200,400])
        _,result=self.call(self.path+'/journey')
        self.assertEqual((result['journey']['balance'],result['journey']['shields']),(7,2))

    def test_every_verse_has_a_creator_recording(self):
        _,catalog=self.call('/content')
        for item in [*catalog['poems'],*catalog['rhymes']]:
            self.assertEqual(len(item['recording']['youtube_id']),11)
            self.assertIn(item['recording']['language'],('en','hi'))
            self.assertTrue(item['recording']['channel'])
            self.assertIn(item['recording']['style'],('song','recitation'))
        self.assertFalse(catalog['narration']['singing_available'])

    def test_activity_narration_accepts_only_published_parts(self):
        base={'kind':'lessons','item_id':'please','language':'hi','part':'question'}
        self.assertEqual(self.call('/narration',base)[0],503)
        self.assertEqual(self.call('/narration',{**base,'part':'option','option':0})[0],503)
        self.assertEqual(self.call('/narration',{**base,'part':'option','option':8})[0],404)
        self.assertEqual(self.call('/narration',{**base,'part':'answer'})[0],404)
        self.assertEqual(self.call('/narration',{'kind':'games','item_id':'memory','language':'hi','part':'instructions'})[0],503)
        for part in ('question','option'):
            self.assertEqual(self.call('/narration',{'kind':'games','item_id':'unknown','language':'hi','part':part})[0],404)
        self.assertEqual(self.call('/narration',{'kind':'games','item_id':'count','language':'hi','part':'question','level':4})[0],422)

    def test_activity_voice_catalog_languages_and_choices(self):
        from api.activity_voice import activity_requests
        from api.narration import published_text
        requests=list(activity_requests())
        self.assertGreater(len(requests),1000)
        for request in requests:
            text=published_text(**request)
            self.assertTrue(text.strip(),request)
            self.assertLessEqual(len(text),4000,request)
        question=published_text('lessons','please','hi',part='question')
        self.assertIn('विकल्प 1',question)
        self.assertIn('विकल्प 3',question)
        self.assertNotIn('Choice',question)
        self.assertNotEqual(question,published_text('lessons','please','en',part='question'))
        self.assertIn('गोला',published_text('games','shapes','hi',part='option',option=0))

    def test_difficulty_gate_and_saved_progress(self):
        payload={'game_id':'count','game_level':2,'answers':[1,0,2]}
        self.assertEqual(self.call(self.path+'/games',payload)[0],403)
        self.call(self.path+'/games',{'game_id':'count','answers':[1,1,0]})
        self.assertEqual(self.call(self.path+'/games',payload)[0],403)
        self.call(self.path+'/games',{'game_id':'count','answers':[1,0,2]})
        _,result=self.call(self.path+'/games',payload)
        self.assertEqual(result['game_result']['level'],2)
        self.assertEqual(result['game_progress']['count']['unlocked'],3)
        self.assertEqual(result['game_progress']['count']['best']['1'],3)
        from api.game_levels import game_bank
        status,result=self.call(self.path+'/games',{**payload,'game_level':3,'answers':game_bank('count',3)['answers']})
        self.assertEqual(status,200)
        self.assertTrue(next(badge for badge in result['badges'] if badge['id']=='challenge-star')['earned'])
        _,children=self.call('/children')
        self.assertEqual(children[0]['game_progress']['count']['best']['3'],3)
    def test_reading_badges_persistence_and_privacy(self):
        body={'kind':'stories','item_id':'lion-mouse','language':'en'}
        self.assertEqual(self.call(self.path+'/readings',body,csrf='bad')[0],403)
        status,first=self.call(self.path+'/readings',body)
        self.assertEqual(status,200)
        self.assertTrue(next(b for b in first['badges'] if b['id']=='story-spark')['earned'])
        _,repeated=self.call(self.path+'/readings',body)
        self.assertEqual(first['readings'],repeated['readings'])
        _,bilingual=self.call(self.path+'/readings',{**body,'language':'hi'})
        self.assertTrue(next(b for b in bilingual['badges'] if b['id']=='two-languages')['earned'])
        _,poem=self.call(self.path+'/readings',{'kind':'poems','item_id':'utho-lal','language':'hi'})
        self.assertTrue(next(b for b in poem['badges'] if b['id']=='rhyme-spark')['earned'])
        self.assertEqual(len(poem['badges']),32)
        self.assertEqual(self.call(self.path+'/readings',{**body,'language':'mr'})[0],404)
        self.assertEqual(self.call(self.path+'/readings',{**body,'item_id':'missing'})[0],404)
        _,catalog=self.call('/content')
        for story in catalog['stories']:
            self.assertGreaterEqual(len(story['text']['en'].split()),120)
            self.assertGreaterEqual(len(story['text']['hi'].split()),110)
            self.assertTrue(story['moral']['hi'])
            self.assertTrue(story['source_url'].startswith('https://'))
    def test_habits_persist_and_are_private(self):
        from datetime import date
        day=date.today().isoformat()
        for _ in range(2):
            status,summary=self.call(self.path+'/habits',{'day':day,'habit':'kind','checked':True})
            self.assertEqual(status,200);self.assertEqual(summary['checked'],['kind']);self.assertEqual(summary['streak'],1)
        self.assertEqual(self.call(self.path+'/habits?day='+day)[1]['checked'],['kind'])
        self.assertEqual(self.call(self.path+'/habits',{'day':day,'habit':'kind','checked':False})[1]['checked'],[])
        stranger=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
        _,account=self.call('/signup',{'name':'Other Parent','email':f'{time.time_ns()}@example.com','password':'testpassword123'},client=stranger,csrf='')
        status,_=self.call(self.path+'/games/check',{'game_id':'habit','question':0,'answer':0},client=stranger,csrf=account['csrf'])
        self.assertEqual(status,404)
        self.assertEqual(self.call(self.path+'/habits?day='+day,client=stranger,csrf=account['csrf'])[0],404)
        self.assertEqual(self.call(self.path+'/habits',{'day':day,'habit':'kind','checked':True},csrf='bad')[0],403)

class NarrationProvider(unittest.TestCase):
    def test_bundled_hindi_does_not_need_a_connected_account(self):
        from api import narration
        text=narration.published_text('lessons','please','hi',part='question')
        with tempfile.TemporaryDirectory() as directory,patch.dict(os.environ,{'OPENAI_API_KEY':'','BRIGHTLY_TTS_PROVIDER':'openai','BRIGHTLY_USE_BUNDLED_AUDIO':'1'}),patch.object(narration,'MODEL','custom-model'),patch.object(narration,'VOICE','custom-voice'),patch('api.narration.urllib.request.urlopen') as send:
            reserve=MagicMock()
            audio=narration.render_audio(text,'hi',directory,reserve)
            self.assertGreater(len(audio),1000)
            reserve.assert_not_called()
            send.assert_not_called()
            self.assertTrue(narration.available())

    def test_renders_only_catalog_text_and_reuses_audio(self):
        from api import narration
        text = narration.published_text('poems','the-star','hi')
        self.assertIn('तारा', text)
        response = MagicMock()
        response.__enter__.return_value = response
        response.headers = {'Content-Type':'audio/mpeg'}
        response.read.return_value = b'ID3 test audio'
        with tempfile.TemporaryDirectory() as directory, patch.dict(os.environ, {'OPENAI_API_KEY':'test-only','BRIGHTLY_TTS_PROVIDER':'openai','BRIGHTLY_USE_BUNDLED_AUDIO':'0'}), patch('api.narration.urllib.request.urlopen', return_value=response) as send:
            reserve = MagicMock()
            first = narration.render_audio(text, 'hi', directory, reserve)
            cached = narration.render_audio(text, 'hi', directory, reserve)
            self.assertEqual(first, cached)
            reserve.assert_called_once()
            send.assert_called_once()
            request = send.call_args.args[0]
            payload = json.loads(request.data)
            self.assertEqual(request.full_url, 'https://api.openai.com/v1/audio/speech')
            self.assertEqual(payload['input'], text)
            self.assertIn('gentle storyteller', payload['instructions'])

class SingingProvider(unittest.TestCase):
    def test_singing_uses_composition_lyrics_and_distinct_cache(self):
        from api import narration
        text=narration.published_text('rhymes','twinkle','en')
        response=MagicMock()
        response.__enter__.return_value=response
        response.headers={'Content-Type':'audio/mpeg'}
        response.read.return_value=b'ID3 singing test'
        with tempfile.TemporaryDirectory() as directory, patch.dict(os.environ,{'ELEVENLABS_API_KEY':'test-only'}), patch('api.narration.urllib.request.urlopen',return_value=response) as send:
            narration.render_audio(text,'en',directory,lambda:None,mode='sung')
            request=send.call_args.args[0]
            self.assertEqual(request.full_url,'https://api.elevenlabs.io/v1/music?output_format=mp3_44100_128')
            plan=json.loads(request.data)['composition_plan']
            self.assertEqual(plan['sections'][0]['lines'],text.split('\n')[1:])
            self.assertNotEqual(narration.cache_path(text,'en',directory),narration.cache_path(text,'en',directory,'sung'))

if __name__=='__main__':unittest.main()
