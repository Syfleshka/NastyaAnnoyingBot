from API_INFO import KEY
from CONFIG import *

import telebot
import logging
from googlesearch import search

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)
bot = telebot.TeleBot(KEY)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, START_MESSAGE)


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, HELP_MESSAGE)


@bot.message_handler(HANDLER_OPTIONS)
def get_text_messages(message):
    print(message)
    if message.from_user.username == TARGET:
        if "Как начать" in message.text:
            bot.send_message(message.chat.id,
                             "@" + message.from_user.username
                             + ", серьёзно? Никак.")
        elif ('Как' in message.text
              or 'А как' in message.text
              or 'А ' in message.text
              and '?' in message.text):
            for searchResult in search(message.text, tld="co.in", num=1, stop=1, pause=2):
                bot.send_message(message.chat.id,
                                 "@" + message.from_user.username
                                 + ", давай я тебе помогу: " + searchResult, 'disable_web_page_preview')
        elif "скучно" in message.text:
            bot.send_message(message.chat.id,
                             "@" + message.from_user.username
                             + ", с https://www.codewars.com/dashboard тебе будет не так скучно.",
                             'disable_web_page_preview')
        elif ("Шутка" in message.text
              or "шутка" in message.text):
            bot.send_message(message.chat.id,
                             "@" + message.from_user.username
                             + ", шутка-хуютка.")
        elif ("Шутки" in message.text
              or "шутки" in message.text):
            bot.send_message(message.chat.id,
                             "@" + message.from_user.username
                             + ", шутки-хуютки.")
        elif ("Шуток" in message.text
              or "шуток" in message.text):
            bot.send_message(message.chat.id,
                             "@" + message.from_user.username
                             + ", шуток-хуюток.")

    elif '@kkomilfobot' in message.text:
        for searchResult in search(message.text, tld="co.in", num=1, stop=1, pause=2):
            bot.send_message(message.chat.id,
                             "*Голосом Алисы \n"
                             + "@" + message.from_user.username
                             + ", вот что я нашла: "
                             + searchResult, 'disable_web_page_preview')


bot.polling(none_stop=True, interval=0)
