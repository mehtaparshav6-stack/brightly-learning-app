"""Read only published activity text; never accept arbitrary text for speech."""
from .content import LESSONS, LANGUAGES
from .game_levels import LEVELS, BASE, game_bank

WORDS = {
    'en': dict(choice='Choice', memory='Find the matching pairs. Tap one card, then another. If the pictures match, they stay open. If they are different, try another pair.', game='Listen to the question and choices. Tap the answer you choose.', sequence='Tap the pictures in the order they happen. Listen to each choice before you put them in order.', tidy='Put each object in its home. You can tap a place or drag the object.', count='Tap each picture once to help you count, then choose your answer.'),
    'hi': dict(choice='विकल्प', memory='एक जैसी जोड़ियाँ खोजें। पहले एक चित्र खोलें, फिर दूसरा। एक जैसे चित्र खुले रहेंगे। अलग चित्र हों तो दूसरी जोड़ी आज़माएँ।', game='सवाल और विकल्प सुनें। फिर अपने चुने हुए उत्तर पर टैप करें।', sequence='घटनाओं के क्रम में चित्रों पर टैप करें। क्रम बनाने से पहले हर विकल्प सुन सकते हैं।', tidy='हर चीज़ को उसकी सही जगह रखें। जगह पर टैप करें या चीज़ खींचकर रखें।', count='गिनने के लिए हर चित्र पर एक बार टैप करें। फिर अपना उत्तर चुनें।'),
    'mr': dict(choice='पर्याय', memory='जुळणाऱ्या जोड्या शोधा. आधी एक चित्र, मग दुसरे उघडा. सारखी चित्रे उघडी राहतील. वेगळी असतील तर दुसरी जोडी शोधा.', game='प्रश्न आणि पर्याय ऐका. मग निवडलेल्या उत्तरावर टॅप करा.', sequence='घटनांच्या क्रमाने चित्रांवर टॅप करा. क्रम लावण्यापूर्वी प्रत्येक पर्याय ऐकू शकता.', tidy='प्रत्येक वस्तू तिच्या जागी ठेवा. जागेवर टॅप करा किंवा वस्तू ओढा.', count='मोजण्यासाठी प्रत्येक चित्रावर एकदा टॅप करा. मग उत्तर निवडा.')
}

SYMBOLS = {
    '●': ('circle', 'गोला', 'गोल'), '■': ('square', 'वर्ग', 'चौरस'),
    '▲': ('triangle', 'त्रिकोण', 'त्रिकोण'), '◇': ('diamond', 'हीरे का आकार', 'हिऱ्याचा आकार'),
    '★': ('star', 'तारा', 'तारा'), '☀': ('sun', 'सूरज', 'सूर्य'),
    '♡': ('heart', 'दिल', 'हृदय'), '✿': ('flower', 'फूल', 'फूल'),
    '☂': ('umbrella', 'छाता', 'छत्री'), '♬': ('music', 'संगीत', 'संगीत'),
    '🍎': ('apple', 'सेब', 'सफरचंद'), '🍌': ('banana', 'केला', 'केळे'),
    '🥭': ('mango', 'आम', 'आंबा'), '🚌': ('bus', 'बस', 'बस'),
    '👟': ('shoe', 'जूता', 'बूट'), '🌱': ('seedling', 'अंकुर', 'रोप'),
    '🌸': ('flower', 'फूल', 'फूल'), '🦋': ('butterfly', 'तितली', 'फुलपाखरू'),
    '🔺': ('triangle', 'त्रिकोण', 'त्रिकोण'), '🔵': ('blue circle', 'नीला गोला', 'निळा गोल'),
    '🟡': ('yellow circle', 'पीला गोला', 'पिवळा गोल'), '=': ('equal', 'बराबर', 'समान'),
}


def speakable(text, language):
    index = ('en', 'hi', 'mr').index(language)
    for symbol, names in SYMBOLS.items():
        text = text.replace(symbol, ' ' + names[index] + ' ')
    return ' '.join(text.replace('→', '. ').split())


def choices_text(prompt, choices, language):
    return '\n'.join([prompt, *[f"{WORDS[language]['choice']} {index + 1}. {choice}." for index, choice in enumerate(choices)]])


def activity_text(kind, item_id, language, part, question=0, option=None, level=1):
    if language not in LANGUAGES or level not in (1, 2, 3):
        raise ValueError('Unknown language or difficulty.')
    if kind == 'lessons':
        item = next((lesson for lesson in LESSONS if lesson['id'] == item_id), None)
        if not item:
            raise ValueError('Lesson not found.')
        prompt, choices = item['question'][language], item['options'][language]
        if part == 'question':
            return speakable(choices_text(prompt, choices, language), language)
        if part == 'practice' and item.get('practice'):
            return speakable(item['practice'][language], language)
    elif kind == 'games':
        if item_id not in {*BASE, 'memory'}:
            raise ValueError('Game not found.')
        if part == 'instructions':
            instruction = 'memory' if item_id == 'memory' else 'sequence' if item_id == 'sequence' else 'tidy' if item_id == 'tidy' else 'count' if item_id == 'count' else 'game'
            return WORDS[language][instruction]
        if item_id == 'memory' or question not in (0, 1, 2):
            raise ValueError('Question not found.')
        item = game_bank(item_id, level)
        prompt, choices = item['questions'][language][question]
        if part == 'question':
            visual = item.get('visuals', [None] * 3)[question]
            return speakable(choices_text(prompt + (' ' + visual if visual else ''), choices, language), language)
    else:
        raise ValueError('Activity not found.')
    if part == 'option' and type(option) is int and 0 <= option < len(choices):
        return speakable(f"{WORDS[language]['choice']} {option + 1}. {choices[option]}", language)
    raise ValueError('Reading part not found.')


def activity_requests(languages=('en', 'hi')):
    for language in languages:
        for lesson in LESSONS:
            yield dict(kind='lessons', item_id=lesson['id'], language=language, part='text')
            yield dict(kind='lessons', item_id=lesson['id'], language=language, part='question')
            if lesson.get('practice'):
                yield dict(kind='lessons', item_id=lesson['id'], language=language, part='practice')
            for option in range(len(lesson['options'][language])):
                yield dict(kind='lessons', item_id=lesson['id'], language=language, part='option', option=option)
        for game_id in [*BASE, 'memory']:
            yield dict(kind='games', item_id=game_id, language=language, part='instructions')
            for level in LEVELS.get(game_id, {}):
                for question in range(3):
                    yield dict(kind='games', item_id=game_id, language=language, part='question', level=level, question=question)
                    for option in range(len(game_bank(game_id, level)['questions'][language][question][1])):
                        yield dict(kind='games', item_id=game_id, language=language, part='option', level=level, question=question, option=option)
