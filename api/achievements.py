"""Achievements derived from saved progress, including progress before the update."""
from .content import LESSONS


def achievements(completed, games, readings=()):
    story_ids={reading['item_id'] for reading in readings if reading['kind']=='stories'}
    verse_ids={(reading['kind'],reading['item_id']) for reading in readings if reading['kind'] in ('poems','rhymes','performances')}
    reading_languages={reading['language'] for reading in readings}
    from .content import STORIES
    collections={story['collection'] for story in STORIES if story['id'] in story_ids}
    categories={category:sum(lesson['category']==category and lesson['id'] in completed for lesson in LESSONS) for category in ('manners','habits','friends','life')}
    challenge_games={game['game_id'] for game in games if game['game_level']==3 and game['score']>=2}
    kinds = {game['game_id'] for game in games}
    scores = {game['game_id'] for game in games if game['score'] == 3}
    habits = sum(lesson['category'] == 'habits' and lesson['id'] in completed for lesson in LESSONS)
    milestones = [
        ('first-spark', '✦', 'First spark', 'पहली चमक', 'पहिली चमक', 'Complete one lesson.', 'एक पाठ पूरा करें।', 'एक धडा पूर्ण करा.', len(completed), 1),
        ('kindness-keeper', '♡', 'Kindness keeper', 'दयालु साथी', 'प्रेमळ साथीदार', 'Complete three lessons.', 'तीन पाठ पूरे करें।', 'तीन धडे पूर्ण करा.', len(completed), 3),
        ('growing-star', '✳', 'Growing star', 'बढ़ता सितारा', 'वाढता तारा', 'Complete six lessons.', 'छह पाठ पूरे करें।', 'सहा धडे पूर्ण करा.', len(completed), 6),
        ('bright-explorer', '☀', 'Bright explorer', 'चमकता खोजी', 'तेजस्वी शोधक', 'Complete ten lessons.', 'दस पाठ पूरे करें।', 'दहा धडे पूर्ण करा.', len(completed), 10),
        ('habit-helper', '🌿', 'Habit helper', 'आदतों का साथी', 'सवयींचा साथी', 'Complete three Good Habits lessons.', 'अच्छी आदतों के तीन पाठ पूरे करें।', 'चांगल्या सवयींचे तीन धडे पूर्ण करा.', habits, 3),
        ('first-game', '🎈', 'Ready to play', 'खेलने को तैयार', 'खेळायला तयार', 'Finish any mini game.', 'कोई भी छोटा खेल पूरा करें।', 'कोणताही एक छोटा खेळ पूर्ण करा.', len(games), 1),
        ('game-explorer', '🧩', 'Game explorer', 'खेलों का खोजी', 'खेळांचा शोधक', 'Finish four different games.', 'चार अलग-अलग खेल पूरे करें।', 'चार वेगवेगळे खेळ पूर्ण करा.', len(kinds), 4),
        ('triple-spark', '✨', 'Triple spark', 'तीन चमकते सितारे', 'तीन चमकते तारे', 'Earn three stars in three different games.', 'तीन अलग-अलग खेलों में तीन-तीन सितारे पाएँ।', 'तीन वेगवेगळ्या खेळांत प्रत्येकी तीन तारे मिळवा.', len(scores), 3),
        ('memory-friend', '🌼', 'Memory friend', 'यादों का दोस्त', 'आठवणींचा मित्र', 'Match all the pairs in Memory Garden.', 'याददाश्त के बगीचे की सारी जोड़ियाँ मिलाएँ।', 'स्मरणबागेतील सर्व जोड्या जुळवा.', int('memory' in scores), 1),
        ('patient-player', '🪁', 'Playful persistence', 'कोशिश का कमाल', 'प्रयत्नांची कमाल', 'Finish ten rounds of play.', 'खेल के दस दौर पूरे करें।', 'खेळाच्या दहा फेऱ्या पूर्ण करा.', len(games), 10),
    ]
    milestones.extend([
        ('learning-path', '📚', 'Learning pathfinder', 'सीख का खोजी', 'शिकण्याचा शोधक', 'Complete twenty lessons.', 'बीस पाठ पूरे करें।', 'वीस धडे पूर्ण करा.', len(completed), 20),
        ('whole-garden', '🌳', 'Whole garden explorer', 'पूरे बगीचे का खोजी', 'संपूर्ण बागेचा शोधक', 'Complete fifty lessons.', 'पचास पाठ पूरे करें।', 'पन्नास धडे पूर्ण करा.', len(completed), 50),
        ('challenge-star', '🏅', 'Challenge star', 'चुनौती का सितारा', 'आव्हानाचा तारा', 'Earn three stars at difficulty three in any game.', 'किसी खेल की तीसरी कठिनाई में तीन सितारे पाएँ।', 'कोणत्याही खेळाच्या तिसऱ्या पातळीवर तीन तारे मिळवा.', int(any(game['game_level']==3 and game['score']==3 for game in games)), 1),
    ])
    milestones.extend([
        ('story-spark','📖','Story spark','कहानी की शुरुआत','गोष्टीची सुरुवात','Finish your first story together.','साथ में पहली कहानी पूरी करें।','सोबत पहिली गोष्ट पूर्ण करा.',len(story_ids),1),
        ('story-traveller','🧭','Story traveller','कहानी का यात्री','गोष्टीचा प्रवासी','Finish five different stories.','पाँच अलग कहानियाँ पूरी करें।','पाच वेगळ्या गोष्टी पूर्ण करा.',len(story_ids),5),
        ('tale-keeper','🏰','Tale keeper','कहानियों का रखवाला','गोष्टींचा राखणदार','Finish ten different stories.','दस अलग कहानियाँ पूरी करें।','दहा वेगळ्या गोष्टी पूर्ण करा.',len(story_ids),10),
        ('grand-library','📚','Grand library explorer','बड़ी लाइब्रेरी का खोजी','मोठ्या वाचनालयाचा शोधक','Finish twenty different stories.','बीस अलग कहानियाँ पूरी करें।','वीस वेगळ्या गोष्टी पूर्ण करा.',len(story_ids),20),
        ('rhyme-spark','🎶','A little rhythm','लय की शुरुआत','लयीची सुरुवात','Finish one poem, rhyme, or performance.','एक कविता, बाल गीत या प्रस्तुति पूरी करें।','एक कविता, गीत किंवा सादरीकरण पूर्ण करा.',len(verse_ids),1),
        ('poetry-pal','🌸','Poetry pal','कविताओं का साथी','कवितांचा साथी','Finish five different verses or performances.','पाँच अलग कविताएँ या प्रस्तुतियाँ पूरी करें।','पाच वेगळ्या कविता किंवा सादरीकरणे पूर्ण करा.',len(verse_ids),5),
        ('rhythm-garden','🎼','Rhythm garden','लय का बगीचा','लयीची बाग','Finish ten different verses or performances.','दस अलग कविताएँ या प्रस्तुतियाँ पूरी करें।','दहा वेगळ्या कविता किंवा सादरीकरणे पूर्ण करा.',len(verse_ids),10),
        ('two-languages','🌍','Two language explorer','दो भाषाओं का खोजी','दोन भाषांचा शोधक','Read or listen in both English and Hindi.','अंग्रेज़ी और हिन्दी दोनों में पढ़ें या सुनें।','इंग्रजी आणि हिंदी दोन्हीत वाचा किंवा ऐका.',len(reading_languages & {'en','hi'}),2),
        ('story-worlds','🗺','Many story worlds','कहानियों की कई दुनिया','गोष्टींची अनेक विश्वे','Finish stories from three collections.','तीन संग्रहों की कहानियाँ पूरी करें।','तीन संग्रहांतील गोष्टी पूर्ण करा.',len(collections),3),
        ('kind-words-champion','💬','Kind words champion','अच्छे शब्दों का सितारा','गोड शब्दांचा तारा','Complete six Kind Words lessons.','अच्छे शब्दों के छह पाठ पूरे करें।','गोड शब्दांचे सहा धडे पूर्ण करा.',categories['manners'],6),
        ('balanced-garden','🌻','A balanced garden','हर ओर सीख','सर्व बाजूंनी शिकणे','Complete two lessons in every category.','हर श्रेणी में दो पाठ पूरे करें।','प्रत्येक प्रकारात दोन धडे पूर्ण करा.',sum(value>=2 for value in categories.values()),4),
        ('challenge-explorer','🚀','Challenge explorer','चुनौतियों का खोजी','आव्हानांचा शोधक','Earn two stars at difficulty three in three games.','तीन खेलों की तीसरी कठिनाई में दो सितारे पाएँ।','तीन खेळांच्या तिसऱ्या पातळीवर दोन तारे मिळवा.',len(challenge_games),3),
    ])
    return [dict(id=key, icon=icon, name=en, title=dict(en=en, hi=hi, mr=mr),
                 goal=dict(en=goal_en, hi=goal_hi, mr=goal_mr), current=min(count, target),
                 target=target, earned=count >= target)
            for key, icon, en, hi, mr, goal_en, goal_hi, goal_mr, count, target in milestones]
