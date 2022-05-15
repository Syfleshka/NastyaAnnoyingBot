#
# / Messages
#

START_MESSAGE = 'Привет, я тут для того, чтобы помочь Насте учить JavaScript'
HELP_MESSAGE = 'Я живу ради Насти, но если есть какие-то вопросы, можешь задать.\n' \
               'Просто обратись ко мне со своим вопросом. Например:\n' \
               '@kkomilfobot, какая погода сегодня?\n\n' \
               'Ещё можешь использовать слово javascript или js в вопросе, тогда я поищу информацию на learnjs\n'

#
# Dictionary for some predefined answers
#

COOL = [' классный?', ' классная?', ' классное?', ' клёвый?', ' клёвая?', ' клевый?', ' клевая?']
COOL_ANSWER = 'Да <3'

HORO = ['предскажи будущее']
HORO_ANSWER = 'Что-то было, что-то будет. Если будешь делать хуже - будет хуже. Сделаешь лучше - будет лучше.'

#
# Search
#

# SEARCH = None
SEARCH_OPTIONS = '-context.reverso.net'
SEARCH_ANSWER = '*Голосом Алисы* \nВот что я нашла:'

JS_SEARCH = ['js ', ' js', 'javascript']
JS_SEARCH_OPTIONS = 'site: https://learn.javascript.ru/'
JS_SEARCH_ANSWER = '*Голосом Алисы* \nВот что я нашла на learnjs:'

#
# Dictionary for targets
#
QUESTIONS = ['как', 'что', 'кто', 'почему', 'зачем']
QUESTIONS_OPTIONS = '-context.reverso.net'
QUESTIONS_ANSWER = 'Давай я помогу:'

BORING = ['скучн']
BORING_ANSWER = 'https://www.codewars.com/dashboard не даст тебе заскучать'

WHY = ['почему?']
WHY_ANSWER = 'по кочану.'

JOKE = ['шутк', 'шуто']
JOKE_ANSWER = 'шутка-хуютка.'

KIRKOROV = ['да', 'da', 'дa']
KIRKOROV_ANSWER = 'пизда.'

KIRKOROVMULTI = ['дадада', 'дадад', 'адада', 'ададад', 'дададад']
KIRKOROVMULTI_ANSWER = 'пиздапиздапизда.'

TRAKTORIST = ['300', 'триста', 'тристо', 'три сотни']
TRAKTORIST_ANSWER = 'вам надо бы зайти на приём к трактористу.'

WHO_EASY = ['изи', 'та изи']
WHO_EASY_ANSWER = 'хуизи.'

PIDOR = ['нет', 'нет.']
PIDOR_ANSWER = 'пидора ответ.'

ULTRAPIDOR = ['та нет', 'та нет.']
ULTRAPIDOR_ANSWER = 'та пидора ответ.'

KIRKOROV_PIDOR = ['да нет', 'да нет.']
KIRKOROV_PIDOR_ANSWER = 'и всё же пидора ответ.'

PROMISE = ['ты обещал']
PROMISE_ANSWER = 'к сожалению сегодня обещавший занят, попробуй в другой день.'

SIGN = ['?']
SIGN_ANSWER = '!'

SMILEY = ['👀']
SMILEY_ANSWER = 'не подглядывай'

SORRY = ['обидно', 'жаль', 'ну блин', '...']
SORRY_ANSWER = 'это всё потому что ты ленивая жопа'

BEE = ['жалко']
BEE_ANSWER = 'жалко у пчёлки, а мы наказываем, жестоко наказываем'