let csrf = '';
const timeZone=()=>{try{return Intl.DateTimeFormat().resolvedOptions().timeZone||'UTC'}catch{return 'UTC'}};
export const setCsrf = value => { csrf = value || ''; };
export async function narrationAudio(body,signal) {
  const response=await fetch('/api/narration',{method:'POST',credentials:'same-origin',signal,headers:{'Content-Type':'application/json','x-csrf-token':csrf},body:JSON.stringify(body)});
  if(!response.ok)throw new Error('Narration unavailable');
  if(!response.headers.get('Content-Type')?.startsWith('audio/'))throw new Error('Invalid audio');
  return response.blob();
}
export async function api(path, method='GET', body) {
  const response = await fetch('/api'+path, {method, credentials:'same-origin', headers:{'x-time-zone':timeZone(),...(body?{'Content-Type':'application/json'}:{}),...(method!=='GET'?{'x-csrf-token':csrf}:{})},body:body?JSON.stringify(body):undefined});
  const data = await response.json().catch(()=>({detail:'Something went wrong. Please try again.'}));
  if(!response.ok) throw new Error(typeof data.detail==='string'?data.detail:'Something went wrong. Please try again.');
  return data;
}
