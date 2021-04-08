# ShareURLbotV1 😋
A Telegram bot to convert Text as a shareable text link format..🤗

###### Features

- Easy Accessible
- Works in Chat and in Inline
- Supports emoji
- Compatible

## Installation

### Deploy to Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/ashkar2001/shareurlbotv1)

### Deploy in your VPS

Clone the repository:

```sh
git clone https://github.com/ashkar2001/shareurlbotv1
cd shareurlbotv1
```

Install dependencies:

```
pip3 install -r requirements.txt
```
Create config.py file with required variables.

Example:
```python 3
class Config:
    BOT_TOKEN = "1242918832:AAFQhNnkmx61J-VfMaQBG78oXLAIg12K958"
    API_ID = 1234567
    API_HASH = "36de51fd24d20Byj9zq60eJ8F0"
```
Run the bot:
```
python3 main.py
```

## Configs

* `API_HASH` Your API Hash from my.telegram.org
* `API_ID` Your API ID from my.telegram.org
* `BOT_TOKEN` Your bot token from @BotFather
