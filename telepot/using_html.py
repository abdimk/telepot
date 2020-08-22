try:
    import sys
    import telepot 
    import time
    from telepot.loop import MessageLoop
except Exception as error:
    print('some thing went wrong'.format(error))
'''
#using html , prase_mood = 'html'
#token must be from the botfather
'''

def message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print('Chat:', content_type, chat_type, chat_id)
    command = msg['text'].lower()
    if command == '/start':
        #inaddition to this you can also use markdown , parse_mood = 'markdown'
        bot.sendMessage(chat_id,'<b>hello there </b>',parse_mode='html')
        #hints
        '''
        <b>bold</b> or <strong>bold</strong>
        <
        '''


#get your token from bot father @BotFather
TOKEN = sys.argv[1] # or TOKEN = "Your-Bot-Token"
bot = telepot.Bot(TOKEN)
answer = telepot.helper.Answerer(bot)

MessageLoop(bot,{'chat': message}).run_as_thread()
print('Listening....')

#to make the program keep running
while 1:
    time.sleep(10)