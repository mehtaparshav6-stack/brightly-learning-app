import React,{useEffect,useRef,useState} from 'react';
import NarrationPlayer from './NarrationPlayer.jsx';
import OriginalPerformance from './OriginalPerformance.jsx';
import {api} from './api';
import {earnedSince} from './AchievementFeedback.jsx';

const copy={
 en:{stories:'The story room',verses:'Poems, rhymes & songs',title:'Once upon a time…',verseTitle:'Words to remember. Songs to love.',intro:'Complete moral stories to read aloud, wonder about, and return to.',verseIntro:'Familiar English and Hindi favourites, credited poems, and original performances.',all:'All',search:'Find a story, poem, or song',read:'Read the story',open:'Open',back:'Back to the library',moral:'The moral of the story',talk:'Talk about it together',next:'Next story',nextVerse:'Next reading',done:'We finished this together',saved:'Finished together',saving:'Saving your reading…',minutes:'min read',storiesCount:'stories',readingsCount:'readings',collection:'Collection',poems:'Poems',rhymes:'Rhymes',performances:'Watch & listen',empty:'No matches yet. Try a different title or collection.',play:'Play the original performance',closeVideo:'Close player',external:'This performance plays through YouTube. Availability, advertisements, and related videos are controlled by YouTube.',onYoutube:'Open on YouTube',original:'Original text',translation:'Brightly translation',retelling:'A complete Brightly retelling',source:'Source & credits',by:'By',mr:'This reading is available in English and Hindi. Showing English.',english:'English classics',hindi:'Hindi classics'},
 hi:{stories:'कहानियों का कमरा',verses:'कविताएँ, बाल गीत और गाने',title:'एक समय की बात है…',verseTitle:'याद रहने वाले शब्द। प्यारे गीत।',intro:'पूरी नैतिक कहानियाँ पढ़ें, सुनें और उनके बारे में साथ सोचें।',verseIntro:'हिन्दी और अंग्रेज़ी की परिचित रचनाएँ, कवियों के नाम और असली प्रस्तुतियाँ।',all:'सभी',search:'कहानी, कविता या गीत खोजें',read:'कहानी पढ़ें',open:'खोलें',back:'पुस्तकालय में लौटें',moral:'कहानी की सीख',talk:'साथ बात करें',next:'अगली कहानी',nextVerse:'अगली रचना',done:'हमने इसे साथ पूरा किया',saved:'साथ पूरा किया',saving:'पढ़ना सहेज रहे हैं…',minutes:'मिनट की कहानी',storiesCount:'कहानियाँ',readingsCount:'रचनाएँ',collection:'संग्रह',poems:'कविताएँ',rhymes:'बाल गीत',performances:'देखें और सुनें',empty:'कुछ नहीं मिला। दूसरा नाम या संग्रह चुनें।',play:'असली प्रस्तुति चलाएँ',closeVideo:'प्लेयर बंद करें',external:'यह प्रस्तुति YouTube से चलती है। उपलब्धता, विज्ञापन और सुझाए गए वीडियो YouTube के नियंत्रण में हैं।',onYoutube:'YouTube पर खोलें',original:'मूल रचना',translation:'Brightly का अनुवाद',retelling:'Brightly का पूरा पुनर्कथन',source:'स्रोत और रचनाकार',by:'रचनाकार',mr:'यह रचना हिन्दी और अंग्रेज़ी में उपलब्ध है।',english:'अंग्रेज़ी की प्रसिद्ध रचनाएँ',hindi:'हिन्दी की प्रसिद्ध रचनाएँ'}
};
const collections={
 en:{aesop:'Aesop’s fables',panchatantra:'Panchatantra',birbal:'Akbar & Birbal',folktale:'Traditional tales'},
 hi:{aesop:'ईसप की कहानियाँ',panchatantra:'पंचतंत्र',birbal:'अकबर और बीरबल',folktale:'लोककथाएँ'}
};

export default function Library({items,kind,lang,narration,child,onRefresh,onError,onBadges}){
 const [open,setOpen]=useState(null);
 const [query,setQuery]=useState('');
 const [filter,setFilter]=useState('all');

 const [busy,setBusy]=useState(false);
 const [savedHere,setSavedHere]=useState([]);
 const heading=useRef(null),live=useRef(true);
 const readingLang=lang==='hi'?'hi':'en',w=copy[readingLang];
 const isStory=kind==='stories';
 useEffect(()=>{live.current=true;return()=>{live.current=false}},[]);
 const filtered=items.filter(item=>{
  const typeMatch=filter==='all'||(isStory?item.collection===filter:
    filter==='performances'?!!item.youtube_id:
    filter==='poems'?item.format==='poem':
    filter==='rhymes'?!item.format:
    item.original_language===(filter==='english'?'en':'hi'));
  const searchable=[item.title[readingLang],item.title.en,item.title.hi,item.author,item.collection].filter(Boolean).join(' ').toLocaleLowerCase();
  return typeMatch&&searchable.includes(query.trim().toLocaleLowerCase());
 });
 const item=items.find(item=>item.id===open);
 const index=items.findIndex(item=>item.id===open);
 const itemLanguage=item?.youtube_id?item.original_language:readingLang;
 const readingKind=item?.youtube_id?'performances':item?.format==='poem'?'poems':kind;
 const done=item&&(savedHere.includes(item.id+itemLanguage+child.journey?.day)||(child.journey?.reading_keys||[]).includes(`${readingKind}:${item.id}:${itemLanguage}`));
 const minutes=reading=>Math.max(1,Math.ceil(reading.text?.[readingLang]?.split(/\s+/).length/100||1));
 function select(id){
  setOpen(id);
  requestAnimationFrame(()=>{
   heading.current?.focus({preventScroll:true});
   heading.current?.scrollIntoView({block:'start',behavior:window.matchMedia('(prefers-reduced-motion: reduce)').matches?'instant':'smooth'});
  });
 }
 async function finished(){
  if(busy||done)return;
  setBusy(true);
  try{
   const summary=await api(`/children/${child.id}/readings`,'POST',{kind:readingKind,item_id:item.id,language:itemLanguage});
   if(!live.current)return;
   setSavedHere(previous=>[...previous,item.id+itemLanguage+child.journey?.day]);
   onBadges(earnedSince(child,summary));await onRefresh();
  }catch(error){if(live.current)onError(error)}
  finally{if(live.current)setBusy(false)}
 }
 const filters=isStory?['all','aesop','panchatantra','birbal','folktale']:['all','english','hindi','poems','rhymes','performances'];
 return <main className={'workspace reading-room '+(isStory?'moral-library':'verse-library')}>
  {lang==='mr'&&<p className="library-language-note">या वाचनासाठी इंग्रजी आवृत्ती दाखवत आहोत. हिन्दी किंवा English निवडू शकता.</p>}
  {item?<>
   <button className="back-link" onClick={()=>select(null)}>← {w.back}</button>
   <article className="open-book">
    <header className="book-title-page">
     <span className="section-eyebrow">{isStory?collections[readingLang][item.collection]:item.youtube_id?w.performances:item.format==='poem'?w.poems:w.rhymes}</span>
     <span className="reading-emblem" aria-hidden="true">{item.icon}</span>
     <h1 ref={heading} tabIndex={-1}>{item.title[readingLang]}</h1>
     {isStory?<p>{minutes(item)} {w.minutes} · English / हिन्दी</p>:<p>{item.author?`${w.by} ${item.author}`:item.channel||w.rhymes}</p>}
     {item.author&&<small>{item.original_language===readingLang?w.original:w.translation}</small>}
     <div className="book-spine" aria-hidden="true">✦</div>
    </header>
    <div className="book-pages">
     {!isStory?<><OriginalPerformance key={item.id+readingLang} recording={item.recording||item} title={item.title[readingLang]} lang={readingLang} label={item.youtube_id?w.play:undefined}/>{!item.youtube_id&&<div className="read-along verse-reading" aria-label={item.title[readingLang]}>{item.lines[readingLang].map((line,index)=><React.Fragment key={index}>{line}<br/></React.Fragment>)}</div>}</>:<NarrationPlayer key={readingKind+item.id+readingLang} kind={readingKind} item={item} lang={readingLang} narration={narration}/>}

     {item.moral&&<section className="story-moral"><span aria-hidden="true">✦</span><div><h2>{w.moral}</h2><p>{item.moral[readingLang]}</p></div></section>}
     {item.talk&&<aside className="practice-card"><strong>{w.talk}</strong><p>{item.talk[readingLang]}</p></aside>}
     <div className="reading-finish"><button className="button button-dark" disabled={done||busy} onClick={finished}>{busy?w.saving:done?'✓ '+w.saved:w.done+' ✦'}</button></div>
     <details className="reading-credits"><summary>{w.source}</summary><p>{item.credit?.[readingLang]||item.author||item.channel||w.retelling}</p>{item.source_url&&<a href={item.source_url} target="_blank" rel="noreferrer">{w.source} ↗</a>}</details>
     <div className="reading-navigation">{index<items.length-1&&<button className="button button-outline" onClick={()=>select(items[index+1].id)}>{isStory?w.next:w.nextVerse} ↗</button>}<button className="back-link" onClick={()=>select(null)}>{w.back}</button></div>
    </div>
   </article>
  </>:<>
   <header className="reading-room-header"><div><span className="section-eyebrow">{isStory?w.stories:w.verses}</span><h1 ref={heading} tabIndex={-1}>{isStory?w.title:w.verseTitle}</h1><p>{isStory?w.intro:w.verseIntro}</p></div><div className="library-count"><strong>{items.length}</strong><span>{isStory?w.storiesCount:w.readingsCount}</span><i aria-hidden="true">{isStory?'📖':'♫'}</i></div></header>
   <div className="library-tools"><label className="library-search">{w.search}<input type="search" value={query} onChange={event=>setQuery(event.target.value)}/></label><div className="library-filters" role="group" aria-label={w.collection}>{filters.map(value=><button key={value} aria-pressed={filter===value} onClick={()=>setFilter(value)}>{collections[readingLang][value]||w[value]}</button>)}</div></div>
   {!filtered.length&&<p role="status">{w.empty}</p>}
   <div className="reading-catalog">{filtered.map((reading,index)=><button className={'reading-cover '+['mint','lilac','peach','blue','yellow'][index%5]} key={reading.id} onClick={()=>select(reading.id)}>
    <span className="cover-emblem" aria-hidden="true">{reading.icon}</span><div><small>{isStory?collections[readingLang][reading.collection]:reading.youtube_id?w.performances:reading.author||w.rhymes}</small><strong>{reading.title[readingLang]}</strong>{isStory&&<p>{reading.moral[readingLang]}</p>}</div><span className="cover-bottom">{isStory?`${minutes(reading)} ${w.minutes}`:reading.youtube_id?reading.original_language.toUpperCase():w.open}<b aria-hidden="true">↗</b></span>
   </button>)}</div>
  </>}
 </main>;
}
