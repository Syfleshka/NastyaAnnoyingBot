import logging

import requests
import telebot
from googlesearch import search

from API_INFO import KEY
from CONFIG import *

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)
bot = telebot.TeleBot(KEY)

# reset bot at every start to prevent spam
requests.get('https://api.telegram.org/bot' + KEY + '/getUpdates?offset=-1')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, START_MESSAGE)


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, HELP_MESSAGE)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    message_text = message.text.replace(f'@{BOTNAME}', "")
    print(message)
    if f'@{BOTNAME}' in message.text:
        if message.text != f'@{BOTNAME}':
            print(message_text)
            if any([i in message.text.lower() for i in COOL]) and (message.from_user.username not in TARGETS):
                bot.reply_to(message, 'Да <3')
            elif any([i in message.text.lower() for i in HORO]) and (message.from_user.username not in TARGETS):
                bot.reply_to(message, 'Что-то было, что-то будет.'
                                      ' Если будешь делать хуже - будет хуже. Сделаешь лучше - будет лучше.')
            elif any([i in message.text.lower() for i in JS_SEARCH]):
                for searchResult in search(f'{message_text} site: https://learn.javascript.ru/',
                                           tld="co.in", num=1, stop=1, pause=2):
                    bot.reply_to(message, "*Голосом Алисы* \nВот что я нашла на learnjs: " + searchResult,
                                 disable_web_page_preview=True)
            else:
                for searchResult in search(f'{message_text} -context.reverso.net', tld="co.in", num=1, stop=1,
                                           pause=2):
                    bot.reply_to(message, "*Голосом Алисы* \nВот что я нашла: " + searchResult,
                                 disable_web_page_preview=True)
    elif message.from_user.username in TARGETS:
        message.text.replace(f'@{BOTNAME}', "")
        # Checking for question
        if any([i in message.text.lower() for i in QUESTIONS]) \
                and '?' in message.text.lower() \
                and message.from_user.username in TARGET:
            for search_result in search(f'{message_text} -context.reverso.net', tld="co.in", num=1, stop=1,
                                        pause=2):
                bot.send_message(message.chat.id, f'@{message.from_user.username}, давай я помогу: {search_result}',
                                 disable_web_page_preview=True)
                # bot.send_message(message.chat.id, f'@{message.from_user.username},'
                # f'прости, не могу ничем помочь, мне за это не заплатят.')

        # Checking for boring
        elif any([i in message.text.lower() for i in BORING]):
            bot.send_message(message.chat.id, f'@{message.from_user.username}'
                                              f', https://www.codewars.com/dashboard не даст тебе заскучать',
                             disable_web_page_preview=True)

        # Checking for why question
        elif any([i == message.text.lower() for i in WHY]):
            bot.send_message(message.chat.id, f'@{message.from_user.username}, по кочану.')

        # Checking for stupid joke
        elif any([i in message.text.lower() for i in JOKE]):
            bot.send_message(message.chat.id, f'@{message.from_user.username}, шутка-хуютка.')

        # Kirkorov answer
        elif any([len(set(i) ^ set(message.text.lower())) == 0 for i in KIRKOROV]):
            bot.send_message(message.chat.id, f'@{message.from_user.username}, пизда.')

        # KIRKOROVMULTI answer
        elif any([i == message.text.lower() for i in KIRKOROVMULTI]):
            bot.send_message(message.chat.id, f'@{message.from_user.username}, пиздапиздапизда.')

        # TRAKTORIST answer
        elif any([i == message.text.lower() for i in TRAKTORIST]):
            bot.send_message(message.chat.id,
                             f'@{message.from_user.username}, вам надо бы зайти на приём к трактористу.')

        # who easy answer
        elif any([i == message.text.lower() for i in WHY_EASY]):
            bot.send_message(message.chat.id, f'@{message.from_user.username}, хуизи.')

        # pidor answer
        elif any([len(set(i) ^ set(message.text.lower())) == 0 for i in PIDOR]):
            bot.send_message(message.chat.id, f'@{message.from_user.username}, пидора ответ.')

        # ultrapidor answer
        elif any([i == message.text.lower() for i in ULTRAPIDOR]):
            bot.send_message(message.chat.id, f'@{message.from_user.username}, та пидора ответ.')

        # KIRKOROV_PIDOR answer
        elif any([i == message.text.lower() for i in KIRKOROV_PIDOR]):
            bot.send_message(message.chat.id, f'@{message.from_user.username}, и всё же пидора ответ.')

        # promise check
        elif any([i in message.text.lower() for i in PROMISE]):
            bot.send_message(message.chat.id, f'@{message.from_user.username}'
                                              f', к сожалению сегодня обещавший занят, попробуй в другой день.')

        # annoying stripped question mark check
        elif any([i == message.text.lower() for i in SIGN]):
            bot.reply_to(message, f'!')

        # 👀
        elif any([i in message.text.lower() for i in SMILEY]):
            bot.reply_to(message, f' не подглядывай')

        # Добавить функцию, когда Настя говорит что что-то знает (исключаем не из строки)
        # бот задаёт вопрос по JS "знаешь <Оператор>", надо написать список опреаторов


bot.infinity_polling()
