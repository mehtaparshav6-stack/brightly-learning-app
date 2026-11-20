"""Complete bilingual retellings of traditional moral stories.

The prose is original. Source collections and adaptation notes accompany every entry.
"""
AESOP='https://www.gutenberg.org/files/11339/11339-h/11339-h.htm'
PANCH='https://ignca.gov.in/Asi_data/2332.pdf'
FOLK='https://sites.pitt.edu/~dash/type1548.html'


def tale(id,icon,titles,theme,english,hindi,morals,question,collection='aesop'):
    source={'aesop':AESOP,'panchatantra':PANCH,'folktale':FOLK,'birbal':'https://cbseacademic.nic.in/web_material/Curriculum/Vocational/2018/MASS%20MEDIA_XI%28835%29/MASS%20MEDIA%20STUDIES-835-CLASS%20XI%20Resource%20Material.pdf'}[collection]
    if id=='cap-seller':
        source='https://oup.com.pk/media/teaching-guides/My%20Learning%20Train_%20World%20of%20Letters/World%20of%20Letters%20Kindergarten.pdf'
    return dict(id=id,icon=icon,title=dict(en=titles[0],hi=titles[1]),theme=theme,
                text=dict(en=english.strip(),hi=hindi.strip()),moral=dict(en=morals[0],hi=morals[1]),
                talk=dict(en=question[0],hi=question[1]),available_languages=['en','hi'],
                collection=collection,source_kind='adaptation',source_url=source,
                credit=dict(en='A complete Brightly retelling of a traditional tale.',hi='पारंपरिक कहानी का Brightly द्वारा पूरा पुनर्कथन।'))

STORY_LIBRARY=[
tale('lion-mouse','🦁',('The Lion and the Mouse','शेर और चूहा'),'kindness',
'''Deep in the forest, a lion was sleeping beneath a spreading tree. A little mouse ran over his paw while playing. The lion woke with a roar and caught the mouse under his great paw.
“Please let me go,” squeaked the mouse. “I did not mean to wake you. Perhaps one day I can help you.”
The lion looked at the tiny creature. “You help me?” he said with a surprised chuckle. But he lifted his paw, and the mouse hurried away.
Several days later, the lion stepped into a hunter’s rope net. The more he pulled, the tighter the ropes became. He roared until the trees seemed to tremble.
The little mouse recognised the voice. She ran through the grass and found the lion tangled in the net.
“Keep still, my friend. Now it is my turn to help.”
She began to nibble one rope, then another. Her teeth were small, but she worked patiently. At last a large hole opened, and the lion stepped free.
“You were right,” he said gently. “I needed your help after all.”
From that day, the lion greeted the mouse as a friend. He never again thought that being small meant being unable to help.''',
'''घने जंगल में एक शेर पेड़ की छाया में सो रहा था। खेलते-खेलते एक छोटा चूहा उसके पंजे पर चढ़ गया। शेर की नींद खुली। उसने गरजकर चूहे को अपने पंजे के नीचे पकड़ लिया।
“मुझे जाने दीजिए,” चूहा काँपते हुए बोला। “मैंने जानबूझकर नहीं जगाया। शायद किसी दिन मैं भी आपकी मदद कर सकूँ।”
शेर को आश्चर्य हुआ। “तुम मेरी मदद करोगे?” वह हँसा। फिर भी उसे चूहे पर दया आई और उसने पंजा हटा लिया। चूहा धन्यवाद कहकर चला गया।
कुछ दिनों बाद शेर शिकारी के रस्सी वाले जाल में फँस गया। वह जितना छूटने की कोशिश करता, जाल उतना कसता। उसकी गरज पूरे जंगल में सुनाई दी।
चूहे ने अपने मित्र की आवाज़ पहचान ली। वह दौड़कर आया और बोला, “आप शांत रहिए। अब मेरी बारी है।”
उसने एक रस्सी कुतरी, फिर दूसरी। उसके दाँत छोटे थे, लेकिन वह धैर्य से काम करता रहा। आखिर जाल में बड़ा छेद हो गया। शेर बाहर निकल आया।
“तुमने मेरी जान बचाई,” शेर ने कहा। “आज समझ आया कि छोटा साथी भी बड़ी मदद कर सकता है।”
उस दिन से दोनों पक्के मित्र बन गए। शेर हर मिलने वाले छोटे जीव से भी सम्मान से बात करने लगा।''',
('Kindness can return in unexpected ways. Everyone can help.','दयालुता कभी व्यर्थ नहीं जाती। छोटा साथी भी बड़ी मदद कर सकता है।'),('How did the mouse help in a way the lion could not?','चूहे ने ऐसा क्या किया जो शेर नहीं कर पाया?')),
tale('tortoise-hare','🐢',('The Tortoise and the Hare','कछुआ और खरगोश'),'patience',
'''Hare could race across the meadow faster than any of his friends. He liked to remind Tortoise of this every morning.
“By the time you reach that tree, I could run to the hill and back!” he boasted.
Tortoise looked up. “Let us try a race,” she said. “We can each go at our own pace.”
The woodland friends marked a path to the old oak. Fox waved a leaf, and the race began. Hare shot ahead while Tortoise took one steady step after another.
Halfway along, Hare looked back. Tortoise was a tiny dot in the distance. “There is plenty of time,” he thought. He lay down under a bush, closed his eyes, and fell asleep.
Tortoise kept walking. She passed the pond, the stone wall, and finally the sleeping hare. She was tired, so she took a short rest, then continued.
The cheering at the oak woke Hare. He sprang up and ran as fast as he could, but Tortoise had already reached the finish.
“You kept going,” Hare said, out of breath.
“And you certainly ran quickly,” replied Tortoise. “But a race lasts all the way to the end.”
Hare congratulated her. On their walk home, he discovered that a slower journey left time to notice butterflies.''',
'''खरगोश मैदान का सबसे तेज़ दौड़ने वाला जानवर था। वह रोज़ कछुए की धीमी चाल का मज़ाक उड़ाता। “तुम उस पेड़ तक पहुँचोगे, तब तक मैं पहाड़ी से लौट आऊँगा!”
एक दिन कछुआ बोला, “तो चलो दौड़ लगाते हैं। दोनों अपनी गति से चलेंगे।”
जंगल के दोस्तों ने पुराने बरगद तक रास्ता तय किया। लोमड़ी ने पत्ता हिलाया और दौड़ शुरू हो गई। खरगोश तेज़ी से आगे निकल गया। कछुआ एक-एक कदम बढ़ाता रहा।
आधे रास्ते पर खरगोश ने पीछे देखा। कछुआ बहुत दूर था। उसने सोचा, “मेरे पास बहुत समय है। थोड़ा सो लेता हूँ।” वह झाड़ी के नीचे लेट गया और गहरी नींद में सो गया।
कछुआ तालाब के पास से चला, पत्थर की दीवार पार की और सोए हुए खरगोश से आगे निकल गया। थकने पर उसने छोटा विराम लिया, फिर चल पड़ा।
बरगद के पास दोस्तों की तालियाँ सुनकर खरगोश जागा। वह पूरी ताकत से दौड़ा, लेकिन कछुआ पहले ही अंत तक पहुँच चुका था।
“तुम चलते रहे,” खरगोश ने हाँफते हुए कहा।
कछुआ मुस्कुराया। “हाँ, एक-एक कदम से रास्ता पूरा हुआ।” खरगोश ने उसे बधाई दी। घर लौटते समय उसने जाना कि धीरे चलने पर तितलियाँ भी देखी जा सकती हैं।''',
('Steady effort and finishing what you begin matter more than boasting.','घमंड से अच्छा है धैर्य और लगातार कोशिश करना।'),('What small step could you keep practising?','तुम किस चीज़ का थोड़ा-थोड़ा अभ्यास कर सकते हो?')),
tale('crow-pitcher','🐦',('The Thirsty Crow','प्यासा कौआ'),'thinking',
'''It was a hot afternoon, and a crow had been flying for a long time. The little puddles had dried, and he could find no water in the fields.
At last he saw a clay pitcher beside a garden wall. He landed on its rim and peered inside. There was water at the bottom, but the neck was too narrow for him to reach it.
He tried stretching his beak. He tried leaning from the other side. Nothing worked. The pitcher was too heavy to tip safely.
Crow stepped back into the shade. Instead of struggling harder, he looked carefully around him. On the path lay a handful of smooth pebbles.
He picked up one pebble and dropped it into the pitcher. Plop! The water rose just a little. Crow tilted his head and tried another. Plop! The water rose again.
Now he understood. He carried pebbles one by one, stopping to check the water each time. Slowly it came nearer the rim.
At last Crow could dip his beak and drink. He rested on the garden wall, cool and refreshed.
A difficult problem had become easier when he paused, noticed what was nearby, and tried one small idea at a time.''',
'''गर्मी की दोपहर थी। एक कौआ बहुत देर से पानी खोज रहा था। छोटे गड्ढे सूख गए थे और खेतों में कहीं पानी नहीं था। वह थककर एक बगीचे की दीवार पर बैठ गया।
तभी उसे पास में मिट्टी का घड़ा दिखा। वह उड़कर उसके किनारे पहुँचा। घड़े में पानी था, लेकिन बहुत नीचे। कौए की चोंच वहाँ तक नहीं पहुँच सकती थी।
उसने गर्दन बढ़ाई, दूसरी ओर से कोशिश की, पर पानी नहीं मिला। घड़ा भारी था, इसलिए उसे पलटना भी आसान नहीं था।
कौआ छाया में बैठकर सोचने लगा। रास्ते पर कुछ चिकने कंकड़ पड़े थे। उसने एक कंकड़ उठाया और घड़े में डाला। छप! पानी थोड़ा ऊपर आया। उसने दूसरा कंकड़ डाला। पानी फिर ऊपर उठा।
अब कौए को उपाय समझ आ गया। वह एक-एक कंकड़ लाकर घड़े में डालने लगा। बीच-बीच में झाँककर देखता कि पानी कितना ऊपर आया है। धीरे-धीरे पानी उसकी चोंच तक पहुँच गया।
कौए ने जी भरकर पानी पिया और ठंडी छाया में आराम किया। मुश्किल देखकर हार मानने के बजाय उसने रुककर सोचा और छोटी कोशिशों से रास्ता निकाल लिया।
घर पर यह विचार बड़े की देखरेख में बड़ी सुरक्षित वस्तुओं और कटोरे से देखा जा सकता है।''',
('Pause, observe, and solve a problem one step at a time.','समझदारी और धैर्य से कठिनाई का हल मिल सकता है।'),('Why did the water rise when Crow added pebbles?','कंकड़ डालने से पानी ऊपर क्यों आया?')),
tale('ant-grasshopper','🦗',('The Ant and the Grasshopper','चींटी और टिड्डा'),'responsibility',
'''All summer, Grasshopper sang among the tall grasses. Ant enjoyed the music, but each morning she also carried seeds to a dry store beneath a tree.
“Come and play all day,” Grasshopper called.
“I will play after I put these seeds away,” said Ant. “When the weather changes, food may be harder to find.”
Grasshopper meant to gather food later, but each bright day seemed too lovely for work. Before long, the wind turned cold. The grass grew brown, and seeds became scarce.
One evening Grasshopper reached Ant’s door, hungry and shivering. “I forgot to prepare,” he admitted.
Ant brought him inside and shared a warm meal. She did not want a friend to go hungry. Then she showed him the small tasks that had filled her store: one seed, one journey, one little job each day.
When spring returned, Grasshopper made a different plan. He gathered in the morning and played music in the afternoon. Ant listened while she rested.
By the next winter, both homes were ready. Grasshopper had learned that enjoying today and preparing for tomorrow could belong in the same day.''',
'''गर्मियों में टिड्डा घास के बीच गीत गाता रहता था। चींटी को उसका संगीत अच्छा लगता, लेकिन वह हर सुबह कुछ दाने अपने सूखे घर में रखती थी।
“आज सारा दिन खेलो!” टिड्डा कहता।
चींटी जवाब देती, “दाने रखकर खेलूँगी। मौसम बदलेगा तो खाना ढूँढ़ना कठिन हो सकता है।”
टिड्डा सोचता कि बाद में तैयारी कर लेगा। हर दिन खेलते-गाते निकल गया। फिर हवा ठंडी होने लगी। घास सूख गई और दाने कम मिलने लगे।
एक शाम भूखा टिड्डा चींटी के दरवाज़े पहुँचा। “मैंने तैयारी नहीं की,” उसने स्वीकार किया। चींटी उसे भीतर लाई और अपना भोजन बाँटा। वह अपने मित्र को भूखा नहीं रखना चाहती थी।
खाने के बाद उसने दिखाया कि रोज़ का छोटा काम कैसे सर्दियों का सहारा बन गया था। टिड्डे ने ध्यान से सुना।
वसंत आया तो उसने नया नियम बनाया। सुबह थोड़ा भोजन इकट्ठा करता और दोपहर में गीत गाता। चींटी आराम करते समय उसका संगीत सुनती।
अगली सर्दी दोनों के घर तैयार थे। टिड्डे ने समझ लिया कि आज की खुशी और कल की तैयारी, दोनों के लिए समय निकाला जा सकता है।''',
('Make time for play and for small responsibilities.','खेल के साथ ज़रूरी काम की तैयारी भी करें।'),('What little job can you do before playtime?','खेलने से पहले तुम कौन सा छोटा काम कर सकते हो?')),
tale('wind-sun','🌞',('The North Wind and the Sun','हवा और सूरज'),'kindness',
'''The North Wind and the Sun were arguing about which of them was stronger. Below them, a traveller walked along a winding road with a coat wrapped around her shoulders.
“Whoever can make her take off that coat will win,” said Wind.
Sun agreed to watch. Wind blew a cold gust down the road. The traveller pulled the coat tighter. Wind blew harder. Leaves whirled around her shoes, so she fastened every button.
After one final gust, Wind grew tired. “Your turn,” he muttered.
Sun came out from behind a cloud. He did not hurry. He warmed the road, the fields, and the traveller’s chilly hands. Soon she undid a button. Then another.
“What a pleasant afternoon,” she said. She found a shady tree, took off her coat, and sat down to rest.
Wind stared. “I pushed and pushed, yet you hardly seemed to try.”
“I helped her feel comfortable enough to choose,” Sun replied.
The two watched quietly while the traveller ate her lunch. Wind began to blow a soft breeze through the branches. This time, the traveller smiled.''',
'''एक दिन हवा और सूरज में बहस हुई। दोनों कह रहे थे कि वे अधिक शक्तिशाली हैं। नीचे रास्ते पर एक यात्री चल रही थी। उसने ठंड से बचने के लिए कोट पहन रखा था।
हवा बोली, “जो उसका कोट उतरवा दे, वही जीतेगा।” सूरज मान गया।
हवा ने तेज़ झोंका मारा। यात्री ने कोट और कसकर पकड़ लिया। हवा और तेज़ चली। पत्ते उड़ने लगे तो यात्री ने सारे बटन बंद कर लिए। बहुत कोशिश के बाद हवा थक गई।
“अब तुम्हारी बारी,” उसने कहा।
सूरज धीरे से बादल के पीछे से निकला। उसकी नरम धूप ने रास्ते, खेतों और यात्री के ठंडे हाथों को गरम किया। थोड़ी देर में यात्री ने एक बटन खोला, फिर दूसरा।
“कितना अच्छा मौसम हो गया,” उसने कहा। वह पेड़ की छाया में बैठी और कोट उतारकर पास रख दिया।
हवा हैरान थी। “मैंने इतनी ज़ोर लगाया। तुमने तो बस धूप दी!”
सूरज बोला, “कभी-कभी नरमी से वह काम हो जाता है जो ज़ोर से नहीं होता।”
अब हवा हल्की-हल्की चलने लगी। पेड़ के नीचे बैठी यात्री मुस्कुरा उठी।''',
('Gentleness and patience can work better than force.','नरमी और धैर्य कई बार ज़ोर लगाने से अधिक असर करते हैं।'),('How could you ask gently for something you need?','तुम अपनी ज़रूरत प्यार से कैसे बता सकते हो?')),
tale('fox-grapes','🍇',('The Fox and the Grapes','लोमड़ी और अंगूर'),'honesty',
'''A fox wandered through a vineyard on a warm day. Above her hung a bunch of purple grapes, round and shining in the sunlight.
“Those would be a lovely snack,” she thought.
She jumped, but the grapes were too high. She backed up, ran forward, and leapt again. Her paws brushed a leaf, but the bunch still hung beyond her reach.
Fox tried a third time from the other side of the vine. She landed with a thump in the soft grass. Now she was hot, tired, and disappointed.
A sparrow on a nearby fence chirped, “They are high up, aren’t they?”
Fox turned away. “I did not want them anyway. They are probably sour!”
But as she walked down the path, she knew she had not tasted a single grape. She was calling them sour because she felt disappointed.
She stopped beside a patch of shade. “I wanted them, and I could not reach them,” she admitted to herself. “That is the truth.”
After resting, Fox found berries growing low beside the path. This time she could enjoy her snack without pretending that the grapes had been bad.''',
'''गर्म दिन में एक लोमड़ी अंगूरों के बगीचे से गुज़र रही थी। ऊपर बेल पर बैंगनी अंगूरों का गुच्छा चमक रहा था। उसे देखकर लोमड़ी के मुँह में पानी आ गया।
“कितना अच्छा नाश्ता मिलेगा,” उसने सोचा। उसने छलाँग लगाई, लेकिन अंगूर बहुत ऊँचे थे।
वह पीछे गई, दौड़कर आई और फिर उछली। पंजा एक पत्ते से लगा, पर अंगूरों तक नहीं पहुँचा। उसने दूसरी ओर से भी कोशिश की। फिर धप्प से घास पर आ गिरी।
लोमड़ी गरम, थकी और निराश हो गई थी। पास बैठी चिड़िया बोली, “अंगूर काफ़ी ऊपर हैं न?”
लोमड़ी ने मुँह फेर लिया। “मुझे चाहिए ही नहीं। ज़रूर खट्टे होंगे!” वह वहाँ से चल पड़ी।
कुछ दूर जाकर उसे लगा कि उसने एक अंगूर भी चखा नहीं था। वह अंगूरों को खट्टा सिर्फ़ इसलिए कह रही थी क्योंकि वे उसे नहीं मिले थे।
छाया में बैठकर उसने खुद से कहा, “मुझे अंगूर चाहिए थे, लेकिन मैं पहुँच नहीं पाई। यही सच है।”
आराम के बाद उसे नीचे उगी कुछ बेरियाँ मिलीं। उसने खुशी से खाईं। अब अपनी निराशा छिपाने के लिए किसी चीज़ को बुरा बताने की ज़रूरत नहीं थी।''',
('Be honest about disappointment instead of belittling what you cannot have.','जो नहीं मिलता उसे बुरा बताने के बजाय अपनी निराशा को पहचानें।'),('What could Fox say honestly about how she felt?','लोमड़ी अपनी भावना सच-सच कैसे बता सकती थी?')),
tale('boy-wolf','🐑',('The Shepherd Boy and the Wolf','चरवाहा और भेड़िया'),'honesty',
'''A shepherd boy watched his flock on a green hillside. He was bored and wanted someone to talk to. Suddenly he had a foolish idea.
“Wolf! Wolf!” he shouted toward the village.
The villagers hurried up the hill carrying sticks to protect the sheep. There was no wolf. The boy laughed, but the villagers were tired and upset.
“Ask for company if you are lonely,” one woman told him. “An alarm is for a real danger.”
The next day, the boy played the same trick. Again people came, and again there was no wolf.
A few days later, a real wolf appeared near the fence. “Wolf!” cried the boy. But the villagers thought it was another trick. The boy managed to guide the sheep into their pen and shut the gate before the wolf came closer.
When he returned to the village, he was shaking. He explained what had happened and apologised.
“It will take time to rebuild trust,” said the woman. “Start by telling the truth, even about small things.”
The boy did. He also began asking a friend to visit during his long afternoons. He learned a better way to seek company.''',
'''एक चरवाहा पहाड़ी पर अपनी भेड़ों की रखवाली करता था। अकेले बैठे-बैठे वह ऊब जाता। एक दिन उसने शरारत सोची। वह चिल्लाया, “भेड़िया आया! भेड़िया आया!”
गाँव वाले भेड़ों को बचाने दौड़े। वहाँ कोई भेड़िया नहीं था। लड़का हँसने लगा, लेकिन गाँव वाले थक गए थे और दुखी थे।
एक महिला ने कहा, “अकेलापन लगे तो साथ माँगो। ख़तरे की आवाज़ सिर्फ़ असली ख़तरे के लिए होती है।”
अगले दिन लड़के ने फिर झूठ बोला। लोग आए और फिर खाली लौटे।
कुछ दिनों बाद सचमुच भेड़िया बाड़ के पास आया। लड़का सहायता के लिए चिल्लाया, लेकिन गाँव वालों को लगा फिर मज़ाक है। लड़के ने जल्दी से भेड़ों को बाड़े में पहुँचाया और दरवाज़ा बंद कर दिया। भेड़िया दूर चला गया।
गाँव लौटकर लड़के ने सारी बात बताई और माफ़ी माँगी। उसका डर अभी भी कम नहीं हुआ था।
महिला बोली, “भरोसा दोबारा बनने में समय लगता है। छोटी-छोटी बातों में भी सच बोलकर शुरुआत करो।”
लड़के ने बात मान ली। अकेलापन होता तो किसी दोस्त से साथ बैठने को कहता। धीरे-धीरे लोगों का भरोसा भी लौट आया।''',
('Truthfulness builds trust. Ask directly for company or help.','सच बोलने से भरोसा बनता है। साथ चाहिए तो साफ़-साफ़ कहें।'),('Why did people stop believing the boy?','लोगों को लड़के की बात पर भरोसा क्यों नहीं रहा?')),
tale('dog-reflection','🐕',('The Dog and His Reflection','कुत्ता और परछाई'),'contentment',
'''A dog was carrying a piece of bread home. It was a fine piece, large enough for a good meal. He trotted proudly toward a little bridge over a stream.
Halfway across, he looked down. In the still water he saw another dog, also holding bread.
“That dog seems to have an even bigger piece,” he thought. He forgot how pleased he had been a moment before.
Dog leaned over the side of the bridge. The other dog leaned too. He frowned. The other dog frowned back. It was his own reflection, but he did not understand.
“I want that piece as well!” Dog barked. As soon as he opened his mouth, his bread fell into the stream and floated away.
He stared at the empty water. The dog below had lost its bread too.
Then a ripple passed, and the picture broke into moving shapes. Dog finally realised what he had been looking at.
He walked home quietly. At the next meal, he stopped to appreciate what was in his bowl. Wanting someone else’s portion had made him forget to enjoy his own.''',
'''एक कुत्ता रोटी का टुकड़ा लेकर घर जा रहा था। टुकड़ा अच्छा बड़ा था और पेट भरने के लिए काफ़ी था। वह खुशी से छोटी नदी के पुल पर चढ़ा।
बीच पुल पर उसने नीचे पानी में देखा। उसे एक और कुत्ता दिखाई दिया, जिसके मुँह में रोटी थी।
“उसकी रोटी शायद मेरी रोटी से बड़ी है,” उसने सोचा। अभी जो खुशी थी, वह भूल गया।
कुत्ता झुका तो पानी वाला कुत्ता भी झुका। उसने आँखें सिकोड़कर देखा तो दूसरा भी वैसा ही करने लगा। वह अपनी परछाई देख रहा था, पर उसे पता नहीं था।
“मुझे वह टुकड़ा भी चाहिए!” सोचकर उसने भौंकने के लिए मुँह खोला। उसकी अपनी रोटी पानी में गिर गई और बहने लगी।
कुत्ता खाली मुँह खड़ा रह गया। पानी वाले कुत्ते की रोटी भी गायब थी। तभी लहर आई और परछाई टूटकर कई आकारों में बिखर गई। अब उसे समझ आया कि नीचे कोई दूसरा कुत्ता नहीं था।
वह चुपचाप घर लौटा। अगली बार खाना मिला तो उसने पहले अपनी कटोरी का ध्यान किया। दूसरे का हिस्सा पाने की चाह में वह अपना अच्छा हिस्सा खो बैठा था।''',
('Appreciate what you have, and look carefully before acting.','जो मिला है उसकी कद्र करें और बिना समझे जल्दबाज़ी न करें।'),('What changed when Dog looked more carefully?','ध्यान से देखने पर कुत्ते को क्या समझ आया?')),
tale('honest-woodcutter','🪓',('The Honest Woodcutter','ईमानदार लकड़हारा'),'honesty',
'''A woodcutter worked beside a river with an old iron axe. One morning the handle slipped, and the axe fell into deep water. He sat on the bank, worried. Without his tool, how could he work?
In this old folktale, a river spirit heard him. She appeared holding a shining golden axe.
“Is this yours?” she asked.
The woodcutter shook his head. “Mine was plain iron.”
The spirit returned with a silver axe. Again he said, “That is beautiful, but it is not mine.”
At last she brought up the worn iron axe. The woodcutter’s face brightened. “Yes! That is the one.”
The spirit thanked him for telling the truth and, in the tale, gave him the other axes as gifts.
A neighbour heard the story and wanted the same reward. He threw his own axe into the river and claimed the golden one was his. The spirit saw that he was lying and disappeared.
The neighbour returned empty-handed. The woodcutter explained that honesty was not a trick for gaining treasure. It was saying what was true even when a shiny reward made a lie tempting.''',
'''एक लकड़हारा नदी के पास अपनी पुरानी लोहे की कुल्हाड़ी से काम कर रहा था। हाथ फिसला और कुल्हाड़ी गहरे पानी में गिर गई। वह किनारे बैठकर दुखी हो गया। औज़ार के बिना काम कैसे होता?
इस पुरानी लोककथा में नदी की एक देवी ने उसकी बात सुनी। वह सोने की चमकती कुल्हाड़ी लेकर आई। “क्या यह तुम्हारी है?”
लकड़हारे ने सिर हिलाया। “नहीं, मेरी कुल्हाड़ी साधारण लोहे की थी।”
देवी चाँदी की कुल्हाड़ी लाई। उसने फिर कहा, “यह सुंदर है, लेकिन मेरी नहीं है।”
आखिर देवी पुरानी लोहे की कुल्हाड़ी लेकर आई। लकड़हारे का चेहरा खिल उठा। “हाँ, यही मेरी है!”
उसकी ईमानदारी देखकर देवी ने कहानी में बाकी कुल्हाड़ियाँ भी उपहार में दे दीं।
पड़ोसी ने सुना तो लालच में अपनी कुल्हाड़ी नदी में फेंक दी। देवी सोने की कुल्हाड़ी लाई तो उसने झूठ कहा, “यही मेरी है।” देवी उसका झूठ समझ गई और चली गई।
पड़ोसी खाली हाथ लौटा। लकड़हारे ने कहा, “ईमानदारी इनाम पाने की चाल नहीं है। चमकती चीज़ देखकर भी सच कहना ही ईमानदारी है।”''',
('Tell the truth even when a reward is tempting.','लालच के समय भी सच बोलना ईमानदारी है।'),('Which answer showed that the woodcutter was honest?','लकड़हारे का कौन सा उत्तर ईमानदारी दिखाता है?')),
tale('fox-stork','🦊',('The Fox and the Stork','लोमड़ी और सारस'),'fairness',
'''Fox invited Stork to supper. She served fragrant soup on two flat plates. Fox lapped hers easily, but Stork’s long beak could pick up almost nothing.
“Why aren’t you eating?” Fox asked, hiding a smile. Stork went home hungry.
A few days later, Stork invited Fox. He served the meal in tall jars with narrow necks. His beak fitted neatly inside. Fox could smell the delicious food, but her short nose could not reach it.
Now Fox understood how the earlier supper had felt. She sat back and said, “I made my meal easy for me and impossible for you. I am sorry.”
Stork nodded. “A meal together should make room for both guests.”
He brought a wider bowl, and Fox helped carry it to the table. The two shared supper properly at last.
At their next picnic, they planned the dishes together. There was a deep cup for Stork and a broad bowl for Fox. They had learned that treating someone well includes noticing what they need, not simply giving everyone the same thing.''',
'''लोमड़ी ने सारस को खाने पर बुलाया। उसने स्वादिष्ट सूप दो सपाट थालियों में परोसा। लोमड़ी आसानी से खा गई, लेकिन सारस की लंबी चोंच से बहुत थोड़ा सूप उठ पाया।
“तुम खा क्यों नहीं रहे?” लोमड़ी मुस्कान छिपाकर बोली। सारस भूखा लौट गया।
कुछ दिन बाद सारस ने लोमड़ी को बुलाया। उसने पतली गर्दन वाले ऊँचे बर्तनों में खाना दिया। उसकी लंबी चोंच भीतर पहुँच गई। लोमड़ी को खुशबू आ रही थी, लेकिन उसका मुँह खाने तक नहीं पहुँच सका।
अब उसे अपने व्यवहार का एहसास हुआ। उसने कहा, “मैंने तुम्हें ऐसा बर्तन दिया था जिसमें तुम खा ही नहीं सकते थे। मुझे माफ़ करो।”
सारस बोला, “साथ खाने में दोनों का ध्यान होना चाहिए।” वह चौड़ा कटोरा ले आया और लोमड़ी ने मेज़ सजाने में मदद की। दोनों ने मिलकर भोजन किया।
अगली पिकनिक में उन्होंने पहले से तय किया कि किसे कैसा बर्तन चाहिए। सारस के लिए गहरा प्याला और लोमड़ी के लिए चौड़ा कटोरा था। सबकी ज़रूरत का ध्यान रखने से साथ अच्छा लगा।''',
('Consider another person’s needs and make amends when you are unkind.','दूसरे की ज़रूरत समझें और गलती हो तो उसे सुधारें।'),('Why did different bowls make the meal fairer?','अलग बर्तनों से खाना दोनों के लिए अच्छा कैसे हुआ?')),
tale('bundle-sticks','🪵',('The Bundle of Sticks','लकड़ियों का गट्ठर'),'teamwork',
'''An old farmer had three children who often argued. If one wanted to repair a fence, another wanted to mend a gate first. Their small disagreements left many jobs unfinished.
One evening the farmer tied several thin sticks into a bundle. He asked each child to break it. They pushed and bent it, but the bundle held firm.
Then he untied the string. Each separate stick snapped easily.
“What do you notice?” he asked.
“Together they were stronger,” said the youngest.
The farmer nodded. “You do not need to have the same ideas. But if you listen and help one another, difficult jobs become easier.”
The next morning a storm had scattered branches across the lane. The eldest began clearing one end. The middle child brought a cart, and the youngest gathered small twigs. They asked before lifting anything heavy.
Soon the lane was clear. There was even time to mend the gate and finish the fence.
That evening they tied three little sticks together and set them by the door. The bundle reminded them that teamwork begins by listening, agreeing on a plan, and giving each person a useful part.''',
'''एक बूढ़े किसान के तीन बच्चे अक्सर झगड़ते थे। एक बाड़ ठीक करना चाहता तो दूसरा पहले दरवाज़ा बनाने की बात करता। बहस में कई काम अधूरे रह जाते।
एक शाम किसान ने पतली लकड़ियों का गट्ठर बाँधा। उसने हर बच्चे से गट्ठर तोड़ने को कहा। सबने दबाया और मोड़ा, लेकिन लकड़ियाँ साथ बँधी थीं, इसलिए नहीं टूटीं।
फिर किसान ने रस्सी खोल दी। अब हर लकड़ी अलग-अलग आसानी से टूट गई।
“क्या समझ आया?” उसने पूछा।
सबसे छोटा बोला, “साथ थीं तो मज़बूत थीं।”
किसान ने कहा, “तुम्हारे विचार अलग हो सकते हैं। लेकिन एक-दूसरे को सुनकर काम करोगे तो कठिन काम भी आसान होंगे।”
अगली सुबह आँधी से रास्ते पर टहनियाँ बिखरी थीं। बड़े बच्चे ने एक ओर से सफ़ाई शुरू की। दूसरे ने गाड़ी लाई और छोटे ने हल्की टहनियाँ इकट्ठा कीं। भारी चीज़ के लिए उन्होंने मदद माँगी।
जल्दी रास्ता साफ़ हो गया। दरवाज़ा और बाड़ भी ठीक हो गए। शाम को बच्चों ने तीन छोटी लकड़ियाँ साथ बाँधकर दरवाज़े के पास रखीं। अब वह गट्ठर उन्हें मिलकर योजना बनाने और एक-दूसरे की मदद करने की याद दिलाता था।''',
('Working together makes a difficult task easier.','मिलकर काम करने से कठिन काम आसान हो जाता है।'),('What different jobs helped the children finish together?','अलग-अलग काम बाँटने से बच्चों को कैसे मदद मिली?')),
tale('golden-goose','🪿',('The Goose and the Golden Egg','सोने का अंडा देने वाली हंसिनी'),'patience',
'''A farmer found a bright golden egg in the goose’s nest. At first he thought someone had painted it. But the goldsmith confirmed that it was real gold.
Every morning after that, the goose laid one golden egg. The farmer and his wife repaired their roof, bought good seed, and put money away for winter.
For a while they were grateful. Then the farmer grew impatient. “Why should we wait for one egg a day? There must be a whole pile of gold inside the goose.”
His wife warned him to think carefully, but greed had crowded out his good sense. In the old fable, he harmed the goose in an attempt to take all the gold at once.
There was no hidden treasure. Worse still, the gentle bird could give them no more eggs.
The farmer looked at the empty nest and wished he had been patient. He had destroyed something precious by wanting everything immediately.
The family still had the savings from the earlier eggs. They used them carefully and began again, now understanding the importance of caring for what gives us good things.''',
'''एक किसान को हंसिनी के घोंसले में चमकता अंडा मिला। पहले उसे लगा किसी ने रंग लगाया है, लेकिन सुनार ने बताया कि वह असली सोने का था।
उसके बाद हर सुबह हंसिनी एक सोने का अंडा देती। किसान और उसकी पत्नी ने छत ठीक कराई, अच्छे बीज लिए और सर्दियों के लिए कुछ धन बचाया।
पहले दोनों बहुत खुश थे। धीरे-धीरे किसान अधीर हो गया। उसने कहा, “रोज़ एक अंडे का इंतज़ार क्यों करें? इसके भीतर तो बहुत सारा सोना होगा!”
पत्नी ने सोचने को कहा, पर लालच ने किसान की समझ ढक ली। पुरानी कथा में उसने सारा सोना एक साथ पाने के लिए हंसिनी को नुकसान पहुँचा दिया।
भीतर कोई ख़ज़ाना नहीं था। अब वह प्यारी चिड़िया उन्हें अंडे भी नहीं दे सकती थी। किसान खाली घोंसला देखकर पछताया। सब कुछ तुरंत पाने की चाह में उसने अपनी अच्छी चीज़ ही खो दी थी।
परिवार के पास पुराने अंडों से बचाया धन था। उन्होंने समझदारी से उसका उपयोग किया और फिर से काम शुरू किया। अब वे जान गए थे कि जो हमारी मदद करता है, उसकी देखभाल भी ज़रूरी है।''',
('Greed can destroy something valuable. Be patient and care for living things.','लालच अच्छी चीज़ भी छीन सकता है। धैर्य रखें और जीवों की देखभाल करें।'),('What could the farmer have done differently?','किसान कौन सा बेहतर फैसला कर सकता था?')),
]
STORY_LIBRARY += [
tale('monkey-crocodile','🐒',('The Monkey and the Crocodile','बंदर और मगरमच्छ'),'thinking',
'''A monkey lived in a jamun tree beside a river. One day a crocodile rested below. The monkey offered him fruit, and soon the two met every afternoon to talk.
Crocodile carried some jamuns home. His wife tasted them and, in this old tale, imagined that the monkey’s heart must be sweet too. She persuaded Crocodile to bring his friend to her.
The next morning Crocodile invited Monkey to visit his home. “Climb on my back. I will carry you across.”
Monkey trusted his friend and climbed down. Halfway across the deep river, Crocodile admitted the terrible reason for the invitation.
Monkey was frightened, but he kept his voice calm. “Why did you not tell me earlier? I left my heart in the tree. Take me back so I can fetch it.”
Crocodile believed him and turned toward the bank. As soon as they reached the tree, Monkey leapt onto a branch.
“No one leaves their heart behind,” he said. “You have broken my trust. I will stay where I am safe.”
Crocodile tried to apologise, but Monkey did not climb down again. He had used quick thinking to escape and understood that friendship must include care and safety.''',
'''नदी किनारे जामुन के पेड़ पर एक बंदर रहता था। एक दिन मगरमच्छ नीचे आराम करने आया। बंदर ने उसे जामुन दिए। धीरे-धीरे दोनों रोज़ मिलने लगे।
मगरमच्छ कुछ जामुन घर ले गया। पत्नी ने खाकर कहा कि इतने मीठे फल खाने वाले बंदर का दिल भी मीठा होगा। इस पुरानी कथा में उसने मगरमच्छ को बंदर को घर बुलाने के लिए मना लिया।
अगले दिन मगरमच्छ बोला, “मेरी पत्नी तुम्हें बुला रही है। मेरी पीठ पर बैठो, मैं नदी पार करा दूँगा।”
बंदर दोस्त पर भरोसा करके बैठ गया। बीच नदी में मगरमच्छ ने बुलाने का असली कारण बता दिया। बंदर डर गया, लेकिन उसने समझदारी से काम लिया।
“यह बात पहले क्यों नहीं बताई?” उसने कहा। “मेरा दिल तो पेड़ पर रखा है। वापस चलो, ले आता हूँ।”
मगरमच्छ उसकी बात मानकर किनारे लौटा। बंदर तुरंत पेड़ की ऊँची डाल पर कूद गया।
वह बोला, “कोई अपना दिल अलग नहीं रख सकता। तुमने मेरा भरोसा तोड़ा है। अब मैं सुरक्षित जगह पर ही रहूँगा।”
मगरमच्छ ने माफ़ी माँगी, पर बंदर नीचे नहीं उतरा। सूझबूझ से उसकी जान बची। उसने समझा कि दोस्ती में भरोसा और सुरक्षा दोनों ज़रूरी हैं।''',
('Stay calm, think carefully, and seek safety when someone breaks your trust.','मुश्किल में शांत दिमाग से काम लें और अपनी सुरक्षा का ध्यान रखें।'),('What helped Monkey when he realised he was unsafe?','ख़तरा समझ आने पर बंदर को किस बात ने बचाया?'),'panchatantra'),
tale('blue-jackal','🐺',('The Blue Jackal','नीला सियार'),'honesty',
'''A hungry jackal wandered into a village. When dogs began barking, he dashed through an open doorway and fell into a pot of blue dye. He scrambled out and hurried back to the forest.
The animals had never seen a blue creature. They stood back in surprise. Jackal noticed their astonishment and decided to pretend he was someone important.
“I have been sent to rule this forest,” he announced. “You must bring me food and obey my orders.”
For a while the animals believed him. Jackal sat proudly on a rock while others worked. He even sent the other jackals away, afraid that they would recognise him.
One evening, a familiar howl floated through the trees. Hearing his own kind, Jackal forgot his disguise. He threw back his head and howled too.
“A jackal!” cried the animals. “You told us you were something else!”
They refused to follow his orders any longer. The frightened jackal ran away, and the first rain washed the blue colour from his coat.
His trick had given him attention for a little while. It could not give him the trust that comes from being honest about who you are.''',
'''एक भूखा सियार गाँव में चला गया। कुत्ते भौंके तो वह भागकर खुले दरवाज़े के भीतर घुसा और नीले रंग के बड़े बर्तन में गिर पड़ा। बाहर निकला तो उसका पूरा शरीर नीला था। वह जंगल लौट आया।
जानवरों ने ऐसा जीव कभी नहीं देखा था। वे हैरान होकर दूर खड़े हो गए। सियार को एक चाल सूझी।
उसने घोषणा की, “मुझे इस जंगल का राजा बनाकर भेजा गया है। अब सब मेरा आदेश मानो और भोजन लाओ।”
कुछ समय तक जानवर उसकी बात मानते रहे। सियार चट्टान पर बैठा रहता और दूसरे काम करते। उसने अपने जैसे सियारों को दूर भेज दिया ताकि पहचान न खुल जाए।
एक शाम जंगल में सियारों की आवाज़ गूँजी। परिचित आवाज़ सुनकर नीला सियार अपना भेष भूल गया। उसने सिर उठाया और वह भी हुआँ-हुआँ करने लगा।
जानवर समझ गए। “तुम तो सियार हो! तुमने हमसे झूठ बोला,” उन्होंने कहा। अब कोई उसका आदेश मानने को तैयार नहीं था।
सियार भाग गया। पहली बारिश में उसका नीला रंग भी धुल गया। छल से थोड़ी देर ध्यान मिल सकता है, लेकिन भरोसा सच बोलने से ही बनता है।''',
('Pretending to be someone else cannot earn lasting trust.','झूठा दिखावा अधिक समय तक भरोसा नहीं बनाए रख सकता।'),('Why did the animals stop trusting the jackal?','जानवरों ने सियार पर भरोसा क्यों छोड़ दिया?'),'panchatantra'),
tale('lion-rabbit','🐇',('The Clever Rabbit and the Lion','चतुर खरगोश और शेर'),'thinking',
'''A fierce lion frightened the animals of a forest. He demanded that they bring him food each day. The animals gathered beneath a tree, worried about how to end his bullying.
A small rabbit volunteered to speak to him. She walked slowly, thinking of a plan. When she reached the lion, he was angry that she was late.
“Another lion stopped me,” Rabbit said. “He claims this forest belongs to him.”
“Show me!” roared the lion.
Rabbit led him to a deep well. “He is hiding down there,” she said, standing safely back.
Lion looked into the still water. He saw his own reflection and mistook it for a rival. When he roared, the well echoed. Convinced that the other lion was challenging him, he leapt toward the reflection and fell into the well.
Rabbit hurried back to the waiting animals. They were finally free from the lion’s threats.
This is an old fable about thinking rather than using strength. In real life, a child who is threatened should seek a trusted adult instead of facing danger alone.''',
'''एक जंगल में ताकतवर शेर जानवरों को डराता था। वह रोज़ अपने लिए भोजन लाने का आदेश देता। सारे जानवर परेशान थे और उससे बचने का उपाय सोच रहे थे।
एक छोटी खरगोश ने शेर से बात करने की जिम्मेदारी ली। वह धीरे-धीरे चली और रास्ते में योजना बनाती रही। देर से पहुँची तो शेर गरजा, “इतनी देर क्यों हुई?”
खरगोश बोली, “रास्ते में दूसरे शेर ने रोक लिया। वह कहता है यह जंगल उसका है।”
शेर और गुस्से में आया। “मुझे दिखाओ वह कहाँ है!”
खरगोश उसे गहरे कुएँ तक ले गई। खुद सुरक्षित दूर खड़े होकर बोली, “वह नीचे छिपा है।”
शेर ने पानी में झाँका। उसे अपनी परछाई दिखाई दी। उसने समझा कोई दूसरा शेर है। वह गरजा तो कुएँ से आवाज़ गूँजी। गुस्से में बिना सोचे उसने परछाई की ओर छलाँग लगा दी और कुएँ में गिर गया।
खरगोश जानवरों के पास लौट आई। अब वे शेर की धमकियों से मुक्त थे।
यह पुरानी कहानी सूझबूझ की शक्ति बताती है। असली जीवन में कोई डराए तो बच्चे को अकेले सामना करने के बजाय भरोसेमंद बड़े की मदद लेनी चाहिए।''',
('A calm mind can solve what strength cannot. Ask for help with real danger.','बुद्धि ताकत से बड़ी हो सकती है। असली ख़तरे में बड़े की मदद लें।'),('What mistake did the lion make when he saw the water?','पानी देखकर शेर ने कौन सी गलती की?'),'panchatantra'),
tale('talkative-tortoise','🦆',('The Talkative Tortoise','बातूनी कछुआ'),'listening',
'''A tortoise lived beside a lake with two duck friends. During a dry summer, the lake began to shrink. The ducks found a larger lake beyond the hills and wanted to help their friend reach it.
They brought a strong stick. “Hold the middle in your mouth,” they said. “We will hold the ends and fly. But you must keep your mouth closed until we land.”
Tortoise nodded. The ducks rose into the air, carrying him over fields and rooftops. He had never seen the world from so high up.
People below noticed the strange sight. “Look! Ducks are carrying a tortoise!” they called.
Tortoise wanted to answer. He forgot his friends’ instruction and opened his mouth. The stick slipped away, and he fell.
In this gentle retelling, a thick haystack broke his fall. The ducks hurried down and found him shaken, with hay on his shell.
“I should have waited until we landed,” he admitted.
They completed the journey slowly along the ground, stopping often. Tortoise listened carefully whenever his friends explained a safe next step. He had discovered that there is a time to speak and a time to pay attention.''',
'''एक झील के पास कछुआ और दो बत्तखें रहते थे। गर्मियों में पानी कम होने लगा। बत्तखों को पहाड़ियों के पार बड़ी झील मिली। वे अपने मित्र को वहाँ पहुँचाना चाहती थीं।
वे मज़बूत लकड़ी लाईं। बोलीं, “बीच का हिस्सा मुँह से पकड़ लो। हम दोनों सिरों से पकड़कर उड़ेंगे। लेकिन उतरने तक मुँह मत खोलना।”
कछुए ने बात मानी। बत्तखें उसे लेकर खेतों और घरों के ऊपर उड़ने लगीं। उसने दुनिया को इतनी ऊँचाई से कभी नहीं देखा था।
नीचे लोग चकित हो गए। “देखो, बत्तखें कछुए को ले जा रही हैं!” वे बोले।
कछुए का मन जवाब देने को हुआ। वह जरूरी बात भूल गया और बोलने के लिए मुँह खोल दिया। पकड़ छूट गई और वह नीचे गिरने लगा।
इस छोटे बच्चों के पुनर्कथन में नीचे घास का बड़ा ढेर था। कछुआ उसी पर गिरा। बत्तखें नीचे आईं तो वह डरा हुआ बैठा था।
“मुझे उतरने तक इंतज़ार करना चाहिए था,” उसने कहा। उन्होंने बाकी रास्ता धीरे-धीरे ज़मीन पर तय किया। अब जब भी दोस्त सुरक्षित रास्ता बताते, कछुआ ध्यान से सुनता। उसने सीखा कि कुछ समय बोलने का और कुछ समय सुनने का होता है।''',
('Listen carefully to safety instructions and choose the right moment to speak.','सुरक्षा की बात ध्यान से सुनें और सही समय पर बोलें।'),('What important instruction did Tortoise forget?','कछुआ कौन सी ज़रूरी बात भूल गया?'),'panchatantra'),
tale('doves-net','🕊',('The Doves and the Net','कबूतर और जाल'),'teamwork',
'''A flock of doves flew over a field looking for food. Below them lay a tempting patch of grain. They landed together, and a hidden net sprang over their wings.
The doves fluttered in panic. Each pulled in a different direction, and none could escape. Their leader called out, “Stop for a moment. We need one plan.”
She asked them to take a corner of the net in their beaks. “When I count to three, we will all rise together.”
One, two, three! The birds beat their wings at the same time. The net lifted from the field. The hunter ran behind them, but the flock flew beyond his reach.
They landed beside the home of a mouse who was their friend. Mouse began to nibble the knots around their leader.
“Please free the others first,” she said. “They are frightened and tired.”
Mouse worked patiently until every dove could step out. The birds thanked their small friend and rested in the branches nearby.
One bird alone had not been strong enough. A shared plan, steady teamwork, and a helpful friend had brought the whole flock to safety.''',
'''कबूतरों का झुंड भोजन खोजते हुए खेत के ऊपर से उड़ रहा था। नीचे बहुत सारे दाने दिखाई दिए। वे साथ उतरे तो छिपा हुआ जाल उनके ऊपर आ गिरा।
कबूतर घबराकर अलग-अलग ओर फड़फड़ाने लगे। जाल नहीं हटा। उनकी अगुआ बोली, “थोड़ा रुकें। हमें एक योजना चाहिए।”
उसने सबको चोंच से जाल का एक हिस्सा पकड़ने को कहा। “तीन गिनते ही एक साथ उड़ेंगे।”
एक, दो, तीन! सबने एक ही समय पंख चलाए। जाल ज़मीन से ऊपर उठ गया। शिकारी पीछे दौड़ा, लेकिन कबूतर उसकी पहुँच से दूर निकल गए।
वे अपने मित्र चूहे के घर के पास उतरे। चूहा अगुआ की रस्सी काटने लगा तो उसने कहा, “पहले मेरे साथियों को निकालो। वे बहुत डरे और थके हैं।”
चूहा धैर्य से एक-एक गाँठ कुतरता रहा। आखिर सभी कबूतर बाहर आ गए। उन्होंने मित्र को धन्यवाद दिया और पेड़ की डालों पर आराम करने लगे।
अकेले कोई जाल नहीं उठा सकता था। साझा योजना, एक साथ मेहनत और छोटे मित्र की मदद ने पूरे झुंड को बचा लिया।''',
('A shared plan and helping friends can overcome a difficult problem.','एकता, योजना और मित्रों की मदद से बड़ी मुश्किल हल हो सकती है।'),('What changed when the birds worked together?','एक साथ कोशिश करने पर क्या बदला?'),'panchatantra'),
tale('four-friends','🦌',('The Four Friends','चार सच्चे मित्र'),'friendship',
'''Deer, Crow, Mouse, and Tortoise met every evening beside a forest pool. They were very different, but each enjoyed the others’ company.
One evening Deer did not arrive. Crow flew above the trees and spotted her trapped in a net. He called Mouse, who quickly chewed through the ropes. Tortoise came slowly to see whether his friend was safe.
Just then the hunter returned. Deer bounded into the trees, Crow flew up, and Mouse hid. Tortoise could not move quickly enough. The hunter put him in a bag and walked away.
The friends made a new plan. Deer lay still farther along the path, pretending to be hurt. Crow settled beside her as if watching. The hunter set down his bag and went to look at Deer.
Mouse hurried from the grass and nibbled a hole in the bag. Tortoise slipped out and hid near the pool. As soon as everyone was safe, Deer sprang up and ran away.
That evening, all four met again. No one had the same skills. Crow could see far, Mouse could cut knots, Deer could run, and Tortoise reminded them to care. Together their different strengths made a lasting friendship.''',
'''हिरन, कौआ, चूहा और कछुआ हर शाम जंगल के तालाब पर मिलते थे। चारों बहुत अलग थे, लेकिन एक-दूसरे की संगत पसंद करते थे।
एक शाम हिरन नहीं आया। कौआ ऊपर उड़ा और उसे जाल में फँसा देखा। उसने चूहे को बुलाया। चूहे ने रस्सियाँ कुतरकर हिरन को निकाल लिया। कछुआ भी धीरे-धीरे हाल पूछने पहुँचा।
तभी शिकारी लौट आया। हिरन पेड़ों में भागा, कौआ उड़ गया और चूहा छिप गया। कछुआ तेज़ नहीं चल सकता था। शिकारी ने उसे थैले में रखा और चल दिया।
मित्रों ने तुरंत नई योजना बनाई। हिरन आगे रास्ते पर ऐसे लेट गया जैसे उसे चोट लगी हो। कौआ पास बैठा। शिकारी ने थैला नीचे रखा और हिरन की ओर गया।
चूहा घास से निकला और थैले में छेद कर दिया। कछुआ बाहर निकलकर तालाब के पास छिप गया। सब सुरक्षित हुए तो हिरन उठकर भाग गया।
शाम को चारों फिर मिले। कौआ दूर देख सकता था, चूहा गाँठ काट सकता था, हिरन तेज़ दौड़ सकता था और कछुआ साथ निभाता था। सबकी अलग खूबियाँ मिलकर मित्रता को मज़बूत बनाती थीं।''',
('Good friends help one another and value different strengths.','सच्चे मित्र मुश्किल में साथ देते हैं और सबकी खूबियों की कद्र करते हैं।'),('What special strength did each friend bring?','हर मित्र की कौन सी अलग खूबी काम आई?'),'panchatantra'),
tale('jackal-drum','🥁',('The Jackal and the Drum','सियार और ढोल'),'thinking',
'''A jackal searched for food near an old, empty camp. Suddenly a great booming sound rolled through the trees. Boom! Boom!
He froze. “That must be an enormous creature,” he whispered. He turned to run, but hunger made him stop. Perhaps he should first find out what was making the noise.
He watched from behind a bush. Nothing moved except the branches in the wind. When a branch swung against a round object, the booming came again.
Jackal crept a little closer. The object did not chase him. It had a wooden body and a tight skin stretched across the top. It was an abandoned drum.
A dry branch tapped it once more. Boom!
Jackal laughed with relief. Such a great sound had come from something with no teeth or claws at all. He walked around it and discovered how the empty space inside made the sound seem larger.
He continued his search, calmer now. He had learned to look for evidence rather than let a frightening sound tell the whole story. In real life, we can ask a grown-up to investigate an unfamiliar noise with us.''',
'''एक सियार खाली पड़े पुराने पड़ाव के पास भोजन ढूँढ़ रहा था। अचानक जंगल में तेज़ आवाज़ गूँजी। ढम! ढम!
वह डरकर रुक गया। “ज़रूर बहुत बड़ा जीव है,” उसने सोचा। भागने को हुआ, फिर रुका। पहले पता तो करे कि आवाज़ कहाँ से आ रही है।
वह झाड़ी के पीछे से देखने लगा। हवा में पेड़ की डालियाँ हिल रही थीं। जब एक सूखी डाली गोल चीज़ से टकराती, वही बड़ी आवाज़ होती।
सियार थोड़ा पास गया। चीज़ ने उसका पीछा नहीं किया। उसका शरीर लकड़ी का था और ऊपर चमड़ा तना था। वह छोड़ा हुआ ढोल था।
डाली फिर लगी। ढम! अब सियार को हँसी आ गई। इतनी बड़ी आवाज़ उस चीज़ से आ रही थी जिसके न दाँत थे, न पंजे। उसने चारों ओर देखकर समझा कि भीतर की खाली जगह आवाज़ को गूँजदार बनाती है।
सियार शांत होकर आगे बढ़ा। उसने जाना कि सिर्फ़ आवाज़ से पूरी बात नहीं समझ आती। असली जीवन में अनजान आवाज़ आए तो बच्चे किसी बड़े से साथ जाँचने को कह सकते हैं।''',
('Look carefully before deciding that something is frightening.','बिना समझे डरने के बजाय जानकारी लेकर सोचें।'),('What was really making the loud sound?','तेज़ आवाज़ असल में किस वजह से आ रही थी?'),'panchatantra'),
tale('three-fish','🐟',('The Three Fish','तीन मछलियाँ'),'planning',
'''Three fish lived in a pond connected to a river. One afternoon they heard fishermen planning to return with nets the next morning.
The first fish said, “We should leave through the stream tonight.” She studied the waterway and swam safely into the river.
The second fish replied, “If danger comes, I will think of a way out.” The third laughed. “Nothing will happen. This pond has always been safe.”
Morning came, and a net swept through the pond. The second fish kept still as the net was lifted. Thinking she was no longer alive, a fisherman placed her near the water. With a sudden flick, she slipped back in and escaped along the stream.
The third fish had ignored the warning and had no plan. He struggled in the net until a fisherman noticed that he was very small and released him. He was lucky.
Later, the friends met in the river. The first had been prepared, the second had stayed calm, and the third had learned an important lesson: ignoring a warning does not make a danger disappear.''',
'''तीन मछलियाँ एक तालाब में रहती थीं जो छोटी धारा से नदी से जुड़ा था। एक दिन उन्होंने मछुआरों को कहते सुना, “सुबह यहाँ जाल डालेंगे।”
पहली मछली बोली, “आज रात ही नदी में चलना चाहिए।” उसने रास्ता देखा और सुरक्षित निकल गई।
दूसरी ने कहा, “ख़तरा आया तो उपाय सोचूँगी।” तीसरी हँसी, “यह तालाब हमेशा सुरक्षित रहा है। कुछ नहीं होगा।”
सुबह सचमुच जाल आया। दूसरी मछली ने घबराने के बजाय शरीर शांत रखा। मछुआरे ने उसे पानी के पास रखा तो उसने अचानक छलाँग लगाई और धारा से निकल गई।
तीसरी मछली ने चेतावनी नहीं मानी थी। वह जाल में छटपटाती रही। इस छोटे बच्चों के रूप में मछुआरे ने उसे बहुत छोटा समझकर पानी में छोड़ दिया। वह भाग्य से बची।
बाद में तीनों नदी में मिलीं। पहली तैयार थी, दूसरी ने शांत दिमाग से काम लिया और तीसरी ने बड़ी सीख पाई। चेतावनी को अनसुना करने से ख़तरा ख़त्म नहीं होता। समय रहते भरोसेमंद सलाह सुननी चाहिए।''',
('Listen to warnings and prepare before a problem becomes urgent.','चेतावनी सुनकर समय रहते तैयारी करें।'),('Which fish made a plan before the danger arrived?','किस मछली ने ख़तरा आने से पहले योजना बनाई?'),'panchatantra'),
tale('birbal-line','📏',('Birbal and the Shorter Line','बीरबल और छोटी रेखा'),'thinking',
'''Emperor Akbar enjoyed asking his court difficult questions. One morning he drew a straight line on a board and turned to the courtiers.
“Make this line shorter,” he said, “but do not erase it, cover it, or touch any part of it.”
The courtiers studied the line. One reached for a cloth, then remembered the rule. Another suggested turning the board, but the line would still be the same length.
Akbar waited. At last Birbal stepped forward with a piece of chalk.
“May I draw on the empty part of the board?” he asked.
Akbar nodded. Birbal drew a second line beside the first. His new line was much longer.
“Now look at the two together,” Birbal said. “The first line is the shorter line.”
The emperor laughed with delight. Birbal had followed every rule. He had changed the comparison instead of changing the original line.
The courtiers began finding their own examples: a small cup beside a large one, a short stick beside a long one. A puzzle that had seemed impossible became simple when someone considered it from a different direction.''',
'''बादशाह अकबर को दरबारियों से कठिन सवाल पूछना पसंद था। एक सुबह उन्होंने पट्ट पर सीधी रेखा खींची और कहा, “इस रेखा को छोटा करो। लेकिन इसे मिटाना, ढकना या छूना नहीं है।”
दरबारी सोचने लगे। किसी ने कपड़ा उठाया, फिर नियम याद करके रख दिया। किसी ने पट्ट घुमाने की बात की, लेकिन उससे रेखा की लंबाई नहीं बदलती।
अकबर इंतज़ार करते रहे। आखिर बीरबल चाक लेकर आगे आए।
उन्होंने पूछा, “क्या मैं पट्ट की खाली जगह पर कुछ बना सकता हूँ?” अकबर ने हामी भरी।
बीरबल ने पहली रेखा के पास दूसरी रेखा खींच दी। नई रेखा पहली से काफ़ी लंबी थी।
बीरबल बोले, “अब दोनों को साथ देखिए। पहली रेखा छोटी रेखा है।”
अकबर हँस पड़े। बीरबल ने कोई नियम नहीं तोड़ा था। उन्होंने पहली रेखा बदलने के बजाय तुलना बदल दी थी।
दरबारी भी उदाहरण खोजने लगे। बड़ा कप पास रखें तो दूसरा छोटा दिखता है। लंबी लकड़ी के पास दूसरी छोटी होती है। जो पहेली असंभव लगी थी, वह नया तरीका सोचने से आसान हो गई।''',
('A different point of view can reveal a simple solution.','अलग नज़रिए से सोचने पर नया उपाय मिलता है।'),('Did Birbal change the first line or its comparison?','बीरबल ने पहली रेखा बदली या तुलना?'),'birbal'),
tale('birbal-khichdi','🍲',('Birbal’s Khichdi','बीरबल की खिचड़ी'),'fairness',
'''During a cold winter, Akbar offered a reward to anyone who could stand in a palace pond all night. A poor man accepted. By morning he had completed the task, and guards brought him to court.
“How did you bear the cold?” Akbar asked.
“I kept looking at a lamp in a faraway palace window,” the man replied. “It gave me courage.”
Akbar claimed that the lamp had warmed him and refused the reward. The man went away disappointed.
Birbal heard the story. The next day he told Akbar that he was cooking khichdi and would come when it was ready. Hours passed. At last the emperor went to see him.
A little fire burned on the ground. Far above it, a pot hung from a tall pole.
“How can that fire cook food so far away?” Akbar asked.
Birbal answered gently, “If a lamp across the palace could warm a man in a pond, perhaps this fire can cook my khichdi.”
Akbar understood the unfairness of his decision. He called the man back, apologised, and gave him the promised reward. Birbal then lowered the pot, and they enjoyed a properly cooked meal.''',
'''कड़ाके की सर्दी में अकबर ने घोषणा की कि जो व्यक्ति तालाब में पूरी रात खड़ा रहेगा, उसे इनाम मिलेगा। एक गरीब व्यक्ति ने चुनौती स्वीकार की। सुबह पहरेदार उसे दरबार लाए। उसने शर्त पूरी कर ली थी।
अकबर ने पूछा, “ठंड कैसे सह ली?” उसने कहा, “दूर महल की खिड़की में दीपक दिखता रहा। उसे देखकर हिम्मत मिलती रही।”
अकबर बोले, “दीपक की गर्मी मिली होगी। इसलिए इनाम नहीं मिलेगा।” आदमी दुखी होकर चला गया।
बीरबल ने बात सुनी। अगले दिन उन्होंने कहा कि खिचड़ी पकने पर दरबार आएँगे। कई घंटे बीते तो अकबर खुद देखने पहुँचे।
नीचे छोटी आग जल रही थी और बहुत ऊपर बाँस पर बँधी हांडी लटक रही थी। अकबर ने कहा, “इतनी दूर की आग से खिचड़ी कैसे पकेगी?”
बीरबल शांत स्वर में बोले, “अगर महल का दूर का दीपक तालाब में खड़े आदमी को गरम कर सकता है, तो यह आग भी हांडी गरम कर देगी।”
अकबर को अपनी गलती समझ आ गई। उन्होंने उस आदमी को बुलाया, माफ़ी माँगी और वादा किया हुआ इनाम दिया। फिर हांडी नीचे लाई गई और खिचड़ी सचमुच पकाई गई।''',
('Be fair, keep promises, and correct a mistaken decision.','न्याय करें, वादा निभाएँ और गलती समझकर सुधारें।'),('How did Birbal help Akbar understand the unfairness?','बीरबल ने अकबर को गलती कैसे समझाई?'),'birbal'),
tale('cap-seller','🐒',('The Cap Seller and the Monkeys','टोपीवाला और बंदर'),'thinking',
'''A cap seller walked from village to village with a basket balanced on his head. One hot afternoon he rested beneath a tree, set the basket down, and fell asleep with one cap still on his head.
When he woke, the basket was empty. Above him, a troop of monkeys sat on the branches, each wearing a colourful cap.
“Those are mine!” he called. The monkeys chattered back. He waved his arms. They waved theirs. He stamped a foot. They stamped too.
At first he grew angrier. Then he noticed the pattern: the monkeys were copying everything he did.
The cap seller slowly removed his own cap. Every monkey took off its cap. He placed his on the ground. The monkeys dropped theirs among the leaves below.
He quietly gathered every cap into the basket. Before continuing, he counted them carefully and tied a cloth over the top.
As he walked away, he smiled. Shouting had not solved the problem. Watching what the monkeys were doing had given him the idea he needed.''',
'''एक टोपीवाला सिर पर टोकरी रखकर गाँव-गाँव टोपियाँ बेचता था। गर्म दोपहर में वह पेड़ के नीचे बैठा। टोकरी पास रखी और एक टोपी पहने-पहने सो गया।
जागा तो टोकरी खाली थी। ऊपर डालों पर बंदर बैठे थे। सबने रंगीन टोपी पहन रखी थी।
“ये मेरी टोपियाँ हैं!” वह बोला। बंदर भी आवाज़ करने लगे। उसने हाथ हिलाए तो उन्होंने भी हिलाए। उसने पैर पटका तो उन्होंने भी पैर पटके।
पहले टोपीवाला गुस्सा हुआ। फिर उसने गौर किया कि बंदर उसकी हर हरकत की नकल कर रहे हैं।
उसने धीरे से अपनी टोपी उतारी। बंदरों ने भी टोपी उतार ली। उसने अपनी टोपी ज़मीन पर रखी। बंदरों ने अपनी टोपियाँ नीचे गिरा दीं।
टोपीवाले ने चुपचाप सब टोपियाँ इकट्ठा कीं। उन्हें गिनकर टोकरी में रखा और ऊपर कपड़ा बाँध दिया। अब वे सुरक्षित थीं।
आगे चलते हुए वह मुस्कुराया। चिल्लाने से उपाय नहीं मिला था। बंदरों का व्यवहार ध्यान से देखने पर उसे सही विचार आया। कभी-कभी शांत होकर देखने से समस्या का रास्ता मिल जाता है।''',
('Observe carefully and think before reacting.','गुस्सा करने से पहले ध्यान से देखकर सोचें।'),('What did the seller notice about the monkeys?','टोपीवाले ने बंदरों की कौन सी बात पहचानी?'),'folktale'),
tale('stone-soup','🥣',('Stone Soup','पत्थर का सूप'),'sharing',
'''A traveller arrived in a village carrying a pot. The villagers had little food to spare and did not want to promise him a meal.
“I can make stone soup,” he said. He washed a smooth stone, placed it in the pot, and filled it with water. A grown-up lit the cooking fire, and curious neighbours gathered.
“Stone soup is pleasant,” said the traveller, “though a carrot would give it a little flavour.” A gardener brought one.
“A potato would make it heartier.” Someone fetched two potatoes. Then came an onion, a handful of beans, and a pinch of salt.
Soon a wonderful smell drifted across the square. The villagers brought bowls and sat together. Before serving, the traveller removed the stone with a long spoon and set it aside to cool.
“This soup came from all of us,” a child noticed. “The stone did not make the vegetables appear.”
The traveller smiled. “It helped us begin a conversation. You made the meal by sharing.”
There was enough for everyone. Later the villagers remembered not a magical stone, but the meal they had created from many small contributions.''',
'''एक यात्री गाँव में खाली हांडी लेकर आया। लोगों के पास थोड़ा भोजन था और कोई उसे पूरा खाना देने का वादा नहीं करना चाहता था।
यात्री बोला, “मैं पत्थर का सूप बना सकता हूँ।” उसने चिकना पत्थर धोकर हांडी में रखा और पानी भरा। बड़े ने आग जलाई। उत्सुक पड़ोसी पास आने लगे।
यात्री ने कहा, “सूप तो अच्छा बनेगा, पर एक गाजर से स्वाद बढ़ जाएगा।” माली एक गाजर ले आया।
“एक आलू भी हो तो पेट भरने वाला बने।” कोई दो आलू लाया। फिर प्याज़, थोड़ी फलियाँ और नमक भी आ गए। धीरे-धीरे स्वादिष्ट खुशबू फैलने लगी।
सब कटोरे लेकर बैठे। परोसने से पहले यात्री ने लंबे चम्मच से पत्थर निकालकर ठंडा होने रख दिया।
एक बच्चा बोला, “सूप तो हम सबकी चीज़ों से बना। पत्थर ने सब्ज़ियाँ नहीं पैदा कीं!”
यात्री मुस्कुराया। “पत्थर से बातचीत शुरू हुई। खाना तुम सबने बाँटकर बनाया।”
सबको भोजन मिला। बाद में लोगों को कोई जादुई पत्थर नहीं, बल्कि मिलकर बनाया हुआ स्वादिष्ट खाना याद रहा। थोड़ी-थोड़ी मदद ने सबके लिए अच्छी चीज़ बना दी थी।''',
('Small contributions can become something wonderful when shared.','थोड़ा-थोड़ा बाँटकर सबके लिए अच्छा बनाया जा सकता है।'),('What actually made the soup nourishing?','सूप को अच्छा असल में किन चीज़ों ने बनाया?'),'folktale'),
]
