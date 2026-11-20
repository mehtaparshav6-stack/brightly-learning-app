"""Original activities inspired by play, conversation and everyday discovery.

Research links and editorial scope are recorded in CONTENT_SOURCES.md.
"""
from .extra_lessons import lesson, tr

GROWING_LESSONS = [
lesson('counting','life',1,'🍓','peach',
('One touch, one number','एक चीज़, एक गिनती','एक वस्तू, एक अंक'),
('Lulu puts three toy berries in a bowl. She points to each berry once: one, two, three. The last number tells her how many there are. She counts slowly so no berry is missed.','लूलू कटोरे में तीन खिलौने वाले फल रखती है। वह हर फल को एक बार छूती है: एक, दो, तीन। आखिरी गिनती बताती है कि कुल कितने फल हैं। वह धीरे गिनती है।','लुलू वाटीत तीन खेळण्यातली फळे ठेवते. प्रत्येक फळाला एकदा हात लावून मोजते: एक, दोन, तीन. शेवटचा अंक एकूण फळे किती आहेत ते सांगतो. ती हळूहळू मोजते.'),
('How can Lulu count carefully?','लूलू ध्यान से कैसे गिने?','लुलू नीट कसे मोजू शकते?'),
(['Point to each berry once','Count one berry many times','Guess without looking'],['हर फल को एक बार छुए','एक फल को बार-बार गिने','बिना देखे बताए'],['प्रत्येक फळाला एकदा हात लावा','तेच फळ पुन्हा पुन्हा मोजा','न पाहता अंदाज करा']),0,
('Count three large toys together. Touch each one once.','साथ में तीन बड़े खिलौने गिनें। हर खिलौने को एक बार छुएँ।','एकत्र तीन मोठी खेळणी मोजा. प्रत्येकाला एकदा हात लावा.')),
lesson('patterns','life',2,'◆','lilac',
('A pattern parade','दोहराव की परेड','नक्षीची मिरवणूक'),
('Ari lays out a leaf, a flower, a leaf, a flower. The same little group keeps coming back. “A leaf is next!” Ari says. Patterns can be in pictures, sounds and movements.','आरि एक पत्ता, एक फूल, फिर पत्ता, फिर फूल रखता है। वही जोड़ी दोहराती है। वह कहता है, “अब पत्ता आएगा!” चित्रों, आवाज़ों और हरकतों में दोहराव हो सकता है।','आरी पान, फूल, पुन्हा पान, फूल ठेवतो. तीच जोडी पुन्हा येते. तो म्हणतो, “आता पान येईल!” चित्रे, आवाज आणि हालचालींमध्ये नक्षी असू शकते.'),
('Leaf, flower, leaf, flower… what comes next?','पत्ता, फूल, पत्ता, फूल… अब क्या आएगा?','पान, फूल, पान, फूल… पुढे काय?'),
(['A shoe','A leaf','A cup'],['जूता','पत्ता','कप'],['बूट','पान','कप']),1,
('Try clap, tap, clap, tap together. What comes next?','साथ में ताली, थपकी, ताली, थपकी करें। आगे क्या आएगा?','एकत्र टाळी, थाप, टाळी, थाप द्या. पुढे काय येईल?')),
lesson('mistakes','friends',2,'🌈','yellow',
('A new way to try','फिर कोशिश का नया तरीका','पुन्हा प्रयत्नाची नवी वाट'),
('Uma draws a circle, but it looks wobbly. She feels disappointed. Her friend says, “We can try another way.” Uma turns it into a cloud. A mistake can help us discover something new.','उमा का गोला टेढ़ा बनता है। उसे निराशा होती है। दोस्त कहता है, “हम दूसरा तरीका आज़मा सकते हैं।” उमा उसे बादल बना देती है। गलती से कुछ नया सीख सकते हैं।','उमाचे वर्तुळ वाकडे होते. तिला वाईट वाटते. मैत्रीण म्हणते, “दुसरी पद्धत वापरून पाहू.” उमा त्याचा ढग बनवते. चुकीतून काहीतरी नवे शिकता येते.'),
('What can Uma do when something goes wrong?','कुछ गलत होने पर उमा क्या करे?','चूक झाल्यावर उमा काय करू शकते?'),
(['Never draw again','Hide every picture','Try a different idea'],['फिर कभी चित्र न बनाए','हर चित्र छिपाए','दूसरा विचार आज़माए'],['पुन्हा कधीच चित्र काढू नये','सर्व चित्रे लपवावी','नवी कल्पना वापरून पाहावी']),2,
('Turn a scribble into a picture together. There is no perfect shape.','मिलकर टेढ़ी लकीरों से चित्र बनाएँ। बिल्कुल सही आकार ज़रूरी नहीं।','एकत्र रेघोट्यांचे चित्र बनवा. अगदी अचूक आकाराची गरज नाही.')),
lesson('nature','habits',3,'🌿','mint',
('Little garden helpers','बगीचे के छोटे मददगार','बागेचे छोटे मदतनीस'),
('Bo sees a butterfly on a flower. Bo watches without grabbing it. With a grown-up, Bo waters a plant and leaves living leaves on the stem. Gentle hands help us care for our garden.','बो फूल पर तितली देखता है। वह उसे पकड़े बिना देखता है। किसी बड़े के साथ पौधे को पानी देता है और हरे पत्ते नहीं तोड़ता। नरम हाथों से बगीचे की देखभाल होती है।','बो फुलावर फुलपाखरू पाहतो. न पकडता त्याला पाहतो. मोठ्यांसोबत झाडाला पाणी घालतो आणि हिरवी पाने तोडत नाही. हळुवार हातांनी बागेची काळजी घेता येते.'),
('How can Bo enjoy the butterfly?','बो तितली का आनंद कैसे ले?','बो फुलपाखराचा आनंद कसा घेऊ शकतो?'),
(['Watch gently without grabbing','Pull its wings','Chase it with a stick'],['बिना पकड़े धीरे से देखे','पंख खींचे','डंडे से पीछा करे'],['न पकडता शांतपणे पाहा','पंख ओढा','काठी घेऊन पाठलाग करा']),0,
('Look for three shapes in nature with a grown-up. Leave plants where they grow.','किसी बड़े के साथ प्रकृति में तीन आकार ढूँढ़ें। पौधों को वहीं रहने दें।','मोठ्यांसोबत निसर्गात तीन आकार शोधा. झाडे जागेवरच राहू द्या.')),
lesson('permission','manners',3,'🖍','blue',
('Ask before borrowing','लेने से पहले पूछें','घेण्यापूर्वी विचारा'),
('Ira likes her friend’s blue pencil. “May I borrow it?” she asks. Her friend is still drawing and says, “After I finish.” Ira waits and chooses another colour. Asking also means listening to the answer.','इरा को दोस्त की नीली पेंसिल पसंद है। वह पूछती है, “क्या मैं ले सकती हूँ?” दोस्त चित्र बना रहा है और कहता है, “पूरा होने पर।” इरा इंतज़ार करती है और दूसरा रंग चुनती है। पूछने के साथ उत्तर सुनना भी ज़रूरी है।','इराला मित्राची निळी पेन्सिल आवडते. ती विचारते, “मी घेऊ का?” मित्र चित्र काढत आहे. तो म्हणतो, “माझे झाल्यावर.” इरा थांबते आणि दुसरा रंग निवडते. विचारताना उत्तरही ऐकायचे असते.'),
('What can Ira do while her friend uses the pencil?','दोस्त के पेंसिल इस्तेमाल करते समय इरा क्या करे?','मित्र पेन्सिल वापरत असताना इराने काय करावे?'),
(['Take it anyway','Wait and use another colour','Hide the drawing'],['फिर भी ले ले','इंतज़ार करके दूसरा रंग ले','चित्र छिपा दे'],['तरीही घेऊन टाका','थांबून दुसरा रंग वापरा','चित्र लपवा']),1,
('Practise asking to borrow something and returning it.','कोई चीज़ माँगने और वापस करने का अभ्यास करें।','वस्तू मागून घेण्याचा आणि परत देण्याचा सराव करा.')),
lesson('different-ways','friends',4,'🦋','peach',
('Many ways to join in','साथ खेलने के कई तरीके','एकत्र खेळण्याच्या अनेक वाटा'),
('A group is making music. One child sings, one taps a drum, and another watches before joining. They ask, “What would you like to do?” There is more than one way to belong.','कुछ बच्चे संगीत बना रहे हैं। एक गाता है, एक ढोल बजाता है और एक पहले देखता है। वे पूछते हैं, “तुम क्या करना चाहोगे?” साथ रहने के कई तरीके हैं।','काही मुले संगीत करत आहेत. एक गाते, एक ढोल वाजवते, तर एक आधी पाहते. ते विचारतात, “तुला काय करायला आवडेल?” सहभागी होण्याच्या अनेक वाटा आहेत.'),
('How can we help everyone feel included?','सबको शामिल महसूस कराने के लिए क्या करें?','सर्वांना सहभागी वाटण्यासाठी काय करावे?'),
(['Make everyone do the same thing','Leave quiet children out','Ask how they would like to join'],['सबसे एक ही काम कराएँ','शांत बच्चों को छोड़ दें','पूछें वे कैसे जुड़ना चाहते हैं'],['सर्वांना तेच करायला लावा','शांत मुलांना वगळा','कसे सहभागी व्हायचे ते विचारा']),2,
('Make a pretend band. Each person chooses a comfortable role.','कल्पना का संगीत समूह बनाएँ। सब अपनी पसंद की भूमिका चुनें।','खेळात संगीतगट बनवा. प्रत्येकाने सोयीची भूमिका निवडा.')),
]


def story(id, icon, title, text, talk):
    return dict(id=id, icon=icon, title=tr(*title), text=tr(*text), talk=tr(*talk))


NEW_STORIES = [
story('cloud-boat','☁',('The cloud with a new idea','बादल का नया विचार','ढगाची नवी कल्पना'),
('Milo wanted to draw a boat. His pencil slipped, and a long wobbly line crossed the page. “Oh no,” he said. Grandma sat beside him. “What else could that line be?” Milo turned the page. Now the line looked like a cloud. He added little windows and a flag. It became a cloud boat, sailing over a sleepy town. “I did not plan that,” Milo said with a smile. Grandma nodded. “Sometimes a new idea starts with a little wobble.” Milo saved the drawing to show his friend.',
'मिलो नाव बनाना चाहता था। पेंसिल फिसली और पन्ने पर टेढ़ी रेखा बन गई। “ओह!” उसने कहा। दादी पास बैठीं। “यह रेखा और क्या बन सकती है?” मिलो ने पन्ना घुमाया। रेखा बादल जैसी लगी। उसने छोटी खिड़कियाँ और झंडा बनाया। अब वह बादल की नाव थी, जो सोए शहर के ऊपर तैर रही थी। मिलो मुस्कुराया, “मैंने यह नहीं सोचा था।” दादी बोलीं, “कभी-कभी टेढ़ी रेखा से नई कल्पना आती है।” मिलो ने चित्र दोस्त को दिखाने के लिए रख लिया।',
'मिलोला नाव काढायची होती. पेन्सिल घसरली आणि पानावर वाकडी रेघ आली. “अरे!” तो म्हणाला. आजी शेजारी बसली. “या रेघेचे आणखी काय होऊ शकेल?” मिलोने पान फिरवले. रेघ ढगासारखी दिसली. त्याने छोट्या खिडक्या आणि झेंडा काढला. ती झाली ढगांची नाव, झोपलेल्या गावावरून तरंगणारी. मिलो हसला. “हे मी ठरवले नव्हते.” आजी म्हणाली, “कधी कधी वाकड्या रेघेतून नवी कल्पना सुचते.” मिलोने चित्र मित्राला दाखवण्यासाठी ठेवले.'),
('What could you turn a wobbly line into?','टेढ़ी रेखा से तुम क्या बनाओगे?','वाकड्या रेघेचे तुम्ही काय बनवाल?')),
story('quiet-band','🥁',('The very quiet band','बहुत शांत संगीत समूह','अगदी शांत वाद्यवृंद'),
('Noor invited her friends to make music. Ben tapped a box. Leela hummed a tune. Pip covered his ears. “It feels too loud,” he said. Noor stopped tapping. “Would softer sounds help?” They tried fingertip taps and a gentle hum. Pip chose to wave a ribbon in time. The band had found a sound everyone could enjoy. When they finished, they bowed to a row of toy animals. Even the tiny teddy had a front-row seat.',
'नूर ने दोस्तों को संगीत बनाने बुलाया। बेन डिब्बा बजाता और लीला गुनगुनाती। पिप ने कान ढके। “बहुत तेज़ लग रहा है,” उसने कहा। नूर रुक गई। “क्या धीमी आवाज़ अच्छी लगेगी?” सबने उँगलियों से हल्की थाप दी और धीरे गुनगुनाए। पिप ने लय में फीता हिलाया। अब सब संगीत का आनंद ले रहे थे। अंत में उन्होंने सामने बैठे खिलौनों को झुककर नमस्ते कहा। छोटे भालू को भी आगे की जगह मिली थी।',
'नूरने मित्रांना संगीत करायला बोलावले. बेन डबा वाजवत होता, लीला गुणगुणत होती. पिपने कान झाकले. “खूप मोठा आवाज आहे,” तो म्हणाला. नूर थांबली. “हळू आवाज चालेल का?” त्यांनी बोटांनी हलक्या थापा दिल्या आणि हळू गुणगुणले. पिपने तालावर फीत हलवली. आता सगळ्यांना संगीत आवडले. शेवटी त्यांनी समोर बसलेल्या खेळण्यांना वाकून नमस्कार केला. छोट्या अस्वलालाही पुढची जागा मिळाली होती.'),
('How did the friends make space for Pip?','दोस्तों ने पिप का ध्यान कैसे रखा?','मित्रांनी पिपची काळजी कशी घेतली?')),
story('moon-pocket','🌙',('A pocket full of tomorrow','कल की छोटी पोटली','उद्याची छोटी पिशवी'),
('At bedtime, Tara had many questions. Would it rain? Would her friend visit? Would her seed grow? Papa brought an empty little bag. “Let’s put our tomorrow thoughts here for the night.” Tara pretended to tuck each thought inside. They chose a quiet story and watched the moon from the window. The questions would still be there tomorrow. For now, Tara could rest. She placed the little bag beside her book and whispered, “See you in the morning, thoughts.”',
'सोने के समय तारा के बहुत सवाल थे। क्या बारिश होगी? क्या दोस्त आएगा? क्या बीज बढ़ेगा? पापा छोटी खाली थैली लाए। “कल की बातें रात भर यहाँ रख दें?” तारा ने कल्पना में हर विचार थैली में रखा। उन्होंने शांत कहानी चुनी और खिड़की से चाँद देखा। सवाल कल भी रहेंगे। अभी तारा आराम कर सकती थी। उसने थैली किताब के पास रखी और कहा, “विचारों, सुबह मिलेंगे।”',
'झोपताना ताराला अनेक प्रश्न होते. पाऊस पडेल का? मैत्रीण येईल का? बी उगवेल का? बाबांनी छोटी रिकामी पिशवी आणली. “उद्याचे विचार रात्रभर इथे ठेवूया?” ताराने कल्पनेत प्रत्येक विचार पिशवीत ठेवला. त्यांनी शांत गोष्ट निवडली आणि खिडकीतून चंद्र पाहिला. प्रश्न उद्याही असतील. आत्ता तारा विश्रांती घेऊ शकत होती. तिने पिशवी पुस्तकाजवळ ठेवली आणि म्हटले, “विचारांनो, सकाळी भेटू.”'),
('What is one quiet thing you enjoy before bed?','सोने से पहले तुम्हें कौन सा शांत काम पसंद है?','झोपण्यापूर्वी कोणती शांत गोष्ट करायला आवडते?')),
story('bridge','🌉',('The bridge made together','मिलकर बनाया पुल','एकत्र बांधलेला पूल'),
('Three toy animals needed to cross a pretend river. Ravi built a tall bridge, but it tipped. Asha tried a wide bridge, but it was too short. They sat together and looked at the blocks. “What if we use your wide base and my long pieces?” Ravi asked. They built slowly, taking turns. The rabbit crossed first, then the bear, then a very proud duck. The bridge worked because both ideas had a place. “Shall we build a station next?” Asha asked.',
'तीन खिलौने जानवरों को कल्पना की नदी पार करनी थी। रवि का ऊँचा पुल गिर गया। आशा का चौड़ा पुल छोटा पड़ा। वे साथ बैठकर ब्लॉक देखने लगे। रवि बोला, “तुम्हारा चौड़ा आधार और मेरे लंबे टुकड़े मिलाएँ?” उन्होंने बारी-बारी धीरे पुल बनाया। पहले खरगोश, फिर भालू, फिर खुश बत्तख पार हुई। दोनों के विचारों से पुल बन गया। आशा ने पूछा, “अब स्टेशन बनाएँ?”',
'तीन खेळण्यातल्या प्राण्यांना खोटी नदी ओलांडायची होती. रवीचा उंच पूल पडला. आशाचा रुंद पूल लहान पडला. ते एकत्र बसून ठोकळे पाहू लागले. रवी म्हणाला, “तुझा रुंद पाया आणि माझे लांब तुकडे वापरूया?” त्यांनी आळीपाळीने हळू पूल बांधला. आधी ससा, मग अस्वल, मग आनंदी बदक गेले. दोघांच्या कल्पनांनी पूल जमला. आशाने विचारले, “आता स्टेशन बांधूया?”'),
('What would you build with a friend?','दोस्त के साथ तुम क्या बनाओगे?','मित्रासोबत तुम्ही काय बांधाल?')),
]


def rhyme(id, icon, title, lines, activity):
    return dict(id=id, icon=icon, title=tr(*title), lines=tr(*lines), activity=tr(*activity))


NEW_RHYMES = [
rhyme('leaf-beat','🍃',('The leaf-and-flower beat','पत्ते और फूल की ताल','पानाफुलांचा ताल'),
(['Leaf and flower, leaf and flower,','Make a pattern for our tower.','Tap your knees and clap once more,','What comes next? Let’s both explore!'],['पत्ता, फूल, पत्ता, फूल,','दोहराव का प्यारा उसूल।','थपकी, ताली, फिर दोहराएँ,','आगे क्या है, मिलकर गाएँ।'],['पान आणि फूल, पान आणि फूल,','नक्षी काढू छान अनुकूल.','थाप आणि टाळी, पुन्हा तीच पाळी,','पुढे काय येते, सांगा यावेळी.']),
('Alternate a gentle knee tap and a clap. Sitting still and watching is welcome too.','धीरे घुटना थपथपाएँ, फिर ताली बजाएँ। बैठकर देखना भी ठीक है।','हळू गुडघ्यावर थाप आणि मग टाळी द्या. बसून पाहिले तरी चालेल.')),
rhyme('five-seeds','🌱',('Five sleepy seeds','पाँच नन्हे बीज','पाच छोटी बिया'),
(['One little seed in a soft brown bed,','Two little leaves peep over its head.','Three little raindrops, four sunny beams,','Five sleepy seeds with big green dreams.'],['एक बीज सोया मिट्टी के पास,','दो पत्तों ने खोली आँख।','तीन बूँदें, चार किरणें आईं,','पाँच बीजों ने आस जगाई।'],['एक बी निजले मातीत छान,','दोन पाने आली, झाली कमान.','तीन थेंब, चार किरणे आली,','पाच बियांनी स्वप्ने पाहिली.']),
('Count on your fingers from one to five. Move at your own pace.','उँगलियों पर एक से पाँच गिनें। अपनी गति से करें।','बोटांवर एक ते पाच मोजा. आपल्या वेगाने करा.')),
rhyme('kind-words','💛',('Kind words travel','अच्छे शब्दों की सैर','गोड शब्दांची सफर'),
(['Please is a pebble, thank you a stream,','Sorry can help us rebuild a dream.','A kind little word and a listening ear,','Tell a good friend, “I’m glad you are here.”'],['कृपया कहूँ, धन्यवाद दूँ,','गलती हो तो माफ़ी लूँ।','प्यारे शब्द और ध्यान से सुनना,','दोस्त के संग खुशियाँ बुनना।'],['कृपया म्हणू, आभार मानू,','चूक झाली तर माफी मागू.','गोड शब्द आणि लक्ष देऊ,','मित्रासोबत आनंद घेऊ.']),
('Choose one kind phrase and say it, sign it, or act it out together.','एक अच्छा वाक्य बोलें, इशारे से बताएँ या अभिनय करें।','एक गोड वाक्य बोला, खुणेने सांगा किंवा अभिनय करा.')),
rhyme('moon-rest','🌙',('Moonlight, soft and slow','चाँद की धीमी रोशनी','चांदण्यांची शांत वेळ'),
(['Moonlight rests upon the tree,','Quiet as a cloud can be.','Little hands can rest here too,','Tomorrow holds a sky for you.'],['चाँद की रोशनी पेड़ पर आई,','शांत हवा ने लोरी गाई।','छोटे हाथ अब आराम करें,','कल नए सपनों में रंग भरें।'],['चांदणे आले झाडावरती,','शांत वारा गाणे म्हणती.','छोटे हात विसावू द्या,','उद्याची स्वप्ने खुलू द्या.']),
('Rest your hands and find one quiet sound together.','हाथों को आराम दें और साथ एक धीमी आवाज़ सुनें।','हात विसावा द्या आणि एक शांत आवाज ऐका.')),
]
