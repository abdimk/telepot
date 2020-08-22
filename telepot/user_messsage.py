try:
    import sys
    import telepot 
    import time
    from telepot.loop import MessageLoop
except Exception as error:
    print('some thing went wrong'.format(error))
'''
#this simple code helps you to get user message and send them back
#token must be from the botfather
'''

def message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print('Chat:', content_type, chat_type, chat_id)
    command = msg['text'].lower()
    if command == '/start':
        #the bot will send the command agin and agin
        bot.sendMessage(chat_id,f'{command}')



#get your token from bot father @BotFather
TOKEN = sys.argv[1] # or TOKEN = "Your-Bot-Token"
bot = telepot.Bot(TOKEN)
answer = telepot.helper.Answerer(bot)

MessageLoop(bot,{'chat': message}).run_as_thread()
print('Listening....')

#to make the program keep running
while 1:
    time.sleep(10)