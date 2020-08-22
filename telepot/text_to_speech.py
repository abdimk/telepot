try:
    import sys
    import gtts
    from gtts import gTTS
    import telepot 
    import time
    from telepot.loop import MessageLoop
except Exception as error:
    print('some thing went wrong'.format(error))
'''
#sample text to speech bot
#token must be from the botfather
'''

def message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print('Chat:', content_type, chat_type, chat_id)
    command = msg['text'].lower()
    if command == '/start':
        bot.sendMessage(chat_id,'Enter text?')
    else:
        bot.sendChatAction(chat_id, 'UPLOAD_AUDIO')
        tts = gTTS(message, lang='en')
        tts.save('mk.mp3')
        with open('mk.mp3', 'rb') as speech:
            bot.sendChatAction(chat_id, 'UPLOAD_AUDIO')
            bot.sendVoice(chat_id, voice=speech, caption=f'{command}')

#get your token from bot father @BotFather
TOKEN = sys.argv[1] # or TOKEN = "Your-Bot-Token"
bot = telepot.Bot(TOKEN)
answer = telepot.helper.Answerer(bot)

MessageLoop(bot,{'chat': message}).run_as_thread()
print('Listening....')

#to make the program keep running
while 1:
    time.sleep(10)