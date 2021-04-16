import urllib
from pyrogram import Client, filters
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent)
from config import Config

bot = Client(
    'shareurl-generator',
    bot_token = Config.BOT_TOKEN,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH
)


@bot.on_message(filters.command(['start']))
def start(client, message):
    rep = f"**Hi {message.from_user.username}**\n\n**Am a bot to convert __text into Shareable telegram link__.**\nWorks on both **in pm and in Inline😊**\n\nClick __/help__ if needed.."
    message.reply_text(
        text=rep, 
        quote=False,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('SOURCE', url='https://github.com/ashkar2001/shareurlbotv1')],[InlineKeyboardButton("Search Here", switch_inline_query_current_chat=""),InlineKeyboardButton("Go Inline", switch_inline_query="")], [InlineKeyboardButton('Share Me', url='https://t.me/share/url?url=%2A%2AHello%20Plox%20%F0%9F%91%8B%2A%2A%0A%0A__I%20just%20found%20a%20Bot%20to%20convert__%20%2A%2AText%20as%20a%20Shareable%20Text%20Link%2A%2A%20__format%20%F0%9F%A4%A9.%20Hope%20it%20would%20be%20very%20helpful%20for%20u%20too...%F0%9F%A4%97%F0%9F%A4%97__%0A%0A%2A%2ABot%20Link%3A%20%40ShareUrlBot%20%F0%9F%A5%B0%2A%2A')]]))

@bot.on_message(filters.command(['help']))
def help(client, message):
    message.reply_text("**Nothing Complicated..🤓**\n\n**For PM:**\n__Send your desired text to this bot to get your link.__\n\n**For Inline Method:**\n__Type__  `@ShareUrlBot your text`\n__in any chats keyboard and hit the inline result.__", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('SOURCE', url='https://github.com/ashkar2001/shareurlbotv1')]]))

@bot.on_message(filters.command(['about']))
def about(client, message):
    message.reply_text(f"""**• Bot Info •**
**My Name** :- `Share Url Generator`
**Creator** :- @B_woy
**Language** :- `Python3`
**Library** :- `Pyrogram 1.2.8`
**Server** :- `Heroku.com`
**Build Status** :- `V 0.2`

**• User Info •**
**Name** :- `{message.from_user.first_name} {message.from_user.last_name}`
**ID** :- `{message.from_user.id}`
**Username** :- @{message.from_user.username}
**DC ID** :- `{message.from_user.dc_id}`""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('SOURCE', url = 'https://github.com/ashkar2001/shareurlbotv1')]]))


@bot.on_message(filters.text)
def shareurl(client, message):
    query = message.text
    url = urllib.parse.quote(query)
    rpl = f"https://t.me/share/url?url={url}"
    rslt = f"""**Click to CopY ⬇️⬇️** \n\n```{rpl}```"""
    message.reply_text(text=rslt, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Click to Try on This Link ⬆️⬆️', url=f'{rpl}')]]))

@bot.on_inline_query()
def inline(client, message): 
  query = message.query.lower()
  if query == "":
        result= [InlineQueryResultArticle(title = "How to use Meh!!",
                     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Search Here", switch_inline_query_current_chat=""),InlineKeyboardButton("Go Inline", switch_inline_query="")]]),
                     description ="Help !!",
                     thumb_url="https://telegra.ph/file/99d8f16a777c2ee2781c1.jpg",
                     input_message_content = InputTextMessageContent(message_text ="**Nothing Complicated..**🤓\n\nType `@ShareUrlBot your text` \nin any chats keyboard and hit the inline result.\n\nNote: __U can also use Me in PM!__"))
                ] 
        message.answer(result) 
        return
  else:
     url = urllib.parse.quote(query)
     rpl = f"https://t.me/share/url?url={url}"
     rslt = f"""**Click to CopY⬇️⬇️** \n\n```{rpl}```"""
     result = [InlineQueryResultArticle(title = f'{query}',
               description =f'{rpl}',                        
               reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Click to Try on This linK ⬆️⬆️', url=f'{rpl}')], [InlineKeyboardButton("Search Again", switch_inline_query_current_chat=""),InlineKeyboardButton("Go Inline", switch_inline_query="")]]),
               input_message_content = InputTextMessageContent(message_text = rslt))
              ]
  
  message.answer(result)

bot.run()
