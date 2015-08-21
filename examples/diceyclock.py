import time
import random
import datetime
import telepot

def handle(msg):
    chat_id = msg['from']['id']
    command = msg['text']

    print 'Got message: %s' % command

    if command == '/roll':
        bot.sendMessage(chat_id, random.randint(1,6))
    elif command == '/time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))

bot = telepot.Bot('*** INSERT TOKEN ***')
bot.notifyOnMessage(handle)
print 'I am listening ...'

while 1:
    time.sleep(10)