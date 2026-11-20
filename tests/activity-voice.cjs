const {chromium}=require(process.env.BRIGHTLY_PLAYWRIGHT||'@playwright/test');
const assert=require('node:assert/strict');
const path=require('node:path');

function fixture(){
 const count=44100*8,buffer=Buffer.alloc(44+count*2);
 buffer.write('RIFF');buffer.writeUInt32LE(36+count*2,4);buffer.write('WAVEfmt ',8);buffer.writeUInt32LE(16,16);buffer.writeUInt16LE(1,20);buffer.writeUInt16LE(1,22);buffer.writeUInt32LE(44100,24);buffer.writeUInt32LE(88200,28);buffer.writeUInt16LE(2,32);buffer.writeUInt16LE(16,34);buffer.write('data',36);buffer.writeUInt32LE(count*2,40);
 for(let i=0;i<count;i++)buffer.writeInt16LE(Math.round(Math.sin(i*2*Math.PI*440/44100)*300),44+i*2);
 return buffer;
}

(async()=>{
 const browser=await chromium.launch({headless:true,channel:'chrome'});
 const page=await browser.newPage({baseURL:process.env.BRIGHTLY_TEST_URL||'http://127.0.0.1:8877',viewport:{width:1360,height:950}});
 const errors=[],spoken=[];let checks=0;
 page.on('pageerror',error=>errors.push(error.message));
 page.on('request',request=>{
  if(request.url().endsWith('/api/narration'))spoken.push(request.postDataJSON());
  if(request.url().includes('/games/check')||request.url().includes('/lessons/please/complete'))checks++;
 });
 try{
  await page.addInitScript(()=>localStorage.setItem('brightly-language','en'));
  const signup=await page.request.post('/api/signup',{data:{name:'Language check',email:`activity${Date.now()}@example.com`,password:'TestingPassword123'}});
  const session=await signup.json();assert.equal(signup.status(),200);
  const created=await page.request.post('/api/children',{headers:{'x-csrf-token':session.csrf},data:{name:'Asha',language:'hi',age:5,avatar:'sun'}});
  const child=await created.json();assert.equal(created.status(),200);
  if(!process.env.BRIGHTLY_REAL_AUDIO){
   await page.route('**/api/content',async route=>{const response=await route.fetch();const catalog=await response.json();catalog.narration={ai_available:true,provider:'edge',singing_available:false};await route.fulfill({json:catalog})});
   const audio=fixture();await page.route('**/api/narration',route=>route.fulfill({contentType:'audio/wav',body:audio}));
  }
  await page.goto('/');await page.getByRole('button',{name:/Asha/}).click();
  const language=page.getByRole('combobox',{name:/Switch to English or Hindi/});
  assert.equal(await language.inputValue(),'hi');
  await page.getByRole('heading',{name:/नमस्ते, Asha/}).waitFor();
  await page.getByRole('button',{name:/पाठ देखें/}).click();
  await page.getByRole('button',{name:'ध्वनि और आवाज़',exact:false}).click();
  await page.getByLabel('आवाज़ का स्तर',{exact:false}).focus();await page.keyboard.press('Home');
  await page.keyboard.press('Escape');
  await page.getByRole('button',{name:/साथ सुनें/}).click();
  await page.getByText('आवाज़ का स्तर शून्य है। सुनने के लिए आवाज़ चालू करें।',{exact:true}).waitFor();
  await page.getByRole('button',{name:'आवाज़ चालू करें',exact:true}).click();
  await page.getByRole('button',{name:/साथ सुनें/}).click();
  await page.locator('.narrated-reading .narration-player[data-state=playing]').waitFor({timeout:85000});
  await page.getByRole('button',{name:/अब आपकी बारी/}).click();
  assert.equal(await page.locator('.narrated-reading').count(),0);
  await page.getByRole('button',{name:'सवाल और विकल्प सुनें',exact:true}).click();
  await page.locator('.listen-bar[data-state=playing]').waitFor({timeout:85000});
  assert.equal(spoken.at(-1).language,'hi');assert.equal(spoken.at(-1).part,'question');
  const questionPlayer=page.locator('.listen-bar');
  await page.getByRole('button',{name:'विकल्प सुनें 2',exact:true}).click();
  await page.locator('.listen-icon[data-state=playing]').waitFor({timeout:85000});
  assert.equal(await questionPlayer.getAttribute('data-state'),'idle');
  assert.equal(await page.locator('.answer-choice.chosen').count(),0);
  assert.equal(checks,0);assert.equal(spoken.at(-1).option,1);
  assert.equal(await page.locator('.narration-player[data-state=playing]').count(),1);
  await page.screenshot({path:path.join(__dirname,'../screenshots/hindi-lesson-audio.png'),fullPage:true});
  const saved=page.waitForResponse(response=>response.url().endsWith(`/children/${child.id}/language`)&&response.request().method()==='PUT');
  await language.selectOption('en');assert.equal((await saved).status(),200);
  await page.getByRole('heading',{name:'What can Mira say when she wants a turn?'}).waitFor();
  assert.equal(await page.locator('.narration-player[data-state=playing]').count(),0);
  await page.getByRole('button',{name:'Listen to choice 1',exact:true}).click();
  await page.locator('.listen-icon[data-state=playing]').waitFor({timeout:85000});
  assert.equal(spoken.at(-1).language,'en');
  await page.locator('.child-nav button').nth(2).click();
  assert.equal(await page.locator('.narration-player[data-state=playing]').count(),0);
  await page.getByRole('button',{name:/Choose the right thing/}).click();
  await page.getByRole('button',{name:'Listen to how to play',exact:true}).click();
  await page.locator('.listen-bar[data-state=playing]').waitFor({timeout:85000});
  assert.equal(spoken.at(-1).kind,'games');assert.equal(spoken.at(-1).part,'instructions');
  await page.getByRole('button',{name:'Listen to the question and choices',exact:true}).click();
  await page.locator('.listen-bar[data-state=playing]').waitFor({timeout:85000});
  assert.equal(await page.locator('.narration-player[data-state=playing]').count(),1);
  await language.selectOption('hi');
  await page.getByRole('heading',{name:'खाने से पहले क्या करें?'}).waitFor();
  await page.getByRole('button',{name:'विकल्प सुनें 1',exact:true}).click();
  await page.locator('.listen-icon[data-state=playing]').waitFor({timeout:85000});
  assert.equal(spoken.at(-1).language,'hi');assert.equal(checks,0);
  await page.setViewportSize({width:390,height:844});
  assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true);
  await page.screenshot({path:path.join(__dirname,'../screenshots/hindi-game-audio-mobile.png'),fullPage:true});
  await page.getByRole('button',{name:'आवाज़ रोककर ठहरें',exact:true}).click();
  await page.locator('.answers .answer-choice').first().click();
  await page.getByText('सही जवाब!',{exact:true}).waitFor();
  assert.equal(checks,1);
  await page.getByRole('button',{name:/अगला सवाल/}).click();
  await page.getByRole('button',{name:'सवाल और विकल्प सुनें',exact:true}).click();
  await page.locator('.listen-bar[data-state=playing]').waitFor({timeout:85000});
  assert.equal(spoken.at(-1).question,1);
  await language.selectOption('en');await language.selectOption('hi');await language.selectOption('en');
  await page.waitForFunction(()=>document.documentElement.lang==='en');
  for(let i=0;i<40;i++){
   const children=await (await page.request.get('/api/children')).json();
   if(children[0].language==='en')break;
   if(i===39)throw Error('Final language was not persisted');
   await page.waitForTimeout(100);
  }
  await page.setViewportSize({width:1360,height:950});
  await page.getByRole('button',{name:'Parent view',exact:true}).click();
  await page.getByRole('button',{name:'Edit',exact:true}).click();
  await page.getByLabel('Language',{exact:true}).selectOption('hi');
  await page.getByRole('button',{name:/Save changes/}).click();
  await page.getByRole('button',{name:'अभिभावक',exact:true}).waitFor();
  assert.equal(await language.inputValue(),'hi');
  await page.reload();await page.getByRole('button',{name:/Asha/}).click();
  assert.equal(await language.inputValue(),'hi');
  await page.getByRole('heading',{name:/नमस्ते, Asha/}).waitFor();
  const another=await page.request.post('/api/children',{headers:{'x-csrf-token':session.csrf},data:{name:'Theo',language:'en',age:5,avatar:'sun'}});
  assert.equal(another.status(),200);
  await page.reload();await page.getByRole('button',{name:/Theo/}).click();
  assert.equal(await language.inputValue(),'en');await page.getByRole('heading',{name:/Hello, Theo/}).waitFor();
  assert.equal((await page.request.get('/')).headers()['cache-control'],'no-store');
  assert.equal((await page.request.get('/assets/main.js')).headers()['cache-control'],'no-cache');
  assert.deepEqual(errors,[]);
  console.log(`PASS: child language overrides stale English preference; Hindi persists through refresh/profile edits; both languages narrate lesson/game questions and individual choices; listening never submits an answer; audio does not overlap; mobile layout; ${process.env.BRIGHTLY_REAL_AUDIO?'actual neural audio':'buffered audio fixture'}`);
 }catch(error){await page.screenshot({path:path.join(__dirname,'../screenshots/activity-test-failure.png'),fullPage:true});throw error}finally{await browser.close()}
})().catch(error=>{console.error(error);process.exit(1)});
