# Curriculum sources

Brightly contains 50 original learning lessons, 14 mini games with three difficulties each, 24 complete bilingual traditional-story retellings, 11 traditional nursery rhymes, 11 credited poems, and 6 official video performances. Story retellings and new translations are identified separately from authors’ original texts. This is a selected collection of familiar children’s readings.

## Learning activities

These resources informed the choice of original learning activities.

- [Harvard Center on the Developing Child: Brain-Building Through Play](https://developingchild.harvard.edu/resources/handouts-tools/brainbuildingthroughplay/) inspired activities for practicing attention and remembering an order of events.
- [NAEYC: Word Play Throughout the Day](https://www.naeyc.org/node/5208) inspired the rhyming games and the use of home-language verses.
- [NAEYC: Reimagining Infant and Toddler Preliteracy Programs](https://www.naeyc.org/resources/pubs/yc/jul2020/reimagining-infant-toddler-preliteracy-programs) inspired rhymes with simple movements and caregiver prompts.

## Traditional stories and nursery rhymes

- [Aesop’s Fables, V. S. Vernon Jones edition, 1912](https://www.gutenberg.org/files/11339/11339-h/11339-h.htm) provides the underlying plots for the Aesop collection, including the tortoise and hare, lion and mouse, crow and pitcher, wind and sun, and bundle of sticks.
- [The Real Mother Goose, 1916](https://www.gutenberg.org/files/10607/10607-h/10607-h.htm) provides early traditional versions of the nursery verses. Brightly uses short English selections. New translations are adaptations for meaning and rhythm.
- [Stone Soup folklore collection, University of Pittsburgh](https://sites.pitt.edu/~dash/type1548.html) records the traditional motif behind the new village-soup story.
- [Oxford University Press kindergarten teaching guide](https://oup.com.pk/media/teaching-guides/My%20Learning%20Train_%20World%20of%20Letters/World%20of%20Letters%20Kindergarten.pdf) documents the cap-seller and monkeys oral-story tradition. Brightly uses new prose rather than the guide’s wording or the text of a modern picture book.
- [The Star, Jane Taylor, Academy of American Poets](https://poets.org/poem/star) provides the early poem whose opening stanza became Twinkle, Twinkle, Little Star.
- [Mary Had a Little Lamb publication history, Smithsonian Libraries](https://blog.library.si.edu/blog/2010/09/01/mary-had-a-little-lamb/) documents Sarah Josepha Hale’s nineteenth-century verse.

## Complete story-room replacement

The story room now uses twenty-four complete original retellings in English and Hindi. Each has dialogue, a narrative resolution, a discussion prompt, and a moral. Some situations and endings are softened for young children. Retellings are identified in the interface. They are separate from the original-language poem texts.

Panchatantra plots were checked against [the IGNCA-held Panchatantra edition](https://ignca.gov.in/Asi_data/2332.pdf). Aesop plots use the earlier editions linked above. The Akbar–Birbal tradition is also represented in [CBSE’s educational resource](https://cbseacademic.nic.in/web_material/Curriculum/Vocational/2018/MASS%20MEDIA_XI%28835%29/MASS%20MEDIA%20STUDIES-835-CLASS%20XI%20Resource%20Material.pdf). The cap-seller story is an oral folktale adaptation. Brightly’s village-soup story uses the traditional shared-soup motif.

The new credited poem shelf includes Jane Taylor’s The Star, Robert Louis Stevenson’s The Swing, Rain, The Wind, and Bed in Summer, Hariaudh’s Utho Lal and Koyal, Subhadra Kumari Chauhan’s Kadamb tree poem, and couplets by Kabir and Rahim. The author’s original language is identified. The other-language text is a new Brightly translation.

Additional poem sources include [The Swing](https://www.poetryfoundation.org/poems/43166/the-swing-56d221dc6ffc4), [A Child’s Garden of Verses](https://www.gutenberg.org/ebooks/2569), [Koyal](https://kavitakosh.org/kk/कोयल_/_अयोध्या_सिंह_उपाध्याय_‘हरिऔध’), [Utho Lal](https://www.aojha.in/quotes-etc/utho-laal-ab-aankhe-kholo), and [Kadamb tree](https://bharatdiscovery.org/india/यह_कदम्ब_का_पेड़_-सुभद्रा_कुमारी_चौहान). Minor orthographic variants occur across older editions.

## Performances and generated audio

The performance catalogue stores direct official video IDs and creator credits in `api/performances.py`. It includes Super Simple Songs, Infobells Hindi, MaMa Monkey/Vianet Media, and NCERT OFFICIAL. These performances are embedded, with no downloaded media or lyrics copied from their recordings. Availability, advertising, and recommendations remain controlled by YouTube.

The 103 neural reading tracks are newly synthesized from the published text, with the provider and voices recorded in `media/narration/index.json`. They contain about 91 minutes of English, Hindi, and Marathi readings. They are synthetic speech, separate from the original human performances. The default uses Microsoft Edge neural speech through the [community edge-tts client](https://github.com/rany2/edge-tts). Optional generated songs request original melodies from the configured singing service; those are not the original performances.

The additional 1,139 distinct activity recordings cover English and Hindi lesson narratives, questions, choices and practice instructions, plus game questions, choices and instructions across all three difficulties. Repeated choices share a file, serving 1,544 listening controls. Their published-content identifiers are listed in `media/narration/activities.json`. Narration does not contain parent or child profile data.

## Original verse recordings in the Listen action

Every text poem and nursery rhyme now opens a creator-hosted song or recitation rather than AI singing. These are recordings of the original works, not claims that an author made the recording. Recordings stay in their credited original language. Brightly translations remain written adaptations. Videos are streamed through the visible privacy-enhanced YouTube player on a user click; no soundtracks were extracted, downloaded, or redistributed. Artist/creator metadata was checked through YouTube’s public oEmbed endpoint. Representative English and Hindi players were also exercised in Chrome with real media playback.

| Reading | Recording credit | Language | Form |
| --- | --- | --- | --- |
| Twinkle, twinkle, little star | [Super Simple Songs](https://www.youtube.com/watch?v=yCjJyiqpAuU) | en | song |
| Baa, baa, black sheep | [Mother Goose Club](https://www.youtube.com/watch?v=XpvsJ4ANFp0) | en | song |
| Mary had a little lamb | [Super Simple Songs](https://www.youtube.com/watch?v=YE7PiTwhTQk) | en | song |
| Hickory, dickory, dock | [Super Simple Songs](https://www.youtube.com/watch?v=HGgsklW-mtg) | en | song |
| Hey diddle diddle | [Little Baby Bum](https://www.youtube.com/watch?v=sJiw-edttDY) | en | song |
| Row your boat | [Super Simple Songs](https://www.youtube.com/watch?v=7otAJa3jui8) | en | song |
| Humpty Dumpty | [Super Simple Songs](https://www.youtube.com/watch?v=nrv495corBc) | en | song |
| Rain, rain, go away | [Super Simple Songs](https://www.youtube.com/watch?v=c3v0rJqyCTM) | en | song |
| Pat-a-cake | [Super Simple Songs](https://www.youtube.com/watch?v=jdg50KzCR9w) | en | song |
| Little Bo-Peep | [CoComelon](https://www.youtube.com/watch?v=VS-P1QDKvNw) | en | song |
| One, two, buckle my shoe | [ChuChu TV](https://www.youtube.com/watch?v=FuZ9BiO4PQY) | en | song |
| The Star — Twinkle, Twinkle | [Little Learning Tales · Rima Patel](https://www.youtube.com/watch?v=eYPuGtWHUME) | en | recitation |
| The Swing | [Songs and Stories for the Classroom · Jim Shaw](https://www.youtube.com/watch?v=T42MKLGBv0I) | en | song |
| Rain | [Dr. Adam F. McCune](https://www.youtube.com/watch?v=S8Rqqp5Zoik) | en | recitation |
| The Wind | [LibriVox Audiobooks · Crystal F.](https://www.youtube.com/watch?v=TFLHGir2oSY) | en | recitation |
| Bed in Summer | [Jordan Harling Reads](https://www.youtube.com/watch?v=2IRUoXp1xxQ) | en | recitation |
| Wake Up, Dear Child | [ZappyToons](https://www.youtube.com/watch?v=h6g2W0k3hhQ) | hi | song |
| The Cuckoo | [Jeevan Aayam · Nandini P. Sharma](https://www.youtube.com/watch?v=d4w4awGjH9o) | hi | recitation |
| Words That Bring Peace | [Sanskar Music · Vidhi Sharma](https://www.youtube.com/watch?v=tdbtKvLR2VU) | hi | song |
| Slowly, Little by Little | [Saregama Bhakti · Baiju Mangeshkar](https://www.youtube.com/watch?v=x-kfOV1vBOw) | hi | song |
| The Thread of Love | [Suresh Wadkar](https://www.youtube.com/watch?v=e2m1Xa8HsTc) | hi | song |
| The Kadamb Tree | [Usha Verma](https://www.youtube.com/watch?v=hw0zo37RzhI) | hi | recitation |

The Wind player is limited to the first volunteer recording from the LibriVox collection. Creator arrangements may repeat lines or include other verses; the recording language and creator remain visible. The original media is controlled by its publisher and may carry advertising or become unavailable. A direct creator link is always provided. The underlying textual sources above remain distinct from rights in the performed recordings.
