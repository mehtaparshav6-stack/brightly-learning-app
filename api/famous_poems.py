"""Older public-domain poems with credited original-language text and new translations."""

def poem(id,icon,titles,author,original,source,en,hi):
    return dict(id=id,icon=icon,title=dict(en=titles[0],hi=titles[1]),lines=dict(en=en.strip().split('\n'),hi=hi.strip().split('\n')),
                author=author,original_language=original,available_languages=['en','hi'],source_kind='classic',source_url=source,format='poem')

FAMOUS_POEMS=[
poem('the-star','⭐',('The Star — Twinkle, Twinkle','टिमटिम छोटा तारा'), 'Jane Taylor','en','https://poets.org/poem/star',
'''Twinkle, twinkle, little star,
How I wonder what you are,
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is set,
And the grass with dew is wet,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveler in the dark
Thanks you for your tiny spark,
He could not see where to go
If you did not twinkle so.

In the dark blue sky you keep,
And often through my curtains peep,
For you never shut your eye
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.''',
'''टिमटिम करता नन्हा तारा,
कैसा सुंदर रूप तुम्हारा।
ऊँचे-ऊँचे नभ में चमको,
हीरे जैसे हँसते दमको।

सूरज जब छिप जाता है,
ओस घास पर छा जाता है,
तब तुम दीपक सा जलते हो,
सारी रात चमकते हो।

अँधेरे में जाता राही,
तुमसे पाता राह सुहानी।
तुम न चमको नभ के तारे,
कौन दिखाए पथ बेचारे?

नीले नभ में रहते हो,
परदे से भी दिखते हो।
जब तक सूरज आ न जाए,
तुम अपनी आँख न बंद कर पाए।

नन्हा उजियारा तुम्हारा,
राही का बनता है सहारा।
तुम क्या हो, यह समझ न पाऊँ,
टिमटिम तारा गाता जाऊँ।'''),
poem('the-swing','🌳',('The Swing','झूला'),'Robert Louis Stevenson','en','https://www.poetryfoundation.org/poems/43166/the-swing-56d221dc6ffc4',
'''How do you like to go up in a swing,
Up in the air so blue?
Oh, I do think it the pleasantest thing
Ever a child can do!

Up in the air and over the wall,
Till I can see so wide,
Rivers and trees and cattle and all
Over the countryside—

Till I look down on the garden green,
Down on the roof so brown—
Up in the air I go flying again,
Up in the air and down!''',
'''झूले पर ऊपर जाना कैसा,
नीले नभ में उड़ना कैसा?
मुझको लगता सबसे प्यारा,
बचपन का यह खेल हमारा।

दीवारों से ऊपर जाऊँ,
दूर-दूर तक दृश्य निहारूँ।
नदी, पेड़ और गायें दिखतीं,
हरी धरती में खुशियाँ खिलतीं।

फिर नीचे बाग़ दिखाई देता,
भूरी छत का रूप सुहाता।
ऊपर उड़ता झूला जाए,
फिर नीचे आकर मुस्काए।'''),
poem('rain-stevenson','🌧',('Rain','बारिश'),'Robert Louis Stevenson','en','https://www.gutenberg.org/ebooks/2569',
'''The rain is raining all around,
It falls on field and tree,
It rains on the umbrellas here,
And on the ships at sea.''',
'''चारों ओर बरसता पानी,
खेत और पेड़ सुनें कहानी।
छातों पर भी बूँदें आएँ,
सागर में जहाज़ नहाएँ।'''),
poem('wind-stevenson','🍃',('The Wind','हवा'),'Robert Louis Stevenson','en','https://www.gutenberg.org/ebooks/2569',
'''I saw you toss the kites on high
And blow the birds about the sky;
And all around I heard you pass,
Like ladies’ skirts across the grass—
O wind, a-blowing all day long,
O wind, that sings so loud a song!

I saw the different things you did,
But always you yourself you hid.
I felt you push, I heard you call,
I could not see yourself at all—
O wind, a-blowing all day long,
O wind, that sings so loud a song!

O you that are so strong and cold,
O blower, are you young or old?
Are you a beast of field and tree,
Or just a stronger child than me?
O wind, a-blowing all day long,
O wind, that sings so loud a song!''',
'''पतंगों को ऊँचा उड़ाती हो,
पंछी संग नभ में जाती हो।
घास पर सरसर सुनता तुमको,
फिर भी देख न पाता तुमको।
ओ हवा, दिन भर बहती,
कितना ऊँचा गाना कहती!

काम तुम्हारे दिख जाते हैं,
तुम खुद कहाँ छिप जाते हो?
धक्का महसूस कराता कौन,
आवाज़ों में आता कौन?
ओ हवा, दिन भर बहती,
कितना ऊँचा गाना कहती!

तुम इतनी ठंडी, इतनी बलवान,
छोटे हो या बड़े महान?
पेड़-खेत का जीव अनोखा,
या मुझसे ताकतवर कोई छोकरा?
ओ हवा, दिन भर बहती,
कितना ऊँचा गाना कहती!'''),
poem('bed-summer','🌅',('Bed in Summer','गर्मियों की शाम'),'Robert Louis Stevenson','en','https://www.gutenberg.org/ebooks/2569',
'''In winter I get up at night
And dress by yellow candle-light.
In summer, quite the other way,
I have to go to bed by day.

I have to go to bed and see
The birds still hopping on the tree,
Or hear the grown-up people’s feet
Still going past me in the street.

And does it not seem hard to you,
When all the sky is clear and blue,
And I should like so much to play,
To have to go to bed by day?''',
'''सर्दी में जब उठता हूँ,
पीली रोशनी में सजता हूँ।
गर्मी में बात बदल जाती,
दिन रहते ही नींद बुलाती।

बिस्तर से चिड़ियाँ दिखती हैं,
पेड़ पर फुदकती रहती हैं।
बाहर बड़ों के कदम सुनूँ,
सोने से पहले और खेलूँ।

नभ अब भी नीला-नीला है,
दिन कितना चमकीला है।
मन तो और खेलना चाहे,
पर आराम का समय आ जाए।'''),
poem('utho-lal','🌄',('Wake Up, Dear Child','उठो लाल अब आँखें खोलो'),"अयोध्यासिंह उपाध्याय ‘हरिऔध’",'hi','https://www.aojha.in/quotes-etc/utho-laal-ab-aankhe-kholo',
'''Wake, dear child, and greet the light,
Water waits to wash the night.
Lotus petals open wide,
Bees are swinging at their side.

Birds are singing in the tree,
Lovely breezes wander free.
Morning brings the golden sun,
A beautiful new day’s begun.

Rosy colours fill the skies,
Cool air gently passes by.
Little beams of sunlight play,
Flowers smile to greet the day.

Do not miss this lovely glow,
Wake, dear child, the world says hello.''',
'''उठो लाल अब आँखें खोलो,
पानी लाई मुँह धो लो।
बीती रात कमल-दल फूले,
उनके ऊपर भँवरे झूले।

चिड़ियाँ चहक उठीं पेड़ों पर,
बहने लगी हवा अति सुंदर।
भोर हुई सूरज उग आया,
नभ में छाई सुनहरी काया।

आसमान में लाली छाई,
ठंडी हवा बही सुखदाई।
नन्हीं-नन्हीं किरणें आईं,
फूल हँसे कलियाँ मुसकाईं।

इतना सुंदर समय न खोओ,
मेरे प्यारे अब मत सोओ।'''),
poem('koyal-hariaudh','🐦',('The Cuckoo','कोयल'),"अयोध्यासिंह उपाध्याय ‘हरिऔध’",'hi','https://kavitakosh.org/kk/कोयल_/_अयोध्या_सिंह_उपाध्याय_‘हरिऔध’',
'''A dark little cuckoo calls coo-coo,
From branch to branch she wanders through.
Hidden where the green leaves grow,
She sings the sweetest notes we know.

When winter’s cold begins to fade,
And sunlight warms the garden shade,
The air becomes a lovely thing,
And trees put on the clothes of spring.

With fruit and pods and buds so small,
The branches seem to hold them all.
Flowers open, bright and fair,
And gentle scents fill all the air.

Then cuckoo sings from tree to tree,
A joyful song for you and me.
Children, when you speak today,
Try a gentle, kindly way.

Kind words can bring a smile along,
As lovely as the cuckoo’s song.''',
'''काली-काली कू-कू करती,
जो है डाली-डाली फिरती!
कुछ अपनी ही धुन में ऐंठी,
छिपी हरे पत्तों में बैठी।
जो पंचम सुर में गाती है,
वह ही कोयल कहलाती है।

जब जाड़ा कम हो जाता है,
सूरज थोड़ा गरमाता है।
तब होता है समा निराला,
जी को बहुत लुभाने वाला।
हरे पेड़ सब हो जाते हैं,
नए-नए पत्ते पाते हैं।

कितने ही फल औ फलियों से,
नई-नई कोपल कलियों से,
भली भाँति वे लद जाते हैं,
बड़े मनोहर दिखलाते हैं।
रंग-रंग के प्यारे-प्यारे,
फूल फूल जाते हैं सारे।

बसी हवा बहने लगती है,
दिशा सब महकने लगती है।
तब यह मतवाली हो कर,
कूक-कूक डाली-डाली पर,
अजब समा दिखला देती है,
सबका मन अपना लेती है।

लड़के जब अपना मुँह खोलो,
तुम भी मीठी बोली बोलो।
इससे कितने सुख पाओगे,
सबके प्यारे बन जाओगे।'''),
poem('kabir-kind-words','💬',('Words That Bring Peace','ऐसी वाणी बोलिए'),'कबीर','hi','https://hi.wikisource.org/wiki/कबीर_के_दोहे',
'''Choose words that soften pride,
And let a gentle heart be heard.
Bring calm to those who hear you speak,
And find calm in your own kind words.''',
'''ऐसी वाणी बोलिए, मन का आपा खोय।
औरन को शीतल करे, आपहुं शीतल होय॥'''),
poem('kabir-patience','🌱',('Slowly, Little by Little','धीरे-धीरे रे मना'),'कबीर','hi','https://hi.wikisource.org/wiki/कबीर_के_दोहे',
'''Slowly, heart, and little by little,
Some things come in their own good time.
Though a gardener brings much water,
Fruit still waits for its season to shine.''',
'''धीरे-धीरे रे मना, धीरे सब कुछ होय।
माली सींचे सौ घड़ा, ऋतु आए फल होय॥'''),
poem('rahim-love','🧵',('The Thread of Love','रहिमन धागा प्रेम का'),'रहीम','hi','https://hi.wikisource.org/wiki/रहीम_के_दोहे',
'''Treat love’s gentle thread with care,
Do not snap it thoughtlessly.
Tie it back and knots remain,
Let your kindness keep it free.''',
'''रहिमन धागा प्रेम का, मत तोरो चटकाय।
टूटे से फिर ना जुड़े, जुड़े गाँठ परि जाय॥'''),
]

# Keep familiar traditional English nursery verses with their new translations.
from .classic_library import CLASSIC_RHYMES
TEXT_RHYMES=[item for item in CLASSIC_RHYMES if item.get('source_kind')=='traditional']
FAMOUS_POEMS.append(poem('kadamb-tree','🌳',('The Kadamb Tree','यह कदंब का पेड़'),'सुभद्रा कुमारी चौहान','hi','https://bharatdiscovery.org/india/यह_कदम्ब_का_पेड़_-सुभद्रा_कुमारी_चौहान',
'''If this kadamb tree, Mother dear,
Stood by the Yamuna’s water clear,
I’d sit upon its branches high,
And play at being Krishna nearby.
If you would buy a little flute,
I’d find a branch to climb and sit.
Without a word I’d slip away,
And in the leafy treetop play.

I’d call you through the flute’s sweet sound,
And watch you come to look around.
I’d hide among the leaves so green,
Then play again, still quite unseen.
You’d call me down, then gently say,
“My little prince, come down and play.”
“I’ll bring you sweets and toys so new,
And milk and butter just for you.”

But if I stayed and did not come,
Your worried heart would call me home.
You’d sit beneath the spreading tree,
And close your eyes to pray for me.
Then softly I would come below,
And hide where your loose shawl would flow.
You’d open up your eyes and see
Your little child upon your knee.

So we would play, just you and me,
If by the river stood this tree.''',
'''यह कदंब का पेड़ अगर माँ होता यमुना तीरे।
मैं भी उस पर बैठ कन्हैया बनता धीरे-धीरे।।
ले देतीं यदि मुझे बाँसुरी तुम दो पैसे वाली।
किसी तरह नीची हो जाती यह कदंब की डाली।।

तुम्हें नहीं कुछ कहता पर मैं चुपके-चुपके आता।
उस नीची डाली से अम्मा ऊँचे पर चढ़ जाता।।
वहीं बैठ फिर बड़े मज़े से मैं बाँसुरी बजाता।
अम्मा-अम्मा कह वंशी के स्वर में तुम्हें बुलाता।।

सुन मेरी बंसी को माँ तुम इतनी खुश हो जाती।
मुझे देखने काम छोड़ कर तुम बाहर तक आती।।
तुमको आता देख बाँसुरी रख मैं चुप हो जाता।
पत्तों में छिपकर धीरे से फिर बाँसुरी बजाता।।

गुस्सा होकर मुझे डाँटती, कहतीं नीचे आजा।
पर जब मैं ना उतरता, हँसकर कहतीं मुन्ना राजा।।
नीचे उतरो मेरे भैया तुम्हें मिठाई दूँगी।
नए खिलौने, माखन-मिसरी, दूध मलाई दूँगी।।

बहुत बुलाने पर भी माँ जब नहीं उतर कर आता।
माँ, तब माँ का हृदय तुम्हारा बहुत विकल हो जाता।।
तुम आँचल फैला कर अम्माँ वहीं पेड़ के नीचे।
ईश्वर से कुछ विनती करतीं बैठी आँखें मीचे।।

तुम्हें ध्यान में लगी देख मैं धीरे-धीरे आता।
और तुम्हारे फैले आँचल के नीचे छिप जाता।।
तुम घबरा कर आँख खोलतीं, पर माँ खुश हो जाती।
जब अपने मुन्ना राजा को गोदी में ही पातीं।।

इसी तरह कुछ खेला करते हम-तुम धीरे-धीरे।
यह कदंब का पेड़ अगर माँ होता यमुना तीरे।।'''))
for item in TEXT_RHYMES:
    item['original_language']='en'
    item['available_languages']=['en','hi','mr']
    item['source_url']='https://www.gutenberg.org/files/10607/10607-h/10607-h.htm'
    item['credit']={'en':'Traditional nursery verse. Hindi and Marathi translations by Brightly.','hi':'पारंपरिक बाल गीत। हिन्दी और मराठी रूपांतर Brightly के हैं।'}
