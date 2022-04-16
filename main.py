import logging
from pathlib import Path
import requests

import telebot
from googlesearch import search

from API_INFO import KEY

if Path("CONFIG.py").exists():
    from CONFIG import *
else:
    from CONFIG_DEF import *

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
    print(message)
    if message.from_user.username == TARGET:
        if ('Как' in message.text
                or 'А как' in message.text
                or 'Что' in message.text
                or 'Для' in message.text
                or 'И как' in message.text
                and '?' in message.text):
            for searchResult in search(message.text, tld="co.in", num=1, stop=1, pause=2):
                bot.send_message(message.chat.id,
                                 "@" + message.from_user.username
                                 + ", давай я тебе помогу: " + searchResult,
                                 disable_web_page_preview=True)
        elif ("Скучн" in message.text
              or "скучн" in message.text):
            bot.send_message(message.chat.id,
                             "@" + message.from_user.username
                             + ", https://www.codewars.com/dashboard не даст тебе заскучать.",
                             disable_web_page_preview=True)
        elif ("Шутка" in message.text
              or "шутка" in message.text
              or "Шутки" in message.text
              or "шутки" in message.text
              or "Шуток" in message.text
              or "шуток" in message.text):
            bot.send_message(message.chat.id,
                             "@" + message.from_user.username
                             + ", шутка-хуютка.")
        elif ("Да" == message.text
              or "да" == message.text
              or "Да." == message.text
              or "да." == message.text):
            bot.send_message(message.chat.id,
                             "@" + message.from_user.username
                             + ", пизда.")
        elif ("Нет" == message.text
              or "нет" == message.text
              or "Нет." == message.text
              or "нет." == message.text):
            bot.send_message(message.chat.id,
                             "@" + message.from_user.username
                             + ", пидора ответ.")
        elif ("Ты обещал" in message.text
              or "ты обещал" in message.text):
            bot.send_message(message.chat.id,
                             "@" + message.from_user.username
                             + ", к сожалению сегодня обещавший занят, попробуй в другой день.")
    elif '@kkomilfobot' in message.text:
        if message.text != '@kkomilfobot':
            if 'Влад классный?' in message.text:
                bot.reply_to(message, 'Да <3')
            else:
                for searchResult in search(message.text, tld="co.in", num=1, stop=1, pause=2):
                    bot.reply_to(message, "*Голосом Алисы \nВот что я нашла: " + searchResult,
                                 disable_web_page_preview=True)


bot.polling(none_stop=True, interval=0)
