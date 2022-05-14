# NastyaAnnoyingBot
## Telegram Annoying bot[^tgbotadv]

Created specially for https://t.me/+bEubmjYw3jo0N2M6

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
# ...
```

`DICTIONARY.py`
```python
# Dictionary file for bot

# / messages
START_MESSAGE = 'Hello'
HELP_MESSAGE = 'I can Help you'

# All other messages.
NAME = ['Array']
NAME_ANSWER = 'String'

# Search options
SEARCH = 'String or None, if unused'
SEARCH_OPTIONS = 'String, will be added to the end of search query'
SEARCH_ANSWER = 'String, will be added before result link'
# ...
```

[^tgbotadv]: Make your own bot with [Telegram Bot API](https://core.telegram.org/bots/api)
[^tgbot]: To get your own bot key use guide: [EN](https://core.telegram.org/bots), [RU](https://habr.com/ru/post/262247/)
