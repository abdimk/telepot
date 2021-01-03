#@autor abdisa merga date 1/3/2/2021
#          2021all rights reserved




import sys
import time
import telepot
import googlesearch
import wikipedia
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent


# start of online server proxy config

import urllib3
import telepot.api
proxy_url = 'http://proxy.server:3128'

telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30), }

telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1,
                                                             retries=False, timeout=30))

# end of online server proxy config


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print('Chat:', content_type, chat_type, chat_id)
    command = msg['text'].lower()
    if command == '/start':
        markup = InlineKeyboardMarkup(inline_keyboard=[[dict(text='☂️Github', url='https://t.me/abdisamerga/'),dict(text='Switch inline', switch_inline_query='initial query')],[]])
        responce = bot.getChat(chat_id)
        first_name = responce['first_name']
        bot.sendMessage(chat_id,f'Hello <b>{first_name}! </b> Botisfy is a web-based tool that enables users to search information on the World Wide Web. <b>search specific phrase</b> like <code>cat</code>',parse_mode='html', reply_markup=markup)
    if command != '/start':
        vd = googlesearch.search(f'{command}', lang='en')
        try:
            photo_url_from_google = vd[0]
        except:
            pass
        try:
            wikipedia.set_lang("en")
            var = wikipedia.search(f'{command}')
            try:
                value = var[0]
            except IndexError:
                bot.sendMessage(chat_id,f'opps! Your search-<b>{command}</b> did not match any documents.',parse_mode='html',reply_markup=None)
            title = str(value)
            try:
                lan = wikipedia.summary(f'{title}', sentences=3,auto_suggest=False, redirect=False)
            except:
                lan = wikipedia.summary(f'{title}', sentences=3,auto_suggest=True, redirect=True)
            bot.sendPhoto(chat_id,photo=f'{str(photo_url_from_google)}',caption=f'{lan}',reply_markup=None)
        except Exception:
            wikipedia.set_lang("en")
            var2 = wikipedia.search(f'{command}')
            global value2
            try:
                value2 = var2[0]
            except (IndexError,UnboundLocalError,NameError):
                pass
            title2 = str(value2)
            try:
                lan2 = wikipedia.summary(f'{title2}', sentences=3,auto_suggest=False, redirect=False)
            except:
                lan2 = wikipedia.summary(f'{title2}', sentences=3,auto_suggest=True, redirect=True)
            try:
                photo_url_from_wiki = wikipedia.page(title2).url
                bot.sendPhoto(chat_id,photo=f'{str(photo_url_from_wiki)}',caption=f'{lan2}',reply_markup=None)
            except (wikipedia.exceptions.PageError,wikipedia.exceptions.DisambiguationError,wikipedia.DisambiguationError):
                bot.sendMessage(chat_id,f'{lan2}',reply_markup=None)

def on_inline_query(msg):
    query_id, from_id, query_string = telepot.glance(msg, flavor='inline_query')
    print ('Inline Query:', query_id, from_id, query_string)

    wikipedia.set_lang("en")
    query_var = wikipedia.search(f'{query_string}')
    query_value = query_var[0]
    query_title = str(query_value)
    zvalue = googlesearch.search(f'{query_string}', lang='en')
    try:
        query_photo_url= zvalue[0]
    except:
        query_photo_url = wikipedia.page(f'{query_string}').url
    try:
        qlan2 = wikipedia.summary(f'{query_title}', sentences=2,auto_suggest=False, redirect=False)
    except:
        qlan2 = wikipedia.summary(f'{query_title}', sentences=2,auto_suggest=True, redirect=True)

    articles = [InlineQueryResultArticle(id='abc',title=f'{query_string}',input_message_content=InputTextMessageContent(message_text=f'{qlan2}'))]
    photos = [InlineQueryResultPhoto(id='12345', photo_url=query_photo_url, thumb_url=query_photo_url)]

    bot.answerInlineQuery(query_id, articles,photos)

def on_chosen_inline_result(msg):
    result_id, from_id, query_string = telepot.glance(msg, flavor='chosen_inline_result')
    print ('Chosen Inline Result:', result_id, from_id, query_string)




TOKEN = '1411149304:AAHpVyGm5sHnS9Thwga5V_agOPofPBYO6qY'
# your token
bot = telepot.Bot(TOKEN)
answerer = telepot.helper.Answerer(bot)

MessageLoop(bot, {'inline_query': on_inline_query,'chosen_inline_result': on_chosen_inline_result,'chat': on_chat_message,}).run_as_thread()
print('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
