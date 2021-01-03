import sys
import time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent
from twilio.rest import Client

account_ssd = "AC9a91106e66d05bae7ffafa9954deeaa7"
auth_token = "5415f62d4bda17f072ad274a4d56e34e"
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
        responce = bot.getChat(chat_id)
        global first_name
        global user_name
        global user_id
        global c_type
        global bio
        first_name = responce['first_name']
        user_name = responce['username']
        bot.sendChatAction(chat_id, 'typing')
        user_id = responce['id']
        user_name = responce['username']
        c_type = responce['type']
        bio = responce['bio']
        markup2 = ReplyKeyboardMarkup(keyboard=[['🔰accept and proceed'],], resize_keyboard=True)
        bot.sendPhoto(chat_id, photo="https://images.app.goo.gl/joSrXdbBYpesQt7o6", caption=f'<b>Hello {first_name}!</b> {user_id} \nMSG91 is a cloud communication platform that offers powerful messaging solutions to empower business communications. It consists of 10+ channels across the platform offering services over SMS.',parse_mode='html', reply_markup=markup2)
    if command == '🔰accept and proceed' or command == 'a':
        markup = ReplyKeyboardRemove()
        bot.sendMessage(chat_id,'<b>Text:</b> for recipient:', parse_mode='html',reply_markup=markup)
        



    
    
TOKEN = '1464378098:AAHDrhYK91mP0m7FlMQL9qZPKR-jr6z0_kw'
# your token
bot = telepot.Bot(TOKEN)
answerer = telepot.helper.Answerer(bot)

MessageLoop(bot, {'chat': on_chat_message}).run_as_thread()
print('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)







#if command != '/start':
        #value = googlesearch.search(f'{command}', lang='en')
        #photo_url_from_google = value[0]
        #try:
            #wikipedia.set_lang("en")
            #s1 = wikipedia.search(f'{command}')
            #value = s1[0]
            #title = str(value)
            #t1 = wikipedia.summary(f'{title}', sentences=3)
            #bot.sendPhoto(chat_id,photo=f'{str(photo_url_from_google)}',caption=f'{command}',reply_markup=None)
        #except Exception:
            #wikipedia.set_lang("en")
            #s5 = wikipedia.search(f'{command}')
            #v1 = s5[0]
            #t2 = str(v1)
            #sm = wikipedia.summary(f'{t2}', sentences=3)
            #try:
                #photo_url_from_wiki = wikipedia.page(command).url
                #bot.sendPhoto(chat_id,photo=f'{str(photo_url_from_wiki)}',caption=f'{command}',reply_markup=None)
           # except :
               # bot.sendMessage(chat_id,'False',reply_markup=None)
   # else:
       # pass
          