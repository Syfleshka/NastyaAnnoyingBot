import telebot
import logging
from googlesearch import search

from CONFIG import KEY, TARGET

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)
bot = telebot.TeleBot(KEY)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
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
                                 + ", давай я тебе помогу: " + searchResult)
        elif ("Скуко" in message.text
              or "скуко" in message.text):
            bot.send_message(message.chat.id,
                             "@" + message.from_user.username
                             + ", с https://www.codewars.com/dashboard тебе будет не так скучно.")
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
                             + searchResult)
    elif message.text == "/help":
        bot.send_message(message.chat.id,
                         "@" + message.from_user.username
                         + ", я живу ради Насти, но если есть какие-то вопросы, можешь задать, обратившись ко мне")


bot.polling(none_stop=True, interval=0)
