"""Progressive question banks. Answers remain server-side."""
import json
from pathlib import Path


def tr(en, hi, mr):
    return dict(en=en, hi=hi, mr=mr)


def question(prompt, options, answer, explanation):
    return dict(prompt=prompt, options=options, answer=answer, explanation=explanation)


def bank(rows, **extra):
    return dict(questions={lang:[[row['prompt'][lang],row['options'][lang]] for row in rows] for lang in ('en','hi','mr')},
                answers=[row['answer'] for row in rows],
                explanations={lang:[row['explanation'][lang] for row in rows] for lang in ('en','hi','mr')}, **extra)


def q(en, hi, mr, choices, answer, exp_en, exp_hi, exp_mr):
    return question(tr(en,hi,mr),tr(*choices),answer,tr(exp_en,exp_hi,exp_mr))


BASE = json.loads((Path(__file__).parent/'games.json').read_text())
LEVELS = {key:{1:value} for key,value in BASE.items()}

# Scenario rounds ask children to combine what they learned with a new situation.
SCENARIOS = [
 q('A friend is still using the toy you want. What helps both of you?', 'दोस्त अभी खिलौने से खेल रहा है। दोनों के लिए क्या अच्छा है?', 'मित्र अजून खेळणे वापरतोय. दोघांसाठी काय चांगले?',
 (['Grab it','Ask for a turn when they finish','Hide the toy'],['छीन लें','पूरा होने पर अपनी बारी माँगें','खिलौना छिपाएँ'],['हिसकावा','झाल्यावर पाळी मागा','खेळणे लपवा']),1,'Ask and listen. Both children can have a turn.','पूछें और सुनें। दोनों को बारी मिल सकती है।','विचारा आणि ऐका. दोघांना पाळी मिळू शकते.'),
 q('You spill a little water. What can you do?', 'थोड़ा पानी गिर गया। क्या करें?', 'थोडे पाणी सांडले. काय कराल?',
 (['Tell a grown-up and help wipe it safely','Leave a slippery floor','Blame a friend'],['बड़े को बताकर सुरक्षित ढंग से पोंछें','फ़र्श गीला छोड़ दें','दोस्त को दोष दें'],['मोठ्यांना सांगून सुरक्षितपणे पुसा','ओलेच सोडा','मित्राला दोष द्या']),0,'Ask for help and make the floor safe together.','मदद माँगकर फ़र्श सुरक्षित करें।','मदत मागून जमीन सुरक्षित करा.'),
 q('A game feels too loud for your friend. What could you try?', 'दोस्त को खेल की आवाज़ तेज़ लगती है। क्या करें?', 'मित्राला खेळाचा आवाज मोठा वाटतो. काय कराल?',
 (['Shout louder','Tell them to go away','Ask if a quieter game would help'],['और चिल्लाएँ','उसे जाने को कहें','पूछें क्या शांत खेल अच्छा रहेगा'],['अजून ओरडा','निघून जा म्हणा','शांत खेळ चालेल का विचारा']),2,'Listen to what a friend needs and look for a way to include them.','दोस्त की ज़रूरत सुनें और साथ खेलने का तरीका ढूँढ़ें।','मित्राची गरज ऐका आणि सहभागी होण्याची वाट शोधा.'),
 q('Someone says no to a hug. What is caring?', 'कोई गले मिलने से मना करे तो क्या करें?', 'कोणी मिठी नको म्हणाले तर काय कराल?',
 (['Respect their no and offer a wave','Hug them anyway','Keep asking until they say yes'],['मना करने का सम्मान करके हाथ हिलाएँ','फिर भी गले लगें','हाँ कहने तक पूछते रहें'],['नकार मान्य करून हात हलवा','तरीही मिठी मारा','हो म्हणेपर्यंत विचारा']),0,'People choose what feels comfortable for their bodies.','हर कोई अपने शरीर के लिए आरामदायक तरीका चुन सकता है।','प्रत्येकाला शरीरासाठी सोयीची कृती निवडता येते.'),
 q('Your drawing tears and you feel upset. What is a helpful first step?', 'चित्र फट गया और दुख हुआ। पहला अच्छा कदम क्या है?', 'चित्र फाटले आणि वाईट वाटले. आधी काय कराल?',
 (['Throw things at a friend','Pause, name the feeling, and ask for help','Say you must never draw again'],['दोस्त पर चीज़ें फेंकें','रुकें, भावना बताएँ और मदद माँगें','फिर कभी चित्र न बनाने को कहें'],['मित्रावर वस्तू फेका','थांबा, भावना सांगा आणि मदत मागा','पुन्हा चित्र काढू नये म्हणा']),1,'All feelings are allowed. A pause helps us choose a safe action.','हर भावना ठीक है। रुकने से सुरक्षित कदम चुन पाते हैं।','सर्व भावना मान्य आहेत. थांबल्याने सुरक्षित कृती निवडता येते.'),
 q('Two friends have different ideas for a tower. What helps?', 'दोस्तों के मीनार बनाने के अलग विचार हैं। क्या करें?', 'मनोऱ्यासाठी मित्रांच्या कल्पना वेगळ्या आहेत. काय कराल?',
 (['Use only the loudest idea','Throw away the blocks','Listen and try combining their ideas'],['केवल तेज़ बोलने वाले का विचार लें','ब्लॉक फेंकें','सुनकर विचार मिलाने की कोशिश करें'],['मोठ्याने बोलणाऱ्याचेच ऐका','ठोकळे फेका','ऐकून कल्पना एकत्र वापरा']),2,'Teams can try both ideas and see what works.','टीम दोनों विचार आज़माकर देख सकती है।','संघ दोन्ही कल्पना वापरून पाहू शकतो.'),
]

for key in ('habit','goodbad','emotion'):
    LEVELS[key][2]=bank(SCENARIOS[:3])
    LEVELS[key][3]=bank(SCENARIOS[3:])

for key in ('match','puzzle'):
    LEVELS[key][2]=bank([
        q('Which has four equal sides?', 'किसकी चार बराबर भुजाएँ हैं?', 'कशाच्या चार बाजू समान असतात?',(['Circle ●','Square ■','Triangle ▲'],['गोला ●','वर्ग ■','त्रिकोण ▲'],['गोल ●','चौरस ■','त्रिकोण ▲']),1,'A square has four equal sides.','वर्ग की चार बराबर भुजाएँ होती हैं।','चौरसाच्या चार समान बाजू असतात.'),
        q('Which belongs with apple and banana?', 'सेब और केले के साथ क्या आएगा?', 'सफरचंद आणि केळ्यासोबत काय येईल?',(['Mango 🥭','Shoe 👟','Bus 🚌'],['आम 🥭','जूता 👟','बस 🚌'],['आंबा 🥭','बूट 👟','बस 🚌']),0,'These are all fruits.','ये सभी फल हैं।','ही सर्व फळे आहेत.'),
        q('What fits a rainy day?', 'बारिश में क्या काम आता है?', 'पावसात काय उपयोगी पडते?',(['Sunhat','Sand bucket','Umbrella ☂'],['धूप की टोपी','रेत की बाल्टी','छाता ☂'],['उन्हाची टोपी','वाळूची बादली','छत्री ☂']),2,'An umbrella helps keep rain off us.','छाता बारिश से बचाता है।','छत्री पावसापासून मदत करते.')])
    LEVELS[key][3]=bank([
        q('What is different from circle, triangle, and square?', 'गोले, त्रिकोण और वर्ग से क्या अलग है?', 'गोल, त्रिकोण, चौरस यांच्यापेक्षा वेगळे काय?',(['Rectangle ▬','Apple 🍎','Oval ⬭'],['आयत ▬','सेब 🍎','अंडाकार ⬭'],['आयत ▬','सफरचंद 🍎','लंबगोल ⬭']),1,'An apple is a fruit. The others name flat shapes.','सेब फल है। बाकी समतल आकारों के नाम हैं।','सफरचंद फळ आहे. इतर सपाट आकार आहेत.'),
        q('Which tool measures length?', 'लंबाई किससे मापते हैं?', 'लांबी कशाने मोजतात?',(['Ruler 📏','Spoon','Crayon'],['पैमाना 📏','चम्मच','रंग'],['पट्टी 📏','चमचा','खडू']),0,'A ruler helps compare and measure length.','पैमाना लंबाई मापने में मदद करता है।','पट्टी लांबी मोजायला मदत करते.'),
        q('What do a bird and a butterfly both have?', 'पक्षी और तितली दोनों के पास क्या है?', 'पक्षी आणि फुलपाखरू या दोघांना काय असते?',(['Wheels','Shoes','Wings'],['पहिए','जूते','पंख'],['चाके','बूट','पंख']),2,'Both have wings, though their wings look different.','दोनों के पंख होते हैं, जो अलग दिखते हैं।','दोघांना वेगळे दिसणारे पंख असतात.')])

for level, counts in ((2,[6,7,8]),(3,[9,10,12])):
    rows=[]
    for index,count in enumerate(counts):
        opts=[str(count-1),str(count),str(count+1)]
        shift=index%3
        opts=opts[shift:]+opts[:shift]
        rows.append(q('How many flowers? Touch each one once.','कितने फूल? हर एक को एक बार छुएँ।','किती फुले? प्रत्येकाला एकदा हात लावा.',(opts,opts,opts),opts.index(str(count)),f'Count each flower once. There are {count}.',f'हर फूल एक बार गिनें। कुल {count} हैं।',f'प्रत्येक फूल एकदा मोजा. एकूण {count} आहेत.'))
    LEVELS['count'][level]=bank(rows,objects=[['🌼']*count for count in counts])

for level in (2,3):
    sequences=(['● ■ ▲ ● ■ ?','★ ★ ● ★ ★ ?','▲ ■ ■ ▲ ■ ?'] if level==2 else ['● ■ ■ ▲ ● ■ ■ ?','★ ● ★ ▲ ★ ● ★ ?','▲ ▲ ● ■ ▲ ▲ ● ?'])
    answers=[2,0,1] if level==2 else [2,2,1]
    options=[['●','■','▲'],['●','■','▲'],['●','■','▲']]
    LEVELS['patterns'][level]=bank([q('What repeats? Choose the next shape.','क्या दोहराता है? अगला आकार चुनें।','काय पुन्हा येते? पुढचा आकार निवडा.',(opts,opts,opts),answer,'Look for the repeating group, then continue it.','दोहराता समूह ढूँढ़कर आगे बढ़ाएँ।','पुन्हा येणारा गट शोधा आणि पुढे चालू ठेवा.') for opts,answer in zip(options,answers)],visuals=sequences)

for level in (2,3):
    rounds=(
      [('book','look','dog','sun','रात','बात','धूप','कप','पान','गान','कप','ऊन'),('rain','train','cup','hat','फूल','धूल','पेड़','जल','तारा','वारा','कप','घर'),('boat','goat','tree','bee','रानी','पानी','रात','घर','राणी','पाणी','रात','घर')]
      if level==2 else
      [('play','day','cat','cup','खाना','आना','फूल','घर','गाणे','जाणे','घर','ऊन'),('small','tall','rain','bee','माला','ताला','पेड़','दिन','माती','नाती','फूल','घर'),('blue','shoe','cat','night','सोना','रोना','आम','जल','छोटा','मोठा','घर','ऊन')])
    LEVELS['rhyme'][level]=bank([q(f'What rhymes with {en}?',f'{hi} से तुक मिलाएँ।',f'{mr} चे यमक निवडा.',([yes,no1,no2],[hy,h1,h2],[my,m1,m2]),0,f'{en} and {yes} have matching ending sounds.',f'{hi} और {hy} के अंत की आवाज़ मिलती है।',f'{mr} आणि {my} यांचे शेवटचे आवाज जुळतात.') for en,yes,no1,no2,hi,hy,h1,h2,mr,my,m1,m2 in rounds])

for level in (2,3):
    rows=[]
    steps=(
     [('Get your bag','Check the things you need','Put it by the door'),('Choose a book','Read with a grown-up','Return it to the shelf'),('Ask to join the game','Agree on turns','Play together')],
     [('Find a problem','Ask for ideas','Try a safe solution'),('Notice your feeling','Take a quiet pause','Ask for what you need'),('Plan together','Build together','Check what worked')])[level-2]
    translations=(
     [(['बैग लें','ज़रूरी चीज़ें जाँचें','दरवाज़े के पास रखें'],['दप्तर घ्या','वस्तू तपासा','दाराजवळ ठेवा']),(['किताब चुनें','बड़े के साथ पढ़ें','शेल्फ़ पर लौटाएँ'],['पुस्तक निवडा','मोठ्यांसोबत वाचा','जागेवर ठेवा']),(['साथ खेलने को पूछें','बारी तय करें','मिलकर खेलें'],['खेळायला विचारा','पाळी ठरवा','एकत्र खेळा'])],
     [(['समस्या पहचानें','विचार पूछें','सुरक्षित हल आज़माएँ'],['अडचण ओळखा','कल्पना विचारा','सुरक्षित उपाय करा']),(['भावना पहचानें','शांत विराम लें','ज़रूरत बताएँ'],['भावना ओळखा','शांत थांबा','गरज सांगा']),(['साथ योजना बनाएँ','साथ बनाएँ','देखें क्या अच्छा हुआ'],['एकत्र ठरवा','एकत्र बांधा','काय जमले ते पाहा'])])[level-2]
    for english,(hindi,marathi) in zip(steps,translations):
        order=[2,0,1]
        rows.append(q('Put the steps in order.','कदमों को क्रम से लगाएँ।','पायऱ्या क्रमाने लावा.',([english[i] for i in order],[hindi[i] for i in order],[marathi[i] for i in order]),[1,2,0],' → '.join(english),' → '.join(hindi),' → '.join(marathi)))
    LEVELS['sequence'][level]=bank(rows,type='sequence')

for level in (2,3):
    LEVELS['tidy'][level]=bank([
        q('Paper scraps','कागज़ के टुकड़े','कागदाचे तुकडे',(['Recycling with a grown-up','In a shoe','Under the rug'],['बड़े के साथ कागज़ के सही डिब्बे में','जूते में','कालीन के नीचे'],['मोठ्यांसोबत योग्य डब्यात','बुटात','चटईखाली']),0,'Ask which local bin accepts paper.','पूछें यहाँ कागज़ किस डिब्बे में डालें।','इथे कागद कोणत्या डब्यात टाकतात ते विचारा.'),
        q('A library book','पुस्तकालय की किताब','वाचनालयाचे पुस्तक',(['Bathroom floor','Return shelf or book bag','Kitchen sink'],['बाथरूम का फ़र्श','किताब की शेल्फ़ या बैग','रसोई का सिंक'],['न्हाणीघराची जमीन','पुस्तकांची जागा किंवा दप्तर','स्वयंपाकघराचा सिंक']),1,'Keep borrowed books dry and ready to return.','उधार की किताब सूखी और लौटाने के लिए तैयार रखें।','मागून आणलेले पुस्तक कोरडे आणि परतीसाठी तयार ठेवा.'),
        q('A toy with a broken sharp edge','टूटा नुकीला खिलौना','तुटलेले टोकदार खेळणे',(['In a baby’s toy box','Hide it in bed','Ask a grown-up to handle it'],['छोटे बच्चे के खिलौनों में','बिस्तर में छिपाएँ','बड़े को संभालने के लिए कहें'],['बाळाच्या खेळण्यांत','अंथरुणात लपवा','मोठ्यांना हाताळायला सांगा']),2,'Let a grown-up handle sharp or broken things.','टूटी या नुकीली चीज़ बड़े को संभालने दें।','टोकदार किंवा तुटलेली वस्तू मोठ्यांना हाताळू द्या.')])

# New game families have dedicated questions at each difficulty.
for key,title,icon,color in [
 ('shapes',tr('Shape workshop','आकारों की कार्यशाला','आकारांची कार्यशाळा'),'▲','lilac'),
 ('compare',tr('More or fewer?','ज़्यादा या कम?','जास्त की कमी?'),'⚖','mint'),
 ('numbers',tr('Number path','गिनती का रास्ता','अंकांची वाट'),'🔢','yellow')]:
    BASE[key]=dict(title=title,icon=icon,color=color)
    LEVELS[key]={}
    for level in (1,2,3):
        rows=[]
        for index in range(3):
            if key=='numbers':
                start=(level-1)*4+index+1
                prompt=tr(f'{start}, {start+1}, … what comes next?',f'{start}, {start+1}, … आगे क्या?',f'{start}, {start+1}, … पुढे काय?')
                opts=[str(start+3),str(start+2),str(start)]
                rows.append(question(prompt,tr(opts,opts,opts),1,tr('Count on one more.','एक और गिनें।','आणखी एक मोजा.')))
            elif key=='compare':
                left=level+index+1;right=left+(1 if level==1 else 2)
                if index%2:left,right=right,left
                a='● '*left;b='● '*right
                opts=[a.strip(),b.strip(),'=']
                rows.append(question(tr('Which group has more?','किस समूह में ज़्यादा हैं?','कोणत्या गटात जास्त आहेत?'),tr(opts,opts,opts),int(right>left),tr('Count both groups, or match dots one by one.','दोनों समूह गिनें या बिंदु एक-एक मिलाएँ।','दोन्ही गट मोजा किंवा ठिपके एकेक जुळवा.')))
            else:
                facts=[('Find a circle.','गोला खोजें।','गोल शोधा.',['●','▲','■'],0),('Find a triangle.','त्रिकोण खोजें।','त्रिकोण शोधा.',['■','●','▲'],2),('Find a square.','वर्ग खोजें।','चौरस शोधा.',['▲','■','●'],1)] if level==1 else [
                 ('Which has three corners?','तीन कोने किसके हैं?','तीन कोपरे कशाला?', ['●','▲','■'],1),('Which has no corners?','किसका कोई कोना नहीं?','कोपरे कशाला नाहीत?', ['●','■','▲'],0),('Which has four equal sides?','चार बराबर भुजाएँ किसकी हैं?','चार समान बाजू कशाला?', ['▲','●','■'],2)] if level==2 else [
                 ('Which shape can be the face of a round clock?','गोल घड़ी का चेहरा कौन सा आकार है?','गोल घड्याळाचा आकार कोणता?', ['▲','●','■'],1),('Which has more corners than a triangle?','त्रिकोण से ज़्यादा कोने किसके हैं?','त्रिकोणापेक्षा जास्त कोपरे कशाला?', ['●','■','▲'],1),('Which shape has the same number of sides as corners: three?','तीन भुजाएँ और तीन कोने किसके हैं?','तीन बाजू आणि तीन कोपरे कशाला?', ['▲','●','■'],0)]
                en,hi,mr,opts,answer=facts[index]
                rows.append(q(en,hi,mr,(opts,opts,opts),answer,'Look at the outline and count its sides and corners.','किनारा देखें और भुजाएँ व कोने गिनें।','कडा पाहा आणि बाजू व कोपरे मोजा.'))
        LEVELS[key][level]=bank(rows)


def game_bank(game_id, level):
    return LEVELS[game_id][level]


def public_games():
    return {key:{**{k:v for k,v in values.items() if k not in ('answers','explanations')},
                 'levels':{str(level):{k:v for k,v in data.items() if k not in ('answers','explanations')} for level,data in LEVELS[key].items()}}
            for key,values in BASE.items()}


def game_progress(games):
    result={key:dict(unlocked=1,best={}) for key in [*BASE,'memory']}
    for game in games:
        if game['game_id'] not in result:
            continue
        progress=result[game['game_id']]
        level=game['game_level']
        progress['best'][str(level)]=max(progress['best'].get(str(level),0),game['score'])
    for progress in result.values():
        while progress['unlocked']<3 and progress['best'].get(str(progress['unlocked']),0)>=2:
            progress['unlocked']+=1
    return result
