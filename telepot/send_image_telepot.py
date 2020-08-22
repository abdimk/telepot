try:
    import sys
    import time
    import telepot 
    from telepot.loop import MessageLoop
except Exception as error:
    print('some thing went wrong'.format(error))


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print('Chat:', content_type, chat_type, chat_id)
    command = msg['text'].lower()
    if command =='/start':
        responce = bot.getChat(chat_id)
        first_name = responce['first_name']
        logo_url = 'https://images.app.goo.gl/tAfEA7XAgJpSw2Ky5'
        bot.sendPhoto(chat_id,photo=logo_url,caption=f'hello <strong>{first_name}</strong> welcome to server 95 this server will provide links to donwnload movies',parse_mode='html')
        p1_url = 'https://images.app.goo.gl/JqVuZi3FruroCts47'
        bot.sendPhoto(chat_id,p1_url)

    
    
TOKEN =  sys.argv[1]
# your token
bot = telepot.Bot(TOKEN)
answerer = telepot.helper.Answerer(bot)

MessageLoop(bot, {'chat': on_chat_message}).run_as_thread()
print('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
