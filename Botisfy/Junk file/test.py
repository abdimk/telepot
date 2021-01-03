import telepot
import time
import threading
import random
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
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

def fileShareFunction(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        message = msg['text']
        value = []
        for items in message:
            value.append(items)

        words = ''.lower()
        for first in value[0:5]:
            words += first

        http = ''
        for word in value[0:4]:
            http += word

        back_slash = ''
        for slash in value[5:8]:
            back_slash += slash

        if words == 'https' or back_slash == '://' or http == 'http':
            photo_ur = msg['text']
            markup2 = InlineKeyboardMarkup(
                inline_keyboard=[[dict(text='🦋lINK', url=f'{photo_ur}')]])
            bot.sendPhoto(chat_id, photo=photo_ur, caption='<b>Requested Image</b>',
                          parse_mode='html', reply_markup=markup2)
            global inline_url
            inline_url = photo_ur

        else:
            markup = InlineKeyboardMarkup(inline_keyboard=[[dict(text='🦋Unsplash', url='https://unsplash.com/'), dict(
                text='☂️developer', url='https://t.me/brows000/')], [dict(text='Switch inline', switch_inline_query='initial query')]])
            photo_url = 'https://images.app.goo.gl/HvzqesBKHkcpFV7BA'
            bot.sendPhoto(chat_id, photo=photo_url, parse_mode='html',
                          caption='<b>Hello, welcome to 4kimage downloder bot send me url from google image then the bot will download it in HD or UHD standard it depends on your url</b>', reply_markup=markup)


def on_inline_query(msg):
    def compute():
        query_id, from_id, query_string = telepot.glance(
            msg, flavor='inline_query')
        print('%s: Computing for: %s' %
              (threading.current_thread().name, query_string))

        articles = [InlineQueryResultArticle(
            id='abcde', title='🦋Unsplash', input_message_content=InputTextMessageContent(message_text='Unsplash is a website dedicated to sharing stock photography under the Unsplash license. The website claims over 110,000 contributing photographers and generates more than 11 billion photo impressions per month on their growing library of over 1.5 million photos.')),
            dict(type='article',
                 id='fghij', title='🐲Developer', input_message_content=dict(message_text='This bot will help you to download images from unplash.com and also from google data base you can find me on @brows000')),dict(type='article',
                 id='dgsfe', title='🧩API', input_message_content=dict(message_text='What is unsplash API? The Unsplash API is a modern JSON API that surfaces all of the info you ll need to build any experience for your users. It"s so simple to use that we even run unsplash.com on it! Get a photo Search photos List new photos.')),dict(type='article',
                 id='fghij', title='🔰how does it work', input_message_content=dict(message_text='This bot is download image from specific url you have to send the url first before doing any thing so search image using google or unsplash then send the link and the bot will downlode it also you can forward images with links then the bot will do the rest.'))]

        photo1_url = 'https://images.unsplash.com/photo-1596519115568-19f1bd10afde?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60'
        photo2_url = 'https://images.unsplash.com/photo-1590893384683-cb427aad218b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60'
        photo3_url = 'https://images.unsplash.com/photo-1596641314492-dd437d0d5463?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60'
        photo4_url = 'https://images.unsplash.com/photo-1596880630573-28c5371f7eb1?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60'
        photo5_url = 'https://images.unsplash.com/photo-1596806031968-7ff4df83c356?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60'
        photo6_url = 'https://images.unsplash.com/photo-1596872595556-2586eeb6982e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60'
        photo9_url = 'https://images.unsplash.com/photo-1588863746368-508ae44a7917?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60'
        photo10_url = 'https://images.unsplash.com/photo-1588863746368-508ae44a7917?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60'
        photo11_url = 'https://images.unsplash.com/photo-1596574620648-98e00b6a09e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60'
        photo12_url = 'https://images.unsplash.com/photo-1596718802962-2b4225d41955?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60'
        photo13_url = 'https://images.unsplash.com/photo-1596878276931-02dfa8ba94a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60'
        photos = [InlineQueryResultPhoto(id='12345', photo_url=photo1_url, thumb_url=photo1_url), dict(type='photo', id='67890', photo_url=photo2_url, thumb_url=photo2_url), dict(type='photo', id='53437', photo_url=photo3_url, thumb_url=photo3_url), dict(
            type='photo', id='51826', photo_url=photo4_url, thumb_url=photo4_url), dict(type='photo', id='43433', photo_url=photo5_url, thumb_url=photo5_url), dict(type='photo', id='87665', photo_url=photo6_url, thumb_url=photo6_url), dict(
                type='photo', id='54653', photo_url=photo11_url, thumb_url=photo11_url), dict(
                type='photo', id='34524', photo_url=photo10_url, thumb_url=photo10_url),dict(
                type='photo', id='75676', photo_url=photo9_url, thumb_url=photo9_url),dict(
                type='photo', id='63547', photo_url=photo12_url, thumb_url=photo12_url),dict(
                type='photo', id='54527', photo_url=photo13_url, thumb_url=photo13_url),dict(
                type='photo', id='84658', photo_url=inline_url, thumb_url=inline_url)]

        result_type = query_string[-1:].lower()

        if result_type == 'a':
            return articles
        elif result_type == 'p':
            return photos
        else:
            results = articles if random.randint(0, 1) else photos
            if result_type == 'b':
                return dict(results=results, switch_pm_text='Back to Bot', switch_pm_parameter='Optional_start_parameter')
            else:
                return dict(results=results)

    answerer.answer(msg, compute)


def on_chosen_inline_result(msg):
    result_id, from_id, query_string = telepot.glance(
        msg, flavor='chosen_inline_result')
    print('Chosen Inline Result:', result_id, from_id, query_string)


bot = telepot.Bot("1411149304:AAHpVyGm5sHnS9Thwga5V_agOPofPBYO6qY")
answerer = telepot.helper.Answerer(bot)
MessageLoop(bot, {'inline_query': on_inline_query,
                  'chat': fileShareFunction}).run_as_thread()
print('server online ...')
while 1:
    time.sleep(10)
