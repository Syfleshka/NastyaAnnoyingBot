import logging
import requests
import telebot
import re

from googlesearch import search

from API_INFO import KEY
from CONFIG import *
from DICTIONARY import *

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)
bot = telebot.TeleBot(KEY)

# Reset bot at every start to prevent spam
requests.get('https://api.telegram.org/bot' + KEY + '/getUpdates?offset=-1')

#
# Message send functions
#


def send_mention(message, answer_text):
    bot.send_message(message.chat.id,
                     f'@{message.from_user.username},'
                     f' {answer_text}',
                     disable_web_page_preview=True)


def send_reply(message, answer_text):
    bot.reply_to(message, answer_text, disable_web_page_preview=True)


def send_search_result(message, message_text, add_search_args, answer_text):
    for searchResult in search(f'{message_text} {add_search_args}', tld="co.in", num=1, stop=1, pause=2):
        bot.reply_to(message, f'{answer_text} {searchResult}', disable_web_page_preview=True)

#
# Message check functions
#


def check_in(message_text, check_array):
    return any([i in message_text.lower() for i in check_array])


def check_equals(message_text, check_array):
    return any([i == message_text.lower() for i in check_array])


def check_set(message_text, check_array):
    return any([len(set(i) ^ set(message_text.lower())) == 0 for i in check_array])


def not_in_restricted_names(message, targets):
    return message.from_user.username not in targets

#
# Handler
#


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    message_text = message.text.replace(f'@{BOT_NAME}', '')

    stripped_message_text = re.sub(' ', '', message_text)
    stripped_message_text = re.sub('"', '', stripped_message_text)
    stripped_message_text = re.sub(rf"[.':,!@#№;%?*$^&()_]", '', stripped_message_text)
    stripped_message_text = re.sub(r"\d+", "", stripped_message_text)

    # Commands
    if f'/start@{BOT_NAME}' == message.text:
        return send_reply(message, START_MESSAGE)

    if f'/help@{BOT_NAME}' == message.text:
        return send_reply(message, HELP_MESSAGE)

    # Some logs
    print(message)
    print(message_text)

    # Work with user requests
    if f'@{BOT_NAME}' in message.text:

        # First check for predefined phrases
        if message_text != '' and not_in_restricted_names(message, TARGETS):
            if check_in(message_text, COOL):
                return send_reply(message, COOL_ANSWER)
            if check_in(message_text, HORO):
                return send_reply(message, HORO_ANSWER)

        # Search
        if message_text != '':
            if check_in(message_text, JS_SEARCH):
                return send_search_result(message, message_text, JS_SEARCH_OPTIONS, JS_SEARCH_ANSWER)
            else:
                return send_search_result(message, message_text, SEARCH_OPTIONS, SEARCH_ANSWER)

    elif message.from_user.username in TARGETS:
        # Checking for question
        if check_in(message_text, QUESTIONS) and ('?' in message_text.lower()) and (len(message_text) > 7):
            return send_search_result(message, message_text, QUESTIONS_OPTIONS, QUESTIONS_ANSWER)

        # Checking for boring
        if check_in(message_text, BORING):
            return send_mention(message, BORING_ANSWER)

        # Checking for why question
        if check_equals(message_text, WHY):
            return send_mention(message, WHY_ANSWER)

        # Checking for stupid joke
        if check_in(message_text, JOKE):
            return send_mention(message, JOKE_ANSWER)

        # KIRKOROVMULTI answer
        if check_equals(message_text, KIRKOROVMULTI):
            return send_mention(message, KIRKOROVMULTI_ANSWER)

        # Kirkorov answer
        if check_set(stripped_message_text, KIRKOROV):
            return send_mention(message, KIRKOROV_ANSWER)

        # TRAKTORIST answer
        if check_equals(message_text, TRAKTORIST):
            return send_mention(message, TRAKTORIST_ANSWER)

        # who easy answer
        if check_in(message_text, WHO_EASY) and (len(message_text) < 7):
            return send_mention(message, WHO_EASY_ANSWER)

        # pidor answer
        if check_set(stripped_message_text, PIDOR):
            return send_mention(message, PIDOR_ANSWER)

        # ultrapidor answer
        if check_equals(message_text, ULTRAPIDOR):
            return send_mention(message, ULTRAPIDOR_ANSWER)

        # KIRKOROV_PIDOR answer
        if check_equals(message_text, KIRKOROV_PIDOR):
            return send_mention(message, KIRKOROV_PIDOR_ANSWER)

        # promise check
        if check_in(message_text, PROMISE):
            return send_mention(message, PROMISE_ANSWER)

        # annoying stripped question mark check
        if check_equals(message_text, SIGN):
            return send_mention(message, SIGN_ANSWER)

        # 👀
        if check_in(message_text, SMILEY):
            return send_mention(message, SMILEY_ANSWER)

        # Добавить функцию, когда Настя говорит что что-то знает (исключаем не из строки)
        # бот задаёт вопрос по JS "знаешь <Оператор>", надо написать список операторов


bot.infinity_polling()
