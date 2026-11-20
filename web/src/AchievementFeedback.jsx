import React,{useEffect,useRef,useState} from 'react';
import {useAudio} from './Audio.jsx';

const copy={
 en:{right:'Great thinking!',wrong:'Give it another go',badge:'New badge!'},
 hi:{right:'बहुत बढ़िया!',wrong:'फिर कोशिश करो',badge:'नया बैज!'},
 mr:{right:'खूप छान!',wrong:'पुन्हा प्रयत्न करा',badge:'नवा बॅज!'}
};

export function AnswerPop({correct,lang}){
 const [visible,setVisible]=useState(true);
 useEffect(()=>{const timer=setTimeout(()=>setVisible(false),1800);return()=>clearTimeout(timer)},[]);
 if(!visible)return null;
 return <span className={'answer-pop '+(correct?'success':'gentle')} aria-hidden="true"><b>{correct?'✦':'↻'}</b> {copy[lang][correct?'right':'wrong']}</span>;
}

export function earnedSince(before,after){
 const existing=new Set(before.badges.filter(badge=>badge.earned).map(badge=>badge.id));
 return after.badges.filter(badge=>badge.earned&&!existing.has(badge.id));
}

export function BadgeAnnouncement({badges,lang,onDismiss}){
 const dialog=useRef(null);
 const {playEffect}=useAudio();
 const open=badges.length>0;
 useEffect(()=>{
  if(!open)return;
  const previous=document.activeElement;
  dialog.current?.showModal();
  playEffect('achievement');
  return()=>{dialog.current?.close();if(previous?.isConnected)previous.focus({preventScroll:true})};
 },[open,playEffect]);
 const words={en:{title:'Look what you’ve earned!',intro:'Your practice made this happen. What a lovely step forward!',button:'Keep growing'},hi:{title:'देखो, तुमने क्या पाया!',intro:'तुम्हारे अभ्यास से यह हुआ। बहुत प्यारा कदम आगे बढ़ाया!',button:'आगे सीखें'},mr:{title:'पाहा, तुम्हाला काय मिळाले!',intro:'तुमच्या सरावाने हे जमले. खूप छान पाऊल पुढे!',button:'पुढे शिकूया'}}[lang];
 return <dialog ref={dialog} className="badge-celebration" aria-labelledby="badge-title" onCancel={event=>{event.preventDefault();onDismiss()}}>
  <div className="badge-sparkles" aria-hidden="true">✦ · ✧ · ✦</div>
  <h2 id="badge-title">{words.title}</h2><p>{words.intro}</p>
  <div className="celebration-badges">{badges.map(badge=><article key={badge.id}><span aria-hidden="true">{badge.icon}</span><strong>{badge.title[lang]}</strong><small>{badge.goal[lang]}</small><span className="badge-seeds">✺ +15 {({en:'Sunseeds',hi:'धूप बीज',mr:'सूर्यबिया'})[lang]}</span></article>)}</div>
  <button className="button button-dark" onClick={onDismiss}>{words.button} ↗</button>
 </dialog>;
}
