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
    rep = f"**Hi {message.from_user.username}**\n\nAm a bot to __convert text into Shareable telegram link__.\nWorks on both **pm and in Inline😊**\n\nClick /help if needed.."
    message.reply_text(
        text=rep, 
        quote=False,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('SOURCE', url='https://github.com/ashkar2001')],[InlineKeyboardButton("Search Here", switch_inline_query_current_chat=""),InlineKeyboardButton("Go Inline", switch_inline_query="")]]))

@bot.on_message(filters.command(['help']))
def help(client, message):
    message.reply_text("**Nothing Complicated..🤓**\n\n**For PM:**\n__Send your desired text to this bot to get your link.__\n\n**For Inline Method:**\n__Type__  `@ShareUrlBot your text`\n__in any chats keyboard and hit the inline result.__")

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
**DC ID** :- `{message.from_user.dc_id}`""")


@bot.on_message(filters.text)
def shareurl(client, message):
    query = message.text
    url = urllib.parse.quote(query)
    rpl = f"https://t.me/share/url?url={url}"
    rslt = f"""**Click to CopY⬇️⬇️** \n\n```{rpl}```"""
    message.reply_text(text=rslt, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Click to Try on This Link ⬆️⬆️', url=f'{rpl}')]]))

@bot.on_inline_query()
def inline(client, message): 
  query = message.query.lower()
  if query == "":
        result= [InlineQueryResultArticle(title = "How to use Meh!!",
                     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Search Here", switch_inline_query_current_chat=""),InlineKeyboardButton("Go Inline", switch_inline_query="")]]),
                     description ="Help !!",
                     thumb_url="https://telegra.ph/file/99d8f16a777c2ee2781c1.jpg",
                     input_message_content = InputTextMessageContent(disable_web_page_preview=1,message_text ="**Nothing Complicated..**🤓\n\nType `@ShareUrlBot your text` \nin any chats keyboard and hit the inline result.\n\nNote: __U can also use Me in PM!__"))
                ] 
        message.answer(result) 
        return
  else:
     url = urllib.parse.quote(query)
     rpl = f"https://t.me/share/url?url={url}"
     rslt = f"""**Click to CopY⬇️⬇️** \n\n```{rpl}```"""
     result = [InlineQueryResultArticle(title = f'{query}',
               description =f'{rpl}',                        
               reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Click to Try on This linK ⬆️⬆️', url=f'{rpl}')]]),
               input_message_content = InputTextMessageContent(disable_web_page_preview=0,message_text = rslt))
              ]
  
  message.answer(result)

bot.run()
