const path=require('node:path');
const {chromium}=require(process.env.BRIGHTLY_PLAYWRIGHT||'@playwright/test');
(async()=>{
 const browser=await chromium.launch({channel:'chrome',headless:true});
 const page=await browser.newPage({baseURL:process.env.BRIGHTLY_TEST_URL||'http://127.0.0.1:8878',viewport:{width:1440,height:1000}});
 const result=[];
 try{
  const account=await (await page.request.post('/api/signup',{data:{name:'Recording Check',email:`recordings${Date.now()}@example.com`,password:'TestingPassword123'}})).json();
  await page.request.post('/api/children',{headers:{'x-csrf-token':account.csrf},data:{name:'Recording listener',age:5,language:'en',avatar:'sun'}});
  await page.goto('/');await page.getByRole('button',{name:/Recording listener/}).click();
  for(const item of [{title:/Twinkle, twinkle, little star/,lang:'en'},{title:/उठो लाल अब आँखें खोलो/,lang:'hi'}]){
   await page.getByRole('combobox',{name:/Switch to English or Hindi/}).selectOption(item.lang);
   await page.locator('.child-nav button').nth(4).click();
   if(await page.getByRole('button',{name:/Back to the library|पुस्तकालय में लौटें/}).count())await page.getByRole('button',{name:/Back to the library|पुस्तकालय में लौटें/}).first().click();
   await page.getByRole('button',{name:item.title}).click();
   await page.getByRole('button',{name:/Listen to the original recording|असली रिकॉर्डिंग सुनें/,exact:true}).click();
   const frameElement=await page.locator('.original-performance iframe').elementHandle();
   const frame=await frameElement.contentFrame();
   let observation={};
   for(let attempt=0;attempt<12;attempt++){
    await page.waitForTimeout(1000);
    observation=await frame.evaluate(()=>{const video=document.querySelector('video');return {text:document.body.innerText.slice(0,350),time:video?.currentTime||0,paused:video?.paused,readyState:video?.readyState}}).catch(()=>({text:'Frame is loading'}));
    if(observation.time>.5||/unavailable|sign in|not a bot|configuration error|error occurred/i.test(observation.text))break;
    if(observation.paused){const play=frame.locator('.ytp-large-play-button');if(await play.isVisible().catch(()=>false))await play.click().catch(()=>{})}
   }
   result.push({language:item.lang,...observation});
   await page.screenshot({path:path.join(__dirname,'../screenshots/'+(item.lang==='en'?'english-original-rhyme.png':'hindi-original-poem.png')),fullPage:true,animations:'disabled'});
  }
 }finally{await browser.close()}
 if(result.length!==2||result.some(item=>item.time<=.5||item.paused))throw new Error('An original recording did not start: '+JSON.stringify(result));
 console.log('PASS: actual creator-hosted English and Hindi recordings play in Chrome');
})().catch(error=>{console.error(error);process.exit(1)});
