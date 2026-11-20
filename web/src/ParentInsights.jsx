import React from 'react';
import {ui} from './locale.jsx';

export default function ParentInsights({child,content,lang,t}){
  const weekAgo=Date.now()/1000-7*24*60*60;
  const week=child.completions.filter(item=>item.completed_at>=weekAgo).length;
  const categories=Object.entries(child.completed.reduce((counts,id)=>{
    const category=content?.lessons.find(lesson=>lesson.id===id)?.category;
    if(category)counts[category]=(counts[category]||0)+1;
    return counts;
  },{})).sort((a,b)=>b[1]-a[1]);
  const recent=child.completions.slice(0,3).map(item=>content?.lessons.find(lesson=>lesson.id===item.lesson_id)?.title?.[lang]||item.lesson_id);
  const gameAverage=child.games.length?(child.games.reduce((total,game)=>total+game.score,0)/child.games.length).toFixed(1):'—';
  return <div className="parent-insights">
    <div><strong>{ui(lang,'This week')}</strong><span>{lang==='hi'?`${week} पाठ पूरे`:`${week} lesson${week===1?'':'s'} completed`}</span></div>
    <div><strong>{ui(lang,'Game average')}</strong><span>{gameAverage}{child.games.length?' / 3':''}</span></div>
    <div><strong>{ui(lang,'Growing in')}</strong><span>{t[categories[0]?.[0]]||ui(lang,'New adventures ahead')}</span></div>
    <div className="parent-recent"><strong>{ui(lang,'Recently learned')}</strong><span>{recent.length?recent.join(' · '):ui(lang,'Their first lesson is waiting.')}</span></div>
  </div>
}
