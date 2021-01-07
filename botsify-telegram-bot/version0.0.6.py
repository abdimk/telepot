#@autor abdisa merga date 1/3/2/2021
#          2021all rights reserved


import sys
import time
import telepot
import googlesearch
import wikipedia
import wikipediaapi
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
        markup = InlineKeyboardMarkup(inline_keyboard=[[dict(text='☂️Developer', url='https://t.me/abdisamerga/'),dict(text='Switch inline', switch_inline_query='initial query')],[]])
        responce = bot.getChat(chat_id)
        first_name = responce['first_name']
        bot.sendChatAction(chat_id, 'typing')
        bot.sendMessage(chat_id,f'Hello <b>{first_name}! </b> Botisfy is a web-based tool that enables users to search information on the World Wide Web. <b>search specific phrase</b> like <code>cat</code>',parse_mode='html', reply_markup=markup)
    if command =='/about':
        markup1 = InlineKeyboardMarkup(inline_keyboard=[[dict(text='🐱Github', url='https://github.com/abdimk/telepot/tree/master/botsify-telegram-bot')],[]])
        uphoto = 'https://images.app.goo.gl/x5A2R7tEotv96mUU9'
        bot.sendChatAction(chat_id, 'typing')
        bot.sendPhoto(chat_id,photo=uphoto,caption='This bot will help you to <b>search</b> images,words,phrases on <code>Google</code>,<code>Wikipedia</code> and <code>Bing</code> by uisng HTTP request for humans am trying to improve this bot version <code>0.0.5</code>' ,parse_mode='html',reply_markup=markup1)
    if command =='/help':
        helpurl = 'https://images.app.goo.gl/k8UQ1NWkfvfRte948'
        bot.sendChatAction(chat_id, 'typing')
        bot.sendPhoto(chat_id,photo=helpurl,caption='<code>/start</code> to start the bot\n<code>/about</code> to see the source code\n<code>/help</code> to get help just send specific phrase like <code>Ufc</code>,<code>Bittorrent</code>,<code>Homelander</code> ' ,parse_mode='html',reply_markup=None)
    if command =='/random':
        rand = wikipedia.random()
        rvd = googlesearch.search(f'{rand}', lang='en')
        try:
            rphoto_url_from_google = rvd[0]
        except:
            pass
        try:
            wikipedia.set_lang("en")
            rvar = wikipedia.search(f'{rand}')
            try:
                rvalue = rvar[0]
            except IndexError:
                bot.sendChatAction(chat_id, 'typing')
                bot.sendMessage(chat_id,f'opps! Your search-<b>{rand}</b> did not match any documents.',parse_mode='html',reply_markup=None)
            rtitle = str(rvalue)
            try:
                rlan = wikipedia.summary(f'{rtitle}', sentences=3,auto_suggest=False, redirect=False)
            except:
                try:
                    rlan = wikipedia.summary(f'{rtitle}', sentences=3,auto_suggest=True, redirect=True)
                except:
                    evwiki_wiki = wikipediaapi.Wikipedia('en')
                    epage_py = evwiki_wiki.page(f'{rtitle}')
                    rlan = epage_py.summary[0:200]
            bot.sendChatAction(chat_id, 'typing')
            bot.sendPhoto(chat_id,photo=f'{str(rphoto_url_from_google)}',caption=f'{rlan}',reply_markup=None)
        except Exception:
            wikipedia.set_lang("en")
            mvar2 = wikipedia.search(f'{rand}')
            global mvalue2
            try:
                mvalue2 = mvar2[0]
            except (IndexError,UnboundLocalError,NameError):
                pass
            mtitle2 = str(mvalue2)
            try:
                mlan2 = wikipedia.summary(f'{mtitle2}', sentences=3,auto_suggest=False, redirect=False)
            except:
                try:
                    mlan2 = wikipedia.summary(f'{mtitle2}', sentences=3,auto_suggest=True, redirect=True)
                except:
                    evwiki_wiki = wikipediaapi.Wikipedia('en')
                    epage_py = evwiki_wiki.page(f'{rtitle}')
                    mlan2 = epage_py.summary[0:200]

            try:
                mphoto_url_from_wiki = wikipedia.page(mtitle2).url
                bot.sendChatAction(chat_id, 'typing')
                bot.sendPhoto(chat_id,photo=f'{str(mphoto_url_from_wiki)}',caption=f'{mlan2}',reply_markup=None)
            except (wikipedia.exceptions.PageError,wikipedia.exceptions.DisambiguationError,wikipedia.DisambiguationError):
                bot.sendMessage(chat_id,f'{mlan2}',reply_markup=None)



    if command != '/start' and command != '/about' and command !='/help' and command !='/random':
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
                bot.sendChatAction(chat_id, 'typing')
                bot.sendMessage(chat_id,f'opps! Your search-<b>{command}</b> did not match any documents.',parse_mode='html',reply_markup=None)
            title = str(value)
            try:
                lan = wikipedia.summary(f'{title}', sentences=3,auto_suggest=False, redirect=False)
            except:
                try:
                    lan = wikipedia.summary(f'{title}', sentences=3,auto_suggest=True, redirect=True)
                except:
                    wiki_wiki = wikipediaapi.Wikipedia('en')
                    page_py = wiki_wiki.page(f'{title}')
                    lan = page_py.summary[0:200]

            bot.sendChatAction(chat_id, 'typing')
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
                try:
                    lan2 = wikipedia.summary(f'{title2}', sentences=3,auto_suggest=True, redirect=True)
                except:
                    vwiki_wiki = wikipediaapi.Wikipedia('en')
                    page_py = vwiki_wiki.page(f'{title2}')
                    lan2 = page_py.summary[0:200]
            try:
                photo_url_from_wiki = wikipedia.page(title2).url
                bot.sendChatAction(chat_id, 'typing')
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
