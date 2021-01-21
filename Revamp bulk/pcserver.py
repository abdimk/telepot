import sys
import time
import requests
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent

# start of online server proxy config
'''
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
        markup = InlineKeyboardMarkup(inline_keyboard=[[dict(text='☂Developer', url='https://t.me//paperExtend')],[]])
        responce = bot.getChat(chat_id)
        first_name = responce['first_name']
        bot.sendMessage(chat_id,f'Hello <b>{first_name}! </b> RevampBulk is a popular bulk SMS service provider. Famous for its performance driven messaging services, you can expect a <b>high quality SMS services from us</b>.send sms like <code>251931167494|hello world</code>',parse_mode='html', reply_markup=markup)
    if command !='/start':
        if len(command.split('|')) != 2:
            bot.sendMessage(chat_id,"invalid message")
        else:
            msg = f'{command}'
            value = msg.split('|')
            if value[0]:
                phone_no = value[0]
                message = value[1]
                resp = requests.post('https://www.freebulksmsonline.com/api/v1/index.php', {'number': f'{phone_no}','message': f'{message}','token': '117e4cee73fcf7e190937e2efae83b3c',})
                jas = resp.json()
                if jas['success'] =='true':
                    a = jas['success']
                    b = jas['status']
                    c = jas['id']
                    d = jas['number']
                    e = jas['created_at']
                    f = jas['msg_status']
                    g = jas['user_limit']
                    bot.sendMessage(chat_id,f'''
<b>success</b>: {a}
<b>status</b>: {b}
<b>id</b>: {c}
<b>number</b>: {d}
<b>created</b>: {e}
<b>msg_status</b>: {f}
<b>user_limit</b>: {g}
                    ''',parse_mode='html', reply_markup=None)
                    if jas['success'] =='false':
                    	stoken = 'f4127486758c4986a91764f980454fe5'
                    	resp = requests.post('https://www.freebulksmsonline.com/api/v1/index.php', {'number': f'{phone_no}','message': f'{message}','token': f'{stoken}',})
                    	bot.sendMessage(chat_id,f'''
<b>success</b>: {a}
<b>status</b>: {b}
<b>id</b>: {c}
<b>number</b>: {d}
<b>created</b>: {e}
<b>msg_status</b>: {f}
<b>user_limit</b>: {g}
                    ''',parse_mode='html', reply_markup=None)

    


            

TOKEN = '1533671037:AAG1qKMJJgloFSbBVS-A6uGVaVpB9bNinXg'
# your token
bot = telepot.Bot(TOKEN)
answerer = telepot.helper.Answerer(bot)

MessageLoop(bot, {'chat': on_chat_message,}).run_as_thread()
print('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
