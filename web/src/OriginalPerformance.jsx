import React,{useEffect,useRef,useState} from 'react';
import {useAudio} from './Audio.jsx';

const copy={
 en:{listen:'Listen to the original recording',close:'Close player',loading:'Opening the recording…',source:'Original recording',song:'Recorded song',recitation:'Recorded recitation',note:'Plays through the creator’s YouTube player. Internet is required. YouTube controls availability, advertisements, and related videos.',fallback:'Open the original on YouTube',hint:'If it does not start automatically, press Play inside the recording.',language:'Recording language',translation:'The text below is a Brightly translation; the recording keeps the original language.'},
 hi:{listen:'असली रिकॉर्डिंग सुनें',close:'प्लेयर बंद करें',loading:'रिकॉर्डिंग खुल रही है…',source:'असली रिकॉर्डिंग',song:'रिकॉर्ड किया हुआ गीत',recitation:'रिकॉर्ड किया हुआ काव्य पाठ',note:'रचनाकार के YouTube प्लेयर से चलता है। इंटरनेट चाहिए। उपलब्धता, विज्ञापन और सुझाए गए वीडियो YouTube के नियंत्रण में हैं।',fallback:'असली रिकॉर्डिंग YouTube पर खोलें',hint:'अपने आप शुरू न हो तो रिकॉर्डिंग के अंदर Play दबाएँ।',language:'रिकॉर्डिंग की भाषा',translation:'नीचे Brightly का अनुवाद है। रिकॉर्डिंग मूल भाषा में रहती है।'},
 mr:{listen:'मूळ रेकॉर्डिंग ऐका',close:'प्लेअर बंद करा',loading:'रेकॉर्डिंग उघडत आहे…',source:'मूळ रेकॉर्डिंग',song:'रेकॉर्ड केलेले गाणे',recitation:'रेकॉर्ड केलेले काव्यवाचन',note:'निर्मात्याच्या YouTube प्लेअरमधून चालते. इंटरनेट आवश्यक आहे. उपलब्धता, जाहिराती आणि संबंधित व्हिडिओ YouTube ठरवते.',fallback:'मूळ रेकॉर्डिंग YouTube वर उघडा',hint:'आपोआप सुरू झाले नाही तर रेकॉर्डिंगमधील Play दाबा.',language:'रेकॉर्डिंगची भाषा',translation:'खाली Brightly चा अनुवाद आहे. रेकॉर्डिंग मूळ भाषेत राहते.'}
};

export default function OriginalPerformance({recording,title,lang,label}){
 const [open,setOpen]=useState(false),[loading,setLoading]=useState(false);
 const {claimNarration,releaseNarration}=useAudio();
 const owner=useRef(Symbol('original-performance'));
 const w=copy[lang],language=recording.language||recording.original_language||'en';
 const stop=()=>{setOpen(false);setLoading(false);releaseNarration(owner.current)};
 useEffect(()=>{stop();return()=>releaseNarration(owner.current)},[recording.youtube_id,lang]);
 function play(){claimNarration(owner.current,stop);setLoading(true);setOpen(true)}
 const query=new URLSearchParams({autoplay:'1',rel:'0',playsinline:'1'});
 if(recording.start)query.set('start',recording.start);
 if(recording.end)query.set('end',recording.end);
 return <section className="original-performance" aria-label={w.source}>
  <div className="original-performance-heading"><span aria-hidden="true">♫</span><div><strong>{recording.style==='recitation'?w.recitation:w.song}</strong><p>{recording.channel}</p><small>{w.language}: {({en:'English',hi:'हिन्दी',mr:'मराठी'})[language]}</small></div></div>
  {open?<><div className="video-frame"><iframe title={title} src={`https://www.youtube-nocookie.com/embed/${recording.youtube_id}?${query}`} allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowFullScreen referrerPolicy="strict-origin-when-cross-origin" onLoad={()=>setLoading(false)}/></div>{loading&&<p role="status">{w.loading}</p>}<p className="recording-hint">{w.hint}</p><button className="button button-outline" onClick={stop}>{w.close}</button></>:<button className="button button-dark original-listen" onClick={play}><span aria-hidden="true">▶</span>{label||w.listen}</button>}
  {language!==lang&&<p className="recording-language-note">{w.translation}</p>}
  <p className="story-footnote">{w.note}</p><a className="source-link" href={recording.source_url} target="_blank" rel="noreferrer">{w.fallback} ↗</a>
 </section>;
}
