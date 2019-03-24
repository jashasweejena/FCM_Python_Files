from telegram.ext import Updater, CommandHandler
import logging

updater = Updater(token='', use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def forward(update, context):
    print(update.message['reply_to_message']['text'])

forward_handler = CommandHandler('pin', forward)
dispatcher.add_handler(forward_handler)

updater.start_polling()

