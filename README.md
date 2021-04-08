# shareurlbotv1
https://heroku.com/deploy?template=https://github.com/ashkar2001/shareurlbotv1


## Installation

### Deploy in your VPS

Clone the repository:

```sh
git clone https://github.com/ashkar2001/shareurlbotv1
cd shareurlbotv1
```

Install dependencies

```sh
pip3 install -r requirements.txt
```
Create config.py file with required variables
Example:
```python 3
class Config:
    BOT_TOKEN = "1242918832:AAFQhNnkmx61J-VfMaQBG78oXLAIg12K958"
    API_ID = 1234567
    API_HASH = "36de51fd24d20Byj9zq60eJ8F0"
```
Run the bot
```python 3
python3 main.py
```
