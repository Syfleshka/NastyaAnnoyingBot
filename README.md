# NastyaAnnoyingBot
## Telegram Annoying bot[^tgbotadv]

Created specially for https://t.me/+R0wbqoHzEd5kMjgy

Thanks to @kkomilfo

## Setup bot

Create `API_INFO.py` in root directory and add your telegram bot key[^tgbot]
```python
KEY = 'YOUR:TELEGRAM:BOT:KEY'
```



## Bot config

`CONFIG.py`
```python
# Your target's username, without @
TARGET = 'kkomilfo'

# Your bot username, without @
BOTNAME = 'kkomilfobot'

# Default start and help Messages
START_MESSAGE = 'TEXT'
HELP_MESSAGE = 'TEXT'

# Triggers as arrays
QUESTIONS = ['TRIGGER', 'TRIGGER']
BORING = ['TRIGGER']
# ...
```

[^tgbotadv]: Make your own bot with [Telegram Bot API](https://core.telegram.org/bots/api)
[^tgbot]: To get your own bot key use guide: [EN](https://core.telegram.org/bots), [RU](https://habr.com/ru/post/262247/)
