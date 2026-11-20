import React,{createContext,useCallback,useContext,useEffect,useRef,useState} from 'react';

const AudioContextState=createContext(null);
const defaults={effects:true,volume:.55,rate:.88,source:'auto',voices:{}};
export const audioWords={
 en:{sounds:'Tap and answer sounds',on:'On',off:'Off',settings:'Sound & voice',volume:'Volume',pace:'Reading pace',voice:'Device voice',automatic:'Gentle voice · automatic',slow:'Unhurried',normal:'Natural',source:'Narration source',auto:'AI when available',device:'Device voice',ai:'AI storyteller',listen:'Listen together',pause:'Pause',resume:'Resume',stop:'Stop',restart:'Read again',loading:'Getting the story ready…',ready:'A little listening moment',playing:'Listening together',paused:'Take your time. We’ll wait.',ended:'The end. What did you notice?',failed:'The AI voice is unavailable right now. Try the device voice below.',unavailable:'No voice for this language is installed. Add one in your device’s speech settings, or use configured AI narration. You can still read together.',playBlocked:'Tap Resume to start the audio.',useDevice:'Use device voice',aiNote:'AI-generated voice · only this published text is sent to the voice service.',deviceNote:'Uses your device’s speech service. Available voices vary by device.',position:'Audio position',close:'Close sound settings'},
 hi:{sounds:'टैप और उत्तर की ध्वनि',on:'चालू',off:'बंद',settings:'ध्वनि और आवाज़',volume:'आवाज़ का स्तर',pace:'पढ़ने की गति',voice:'डिवाइस की आवाज़',automatic:'मधुर आवाज़ · अपने आप',slow:'धीरे',normal:'सामान्य',source:'कथावाचन का स्रोत',auto:'उपलब्ध होने पर AI',device:'डिवाइस की आवाज़',ai:'AI कथावाचक',listen:'साथ सुनें',pause:'विराम',resume:'जारी रखें',stop:'रोकें',restart:'फिर सुनें',loading:'कहानी तैयार हो रही है…',ready:'थोड़ा सुनने का समय',playing:'साथ सुन रहे हैं',paused:'अपना समय लें। हम रुकेंगे।',ended:'कहानी पूरी हुई। आपने क्या देखा?',failed:'AI आवाज़ अभी नहीं चल रही। नीचे डिवाइस की आवाज़ आज़माएँ।',unavailable:'इस भाषा की आवाज़ नहीं मिली। डिवाइस की स्पीच सेटिंग में जोड़ें या उपलब्ध AI आवाज़ चुनें। साथ पढ़ना जारी रख सकते हैं।',playBlocked:'ऑडियो शुरू करने के लिए जारी रखें दबाएँ।',useDevice:'डिवाइस की आवाज़ चुनें',aiNote:'AI से बनी आवाज़ · केवल प्रकाशित पाठ वॉइस सेवा को भेजा जाता है।',deviceNote:'डिवाइस की स्पीच सेवा इस्तेमाल होती है। आवाज़ें डिवाइस के अनुसार बदलती हैं।',position:'ऑडियो का स्थान',close:'ध्वनि सेटिंग बंद करें'},
 mr:{sounds:'टॅप आणि उत्तरांचे आवाज',on:'चालू',off:'बंद',settings:'ध्वनी आणि आवाज',volume:'आवाजाची पातळी',pace:'वाचनाचा वेग',voice:'उपकरणाचा आवाज',automatic:'गोड आवाज · आपोआप',slow:'हळूहळू',normal:'नेहमीचा',source:'कथनाचा स्रोत',auto:'उपलब्ध असेल तेव्हा AI',device:'उपकरणाचा आवाज',ai:'AI कथाकथन',listen:'एकत्र ऐका',pause:'विराम',resume:'पुढे ऐका',stop:'थांबवा',restart:'पुन्हा ऐका',loading:'गोष्ट तयार होत आहे…',ready:'थोडा ऐकण्याचा वेळ',playing:'एकत्र ऐकत आहोत',paused:'वेळ घ्या. आपण थांबूया.',ended:'गोष्ट संपली. काय लक्षात आले?',failed:'AI आवाज आत्ता उपलब्ध नाही. खाली उपकरणाचा आवाज वापरा.',unavailable:'या भाषेचा आवाज मिळाला नाही. उपकरणाच्या स्पीच सेटिंगमध्ये जोडा किंवा उपलब्ध AI आवाज वापरा. एकत्र वाचू शकता.',playBlocked:'ऑडिओ सुरू करण्यासाठी पुढे ऐका दाबा.',useDevice:'उपकरणाचा आवाज वापरा',aiNote:'AI ने बनवलेला आवाज · फक्त प्रकाशित मजकूर वॉइस सेवेला पाठवला जातो.',deviceNote:'उपकरणाची स्पीच सेवा वापरली जाते. आवाज उपकरणानुसार बदलतात.',position:'ऑडिओची जागा',close:'ध्वनी सेटिंग बंद करा'}
};

export function AudioProvider({children}){
 const [settings,setSettings]=useState(()=>{try{const saved=JSON.parse(localStorage.getItem('brightly-audio')||'{}');return {...defaults,...saved,volume:Math.max(0,Math.min(1,Number(saved.volume??defaults.volume))),rate:Math.max(.7,Math.min(1.05,Number(saved.rate??defaults.rate))),voices:saved.voices||{}}}catch{return defaults}});
 const [voices,setVoices]=useState([]);const context=useRef(null),tones=useRef(new Set()),current=useRef(settings),narrator=useRef(null);current.current=settings;
 const stopNarration=useCallback(()=>{const previous=narrator.current;narrator.current=null;previous?.stop()},[]);
 const claimNarration=useCallback((owner,stop)=>{if(narrator.current?.owner!==owner)stopNarration();narrator.current={owner,stop}},[stopNarration]);
 const releaseNarration=useCallback(owner=>{if(narrator.current?.owner===owner)narrator.current=null},[]);
 const stopEffects=useCallback(()=>{for(const tone of tones.current){try{tone.stop()}catch{}}tones.current.clear()},[]);
 const unlock=useCallback(()=>{
  try {
   const Context=window.AudioContext||window.webkitAudioContext;
   if(!Context)return;
   context.current??=new Context();
   if(context.current.state!=='running')return context.current.resume().catch(()=>{});
  } catch {}
 },[]);
 const playEffect=useCallback(cue=>{
  if(!current.current.effects||!current.current.volume||document.hidden)return;
  const ready=unlock();
  function play(){
   const ctx=context.current;
   if(!ctx||ctx.state!=='running'||!current.current.effects||!current.current.volume||document.hidden)return;
   const achievement=cue==='achievement';
   const notes=achievement?[523.25,659.25,783.99,1046.5,1318.51,1567.98]:cue==='tap'?[698.46]:cue===true?[523.25,659.25,783.99]:[392,329.63];
   if(cue!=='tap')stopEffects();
   const length=achievement?.62:cue==='tap'?.095:.29;
   for(const [index,frequency] of notes.entries()){
    const oscillator=ctx.createOscillator();
    const gain=ctx.createGain();
    const start=ctx.currentTime+index*(achievement?.105:.092);
    oscillator.type='sine';
    oscillator.frequency.value=frequency;
    gain.gain.setValueAtTime(.0001,start);
    gain.gain.linearRampToValueAtTime(current.current.volume*(achievement?.10:cue==='tap'?.055:.14),start+.014);
    gain.gain.exponentialRampToValueAtTime(.0001,start+length);
    oscillator.connect(gain);
    gain.connect(ctx.destination);
    tones.current.add(oscillator);
    oscillator.onended=()=>{tones.current.delete(oscillator);oscillator.disconnect();gain.disconnect()};
    oscillator.start(start);
    oscillator.stop(start+length+.01);
   }
  }
  if(ready)ready.then(play).catch(()=>{});
  else play();
 },[unlock,stopEffects]);
 useEffect(()=>{
  const tap=event=>{
   if(!event.target.closest?.('button:not(:disabled), a[href]')||event.target.closest('.narration-player,.sound-settings'))return;
   if(document.querySelector('.narration-player[data-state="playing"]'))return;
   playEffect('tap');
  };
  document.addEventListener('click',tap,true);
  return()=>document.removeEventListener('click',tap,true);
 },[playEffect]);
 const update=useCallback(patch=>setSettings(previous=>({...previous,...patch})),[]);
 useEffect(()=>{try{localStorage.setItem('brightly-audio',JSON.stringify(settings))}catch{}if(!settings.effects||settings.volume===0)stopEffects()},[settings,stopEffects]);
 useEffect(()=>{const synth=window.speechSynthesis;if(!synth)return;const read=()=>setVoices(synth.getVoices());read();synth.addEventListener('voiceschanged',read);return()=>synth.removeEventListener('voiceschanged',read)},[]);
 useEffect(()=>()=>{stopNarration();stopEffects();context.current?.close().catch(()=>{})},[stopEffects,stopNarration]);
 return <AudioContextState.Provider value={{settings,update,voices,unlock,playEffect,claimNarration,releaseNarration,stopNarration}}>{children}</AudioContextState.Provider>
}
export const useAudio=()=>useContext(AudioContextState);

export function preferredVoice(voices,lang,chosen){
 const matching=voicesForLanguage(voices,lang);
 return matching.find(voice=>voice.voiceURI===chosen)||[...matching].sort((a,b)=>rank(b)-rank(a))[0];
}
function voicesForLanguage(voices,lang){
 return voices.filter(voice=>voice.lang.toLowerCase().replace('_','-').split('-')[0]===lang);
}
function rank(voice){return (/Samantha|Karen|Moira|Veena|Lekha|Swara|Aarohi|Google.*female/i.test(voice.name)?20:0)+(/Natural|Premium|Enhanced/i.test(voice.name)?10:0)+(voice.localService?2:0)}

export function AudioSettings({lang='en',narration}){
 const {settings,update,voices,unlock,playEffect}=useAudio(),w=audioWords[lang];
 const [open,setOpen]=useState(false),root=useRef(null),trigger=useRef(null);
 useEffect(()=>{if(!open)return;function outside(e){if(!root.current?.contains(e.target))setOpen(false)}function key(e){if(e.key==='Escape'){setOpen(false);trigger.current?.focus()}}document.addEventListener('pointerdown',outside);document.addEventListener('keydown',key);return()=>{document.removeEventListener('pointerdown',outside);document.removeEventListener('keydown',key)}},[open]);
 const matching=voicesForLanguage(voices,lang);
 return <div className="sound-settings" ref={root}><button ref={trigger} className="sound-toggle" aria-expanded={open} aria-controls="sound-panel" onClick={()=>{unlock();setOpen(!open)}}><span aria-hidden="true">{settings.effects?'♫':'♩'}</span><span>{w.settings}</span></button>{open&&<div id="sound-panel" className="sound-popover" role="group" aria-label={w.settings}>
  <div className="sound-heading"><strong>{w.settings}</strong><button aria-label={w.close} onClick={()=>{setOpen(false);trigger.current?.focus()}}>×</button></div>
  <label className="sound-checkbox"><input type="checkbox" checked={settings.effects} onChange={e=>{update({effects:e.target.checked});unlock()}}/>{w.sounds} · {settings.effects?w.on:w.off}</label>
  <label>{w.volume}<input type="range" min="0" max="1" step=".05" value={settings.volume} onChange={e=>update({volume:Number(e.target.value)})} onPointerUp={()=>playEffect(true)}/></label>
  <label>{w.pace}<select value={settings.rate} onChange={e=>update({rate:Number(e.target.value)})}><option value="0.75">{w.slow}</option><option value="0.88">{w.automatic.split(' · ')[0]}</option><option value="1">{w.normal}</option></select></label>
  <label>{w.source}<select value={settings.source} onChange={e=>update({source:e.target.value})}><option value="auto">{narration?.ai_available?w.auto:w.device}</option><option value="device">{w.device}</option></select></label>
  <label>{w.voice}<select value={settings.voices[lang]||''} onChange={e=>update({voices:{...settings.voices,[lang]:e.target.value}})}><option value="">{w.automatic}</option>{matching.map(v=><option key={v.voiceURI} value={v.voiceURI}>{v.name}</option>)}</select></label>
 </div>}</div>
}
