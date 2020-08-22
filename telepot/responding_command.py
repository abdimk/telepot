try:
    import sys
    import random
    import telepot 
    import time
    from telepot.loop import MessageLoop
except Exception as error:
    print('some thing went wrong'.format(error))
'''
#simple telegarm bot to get the name, user_name , user_id
#token must be from the botfather
'''

def message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print('Chat:', content_type, chat_type, chat_id)
    command = msg['text'].lower()
    if command.lower() == '/start':
        msg = '''
<b>Hello</b> there !
avalible commands commands 
/greetings  
/celebrate
/colors
/game 
/image  
'''
        bot.sendMessage(chat_id,f'{msg}',parse_mode='html',reply_markup=None)

    if command.lower() =='/gretings' and command.lower() != '/start':
        values = random.choice(['Good morning', 'Hey there!','hola','Hello'])
        bot.sendMessage(chat_id,f'{values}',reply_markup=None)
    if command.lower() =='/celebrate':
        bot.sendMessage(chat_id,'Good job')
    if command.lower() =='/colors':
        color = random.choice(['❤','🧡','💙','🖤','💛','💜','💚','🤎','💝'])
        bot.sendMessage(chat_id,f'{color}',reply_markup=None)
    if command.lower() =='/game':
        unknown = random.randint(1,5)
        bot.sendMessage(chat_id,'Guess a number')
        if command.lower() == unknown:
            bot.sendMessage(chat_id,'you won!',reply_markup=None)
        else:
            bot.sendMessage(chat_id,f'you lose! the number was {unknown}',reply_markup=None)
    if command.lower() == '/image':
        #sample photo
        photo_url = 'https://images.unsplash.com/photo-1596519115568-19f1bd10afde?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60'
        bot.sendPhoto(chat_id,photo=photo_url,caption='This is the caption of the image you can make it <b>Bold<b/> also',parse_mode='html',reply_markup=None)

#get your token from bot father @BotFather
TOKEN = sys.argv[1] # or TOKEN = "Your-Bot-Token"
bot = telepot.Bot(TOKEN)
answer = telepot.helper.Answerer(bot)

MessageLoop(bot,{'chat': message}).run_as_thread()
print('Listening....')

#to make the program keep running
while 1:
    time.sleep(10)