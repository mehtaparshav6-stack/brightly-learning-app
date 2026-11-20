import React,{useState} from 'react';
import {api} from './api';
import {ui} from './locale.jsx';

export default function Auth({lang,mode,onSwitch,onDone,onError}){
  const tr=text=>ui(lang,text);
  const [form,setForm]=useState({name:'',email:'',password:'',confirm:'',recovery_code:''});
  const [show,setShow]=useState(false);
  const [busy,setBusy]=useState(false);
  const [recovery,setRecovery]=useState(null);
  async function submit(event){
    event.preventDefault();
    if(mode==='signup'&&form.password!==form.confirm){onError(tr('Passwords do not match.'));return}
    setBusy(true);
    try{
      if(mode==='forgot'){
        const data=await api('/reset-password','POST',{email:form.email,recovery_code:form.recovery_code,new_password:form.password});
        setRecovery({code:data.recovery_code,reset:true});
      }else{
        const data=await api(mode==='signup'?'/signup':'/login','POST',form);
        if(data.recovery_code)setRecovery({code:data.recovery_code,session:data});
        else await onDone(data);
      }
    }catch(error){onError(error)}finally{setBusy(false)}
  }
  function continueAfterRecovery(){const data=recovery?.session;setRecovery(null);if(data)onDone(data);else onSwitch('login')}
  return <main className="auth-layout">
    <div className="auth-poster"><span>✦ {tr('YOUR FAMILY’S LITTLE CORNER OF WONDER')}</span><div className="auth-art">✿<small>☀</small></div><h2>{tr('Every bright beginning starts somewhere.')}</h2></div>
    {recovery?<div className="auth-form recovery-panel"><span className="section-eyebrow">{tr('KEEP THIS SOMEWHERE SAFE')}</span><h1>{tr('Your recovery code.')}</h1><p>{tr('Save this code now. It is shown only once and lets you reset your password without sharing your child’s data with an email service.')}</p><output>{recovery.code}</output><button className="button button-dark auth-submit" onClick={continueAfterRecovery}>{tr('I’ve saved my code')} <span>↗</span></button></div>:
    <form className="auth-form" onSubmit={submit}><span className="section-eyebrow">{tr('PARENTS & GUARDIANS')}</span><h1>{mode==='signup'?tr('Begin their bright journey.'):mode==='forgot'?tr('Find your way back.'):tr('Welcome back to the garden.')}</h1><p>{mode==='signup'?tr('Create a private family space and let the little adventures begin.'):mode==='forgot'?tr('Use the recovery code shown when your account was created.'):tr('Pick up right where their curiosity left off.')}</p>
      {mode==='signup'&&<label>{tr('Your name')}<input required minLength="2" maxLength="80" autoComplete="name" value={form.name} onChange={e=>setForm({...form,name:e.target.value})}/></label>}
      <label>{tr('Email address')}<input required type="email" autoComplete="email" value={form.email} onChange={e=>setForm({...form,email:e.target.value})}/></label>
      {mode==='forgot'&&<label>{tr('Recovery code')}<input required autoComplete="off" value={form.recovery_code} onChange={e=>setForm({...form,recovery_code:e.target.value})}/></label>}
      <label htmlFor="brightly-password">{mode==='forgot'?tr('New password'):tr('Password')}</label><div className="password-field"><input id="brightly-password" required minLength={mode==='login'?undefined:8} type={show?'text':'password'} autoComplete={mode==='login'?'current-password':'new-password'} value={form.password} onChange={e=>setForm({...form,password:e.target.value})}/><button type="button" onClick={()=>setShow(!show)} aria-label={show?tr('Hide password'):tr('Show password')}>{show?tr('Hide'):tr('Show')}</button></div>
      {mode==='signup'&&<label>{tr('Confirm password')}<input required type="password" autoComplete="new-password" value={form.confirm} onChange={e=>setForm({...form,confirm:e.target.value})}/></label>}
      <button className="button button-dark auth-submit" disabled={busy}>{busy?tr('One moment…'):mode==='signup'?tr('Create my account'):mode==='forgot'?tr('Reset password'):tr('Sign in')} <span>↗</span></button>
      {mode==='login'&&<button className="auth-forgot" type="button" onClick={()=>onSwitch('forgot')}>{tr('Forgot password?')}</button>}
      <p className="auth-switch">{mode==='signup'?tr('Already have an account?'):mode==='forgot'?tr('Remember your password?'):tr('New to Brightly?')} <button type="button" onClick={()=>onSwitch(mode==='signup'||mode==='forgot'?'login':'signup')}>{mode==='signup'||mode==='forgot'?tr('Sign in'):tr('Create an account')}</button></p>
    </form>}
  </main>
}
