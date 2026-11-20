const {chromium}=require(process.env.BRIGHTLY_PLAYWRIGHT||'@playwright/test');
const assert=require('node:assert/strict');
const path=require('node:path');

(async()=>{
 const browser=await chromium.launch({headless:true,channel:'chrome'});
 const page=await browser.newPage({baseURL:process.env.BRIGHTLY_TEST_URL||'http://127.0.0.1:8878',viewport:{width:1440,height:1000}});
 const errors=[];
 page.on('pageerror',error=>errors.push(error.message));
 try{
  const response=await page.request.post('/api/signup',{data:{name:'Narration check',email:`narration${Date.now()}@example.com`,password:'TestingPassword123'}});
  const account=await response.json();
  assert.equal(response.status(),200);
  const create=await page.request.post('/api/children',{data:{name:'Neural reader',age:6,language:'en',avatar:'sun'},headers:{'x-csrf-token':account.csrf}});
  assert.equal(create.status(),200);
  await page.goto('/');
  await page.getByRole('button',{name:/Neural reader/}).click();
  await page.locator('.child-nav button').nth(3).click();
  await page.getByRole('button',{name:/The Lion and the Mouse/}).click();
  const requests=[];
  page.on('request',request=>{if(request.url().endsWith('/api/narration'))requests.push(request.postDataJSON())});
  await page.getByRole('button',{name:/Listen together/}).click();
  await page.waitForFunction(()=>document.querySelector('.audio-position input')?.valueAsNumber>.4);
  const duration=Number(await page.locator('.audio-position input').getAttribute('max'));
  assert(duration>45);
  await page.getByRole('button',{name:/Pause/}).click();
  const paused=await page.locator('.audio-position input').inputValue();
  await page.waitForTimeout(150);
  assert.equal(await page.locator('.audio-position input').inputValue(),paused);
  await page.getByRole('button',{name:/Resume/}).click();
  await page.waitForFunction(before=>document.querySelector('.audio-position input')?.valueAsNumber>Number(before)+.2,paused);
  assert.equal(requests.length,1);
  await page.screenshot({path:path.join(__dirname,'../screenshots/neural-story-en.png'),fullPage:true,animations:'disabled'});
  await page.getByRole('combobox',{name:/Switch to English or Hindi/}).selectOption('hi');
  await page.getByRole('button',{name:/साथ सुनें/}).click();
  await page.waitForFunction(()=>document.querySelector('.audio-position input')?.valueAsNumber>.4);
  assert.equal(requests.length,2);
  assert.equal(requests[1].language,'hi');
  assert(Number(await page.locator('.audio-position input').getAttribute('max'))>45);
  await page.getByRole('button',{name:/विराम/}).click();
  await page.screenshot({path:path.join(__dirname,'../screenshots/neural-story-hi.png'),fullPage:true,animations:'disabled'});
  assert.deepEqual(errors,[]);
  console.log('PASS: actual bundled English/Hindi neural audio through authenticated API, continuous playback, pause/resume, language switch, and no browser errors');
 }finally{await browser.close()}
})().catch(error=>{console.error(error);process.exit(1)});
