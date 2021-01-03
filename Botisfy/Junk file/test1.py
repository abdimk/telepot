import sys
import time
import telepot
import google
import wikipedia
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent

'''
# start of online server proxy config

import urllib3
import telepot.api
proxy_url = 'http://proxy.server:3128'

telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30), }

telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1,
                                                             retries=False, timeout=30))

# end of online server proxy config
'''

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
        value = google.search(f'{command}', lang='en')
        photo_url_from_google = value[0]
        try:
            wikipedia.set_lang("en")
            s1 = wikipedia.search(f'{command}')
            value = s1[0]
            title = str(value)
            t1 = wikipedia.summary(f'{title}', sentences=3)
            bot.sendPhoto(chat_id,photo=f'{str(photo_url_from_google)}',caption=f'{t1}',reply_markup=None)
        except Exception:
            wikipedia.set_lang("en")
            s5 = wikipedia.search(f'{command}')
            v1 = s5[0]
            t2 = str(v1)
            sm = wikipedia.summary(f'{t2}', sentences=3)
            try:
                photo_url_from_wiki = wikipedia.page(t2).url
                bot.sendPhoto(chat_id,photo=f'{str(photo_url_from_wiki)}',caption=f'{sm}',reply_markup=None)
            except (wikipedia.exceptions.PageError,wikipedia.exceptions.DisambiguationError,wikipedia.DisambiguationError):
                bot.sendMessage(chat_id,f'{sm}',reply_markup=None)
            else:
                l = wikipedia.search(f'{command}')
                v1 = l[2]
                jm = str(v1)
                c = wikipedia.summary(f'{jm}', sentences=3)
                bot.sendMessage(chat_id,f'{c}',reply_markup=None)





TOKEN = '1411149304:AAHpVyGm5sHnS9Thwga5V_agOPofPBYO6qY'
# your token
bot = telepot.Bot(TOKEN)
answerer = telepot.helper.Answerer(bot)

MessageLoop(bot, {'chat': on_chat_message}).run_as_thread()
print('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
