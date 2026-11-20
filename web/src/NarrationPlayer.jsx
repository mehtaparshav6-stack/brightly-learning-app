import React,{useEffect,useRef,useState} from 'react';
import {narrationAudio} from './api';
import {audioWords,preferredVoice,useAudio} from './Audio.jsx';

export function splitReading(text){
 return Array.isArray(text)?text:(text.match(/[^.!?।]+[.!?।]*[”’"']*/gu)||[text]).map(line=>line.trim()).filter(Boolean);
}

export default function NarrationPlayer({kind,item,lang,narration,lines=false,readingText,requestData={},compact=false,label}){
 const {settings,update,voices,unlock,claimNarration,releaseNarration}=useAudio();
 const owner=useRef(Symbol('narration'));
 const words=audioWords[lang];
 const music={
  en:{sing:'Sing',read:'Read aloud',sung:'AI sung rhyme',needs:'Sung playback needs the singing service configured by a parent. Read aloud is available below.',singNote:'AI-generated singing with an original melody.',songLoading:'Preparing the complete song. This can take a moment…'},
  hi:{sing:'गाकर सुनें',read:'पढ़कर सुनें',sung:'AI से गाई कविता',needs:'गाकर सुनाने के लिए अभिभावक को गायन सेवा जोड़नी होगी। अभी पढ़कर सुन सकते हैं।',singNote:'AI गायन और नई धुन।',songLoading:'पूरा गीत तैयार हो रहा है। थोड़ा समय लग सकता है…'},
  mr:{sing:'गाऊन ऐका',read:'वाचून ऐका',sung:'AI ने गायलेली कविता',needs:'गायनासाठी पालकांनी सेवा जोडावी. आत्ता वाचून ऐकू शकता.',singNote:'AI गायन आणि नवी चाल.',songLoading:'संपूर्ण गाणे तयार होत आहे. थोडा वेळ लागू शकतो…'}
 }[lang];
 const text=readingText??(kind==='lessons'?item.story[lang]:kind==='stories'?item.text[lang]:item.lines[lang]);
 const segments=kind==='stories'?text.split(/\n+/).map(part=>part.trim()).filter(Boolean):splitReading(text);
 const [mode,setMode]=useState(kind==='rhymes'&&narration?.singing_available?'sung':'spoken');
 const [state,setState]=useState('idle');
 const [active,setActive]=useState(-1);
 const [error,setError]=useState('');
 const [position,setPosition]=useState(0);
 const [duration,setDuration]=useState(0);
 const [source,setSource]=useState('');
 const generation=useRef(0),media=useRef(null),url=useRef(null),request=useRef(null),utterance=useRef(null),playState=useRef('idle');
 const settingsRef=useRef(settings);settingsRef.current=settings;
 const useAI=mode==='sung'?narration?.singing_available:(narration?.ai_available&&settings.source!=='device');
 const currentSource=source||(useAI?'ai':'device');

 function transition(next){playState.current=next;setState(next)}
 function clear(){
  generation.current++;
  releaseNarration(owner.current);
  request.current?.abort();request.current=null;
  if(media.current){
   const audio=media.current;
   audio.onended=audio.onerror=audio.ontimeupdate=audio.onloadedmetadata=null;
   audio.pause();audio.removeAttribute('src');audio.load();media.current=null;
  }
  if(url.current){URL.revokeObjectURL(url.current);url.current=null}
  if(utterance.current){
   utterance.current.onend=utterance.current.onerror=utterance.current.onboundary=null;
   utterance.current=null;window.speechSynthesis?.cancel();
  }
  playState.current='idle';
 }
 function stop(){clear();setState('idle');setActive(-1);setPosition(0);setDuration(0);setError('');setSource('')}
 useEffect(()=>()=>clear(),[]);
 const readingKey=JSON.stringify([kind,item.id,lang,requestData]);
 useEffect(()=>{stop()},[settings.source,settings.voices[lang],readingKey]);
 useEffect(()=>{
  if(media.current){media.current.volume=settings.volume;media.current.playbackRate=mode==='sung'?1:settings.rate/.88}
  if(utterance.current&&settings.volume===0)pause()
 },[settings.volume,settings.rate]);
 useEffect(()=>{
  function hide(){if(document.hidden&&playState.current==='playing')pause()}
  document.addEventListener('visibilitychange',hide);
  return()=>document.removeEventListener('visibilitychange',hide);
 },[]);

 function startDevice(){
  stop();claimNarration(owner.current,stop);setSource('device');unlock();
  const synth=window.speechSynthesis;
  const voice=preferredVoice(synth?.getVoices()||voices,lang,settings.voices[lang]);
  if(!synth||!voice){setError(words.unavailable);transition('error');return}
  synth.cancel();synth.resume();
  const token=generation.current;
  const fullText=segments.join(lines?'\n':' ');
  const utter=new SpeechSynthesisUtterance(fullText);utterance.current=utter;
  utter.lang={en:'en-US',hi:'hi-IN',mr:'mr-IN'}[lang];utter.voice=voice;
  utter.rate=settings.rate;utter.pitch=1;utter.volume=settings.volume;
  const offsets=[];let offset=0;
  for(const segment of segments){offsets.push(offset);offset+=segment.length+1}
  utter.onboundary=event=>{
   if(token!==generation.current)return;
   const index=offsets.findLastIndex(start=>start<=event.charIndex);
   setActive(index);
  };
  utter.onend=()=>{if(token===generation.current){setActive(-1);transition('ended')}};
  utter.onerror=event=>{
   if(token===generation.current&&!['interrupted','canceled'].includes(event.error)){
    setError(words.unavailable);transition('error');
   }
  };
  setActive(0);transition('playing');synth.speak(utter);
 }
 async function start(){
  if(settingsRef.current.volume<=0){setError(({en:'Voice volume is turned down. Turn on the voice to listen.',hi:'आवाज़ का स्तर शून्य है। सुनने के लिए आवाज़ चालू करें।',mr:'आवाज शून्य आहे. ऐकण्यासाठी आवाज सुरू करा.'})[lang]);transition('error');return}
  if(!useAI){startDevice();return}
  stop();claimNarration(owner.current,stop);setSource('ai');transition('loading');unlock();
  const token=generation.current;request.current=new AbortController();
  try{
   const blob=await narrationAudio({kind,item_id:item.id,language:lang,mode,...requestData},request.current.signal);
   if(token!==generation.current)return;
   url.current=URL.createObjectURL(blob);
   const audio=new Audio(url.current);media.current=audio;
   audio.preload='auto';audio.volume=settingsRef.current.volume;
   audio.playbackRate=mode==='sung'?1:settingsRef.current.rate/.88;
   audio.ontimeupdate=()=>{if(token===generation.current)setPosition(audio.currentTime)};
   audio.onloadedmetadata=()=>{if(token===generation.current)setDuration(Number.isFinite(audio.duration)?audio.duration:0)};
   audio.onended=()=>{if(token===generation.current)transition('ended')};
   audio.onerror=()=>{if(token===generation.current){setError(words.failed);transition('error')}};
   await playMedia(token);
  }catch(err){
   if(token!==generation.current||err.name==='AbortError')return;
   setError(words.failed);transition('error');
  }
 }
 async function playMedia(token){
  try{await media.current.play();if(token===generation.current)transition('playing')}
  catch{if(token===generation.current){setError(words.playBlocked);transition('paused')}}
 }
 function pause(){
  if(playState.current!=='playing')return;
  transition('paused');
  if(media.current){media.current.pause();setPosition(media.current.currentTime)}
  else window.speechSynthesis?.pause();
 }
 function resume(){
  setError('');
  if(media.current)playMedia(generation.current);
  else{window.speechSynthesis?.resume();transition('playing')}
 }
 const statusText={idle:words.ready,loading:mode==='sung'?music.songLoading:words.loading,playing:words.playing,paused:words.paused,ended:words.ended,error:''}[state];
 if(compact){
  const compactWords={en:{loading:'Preparing audio…',pause:'Pause audio',resume:'Resume audio',stop:'Stop audio',ready:'Listen again'},hi:{loading:'आवाज़ तैयार हो रही है…',pause:'आवाज़ रोककर ठहरें',resume:'आवाज़ जारी रखें',stop:'आवाज़ बंद करें',ready:'फिर सुनें'},mr:{loading:'आवाज तयार होत आहे…',pause:'आवाजाला विराम द्या',resume:'आवाज पुढे ऐका',stop:'आवाज थांबवा',ready:'पुन्हा ऐका'}}[lang];
  const controlLabel=state==='playing'?compactWords.pause:state==='paused'?compactWords.resume:state==='loading'?compactWords.loading:label||words.listen;
  return <div className={'narration-player activity-listen '+(compact==='icon'?'listen-icon':'listen-bar')} data-state={state}>
   <button type="button" className="voice-control" aria-label={controlLabel} title={controlLabel} disabled={state==='loading'} onClick={state==='playing'?pause:state==='paused'?resume:start}>
    <span className="voice-speaker" aria-hidden="true">{state==='playing'?'Ⅱ':state==='paused'?'▶':'🔊'}</span>{compact!=='icon'&&<span>{controlLabel}</span>}
   </button>
   {compact!=='icon'&&['loading','playing','paused'].includes(state)&&<button type="button" className="voice-control voice-stop" aria-label={compactWords.stop} title={compactWords.stop} onClick={stop}>■</button>}
   {state==='loading'&&<span className="sr-only" role="status">{compactWords.loading}</span>}
   {error&&<div role="alert" className="activity-voice-error"><p>{error}</p>{settings.volume<=0?<button type="button" className="voice-control" onClick={()=>{update({volume:.55});stop()}}>{({en:'Turn on voice',hi:'आवाज़ चालू करें',mr:'आवाज सुरू करा'})[lang]}</button>:source==='ai'&&state==='error'&&<button type="button" className="voice-control" onClick={startDevice}>{words.useDevice}</button>}</div>}
  </div>;
 }
 return <div className={'narrated-reading '+(lines?'verse-reading':'')}>
  {kind==='rhymes'&&<><div className="playback-style" role="group" aria-label={music.read}>
   <button aria-pressed={mode==='spoken'} onClick={()=>{stop();setMode('spoken')}}>{music.read}</button>
   <button aria-pressed={mode==='sung'} disabled={!narration?.singing_available} onClick={()=>{stop();setMode('sung')}}>♫ {music.sing}</button>
  </div>{!narration?.singing_available&&<p className="game-level-note">{music.needs}</p>}</>}
  <div className="narration-player" data-state={state}>
   <div className="narration-heading"><span className="voice-flower" aria-hidden="true">{mode==='sung'?'♫':'✿'}</span><div><strong>{mode==='sung'?music.sung:currentSource==='ai'?(narration?.provider==='edge'?({en:'Neural storyteller',hi:'कहानी सुनाने वाली आवाज़',mr:'कथाकथनाचा आवाज'})[lang]:words.ai):words.device}</strong><p role="status">{statusText}</p></div><span className={'voice-bars '+(state==='playing'?'is-playing':'')} aria-hidden="true"><i/><i/><i/><i/><i/></span></div>
   <div className="learning-actions">
    {state==='playing'?<button className="button button-dark" onClick={pause}>Ⅱ {words.pause}</button>:state==='paused'?<button className="button button-dark" onClick={resume}>▶ {words.resume}</button>:<button className="button button-dark" disabled={state==='loading'} onClick={start}>▶ {state==='ended'?words.restart:mode==='sung'?music.sing:words.listen}</button>}
    {['loading','playing','paused'].includes(state)&&<button className="button button-outline" onClick={stop}>■ {words.stop}</button>}
   </div>
   {currentSource==='ai'&&duration>0&&<label className="audio-position">{words.position}<input type="range" min="0" max={duration} step=".1" value={position} onChange={event=>{if(media.current){media.current.currentTime=Number(event.target.value);setPosition(Number(event.target.value))}}}/><span>{Math.floor(position)} / {Math.ceil(duration)} s</span></label>}
   {error&&<div role="alert" className="voice-error"><p>{error}</p>{settings.volume<=0?<button className="button button-outline" onClick={()=>{update({volume:.55});stop()}}>{({en:'Turn on voice',hi:'आवाज़ चालू करें',mr:'आवाज सुरू करा'})[lang]}</button>:source==='ai'&&state==='error'&&<button className="button button-outline" onClick={()=>{setMode('spoken');startDevice()}}>{words.useDevice}</button>}</div>}
   <small>{mode==='sung'?music.singNote:currentSource==='ai'?(narration?.provider==='edge'?({en:'Microsoft neural voice · the published text is sent to the speech service.',hi:'Microsoft की न्यूरल आवाज़ · प्रकाशित पाठ स्पीच सेवा को भेजा जाता है।',mr:'Microsoft न्यूरल आवाज · प्रकाशित मजकूर स्पीच सेवेला पाठवला जातो.'})[lang]:words.aiNote):words.deviceNote}</small>
  </div>
  <div className="read-along" aria-label={item.title[lang]}>{segments.map((segment,index)=>kind==='stories'?<p className={active===index?'reading-active':''} key={index}>{segment}</p>:<span className={active===index?'reading-active':''} key={index}>{segment}{lines?<br/>:' '}</span>)}</div>
 </div>
}
