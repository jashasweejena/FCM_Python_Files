from telegram.ext import Updater, CommandHandler
import logging
import messaging_test

def get_file_contents(filename):
    """ Given a filename,
        return the contents of that file
    """
    try:
        with open(filename, 'r') as f:
            # It's assumed our file contains a single line,
            # with our API key
            return f.read().strip()
    except FileNotFoundError:
        print("'%s' file not found" % filename)

api_key = get_file_contents('keys/telegram_api_key')

updater = Updater(token=api_key, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def forward(update, context):
    message = update.message['reply_to_message']['text']
    print(message)
    messaging_test.send_to_token(message)

forward_handler = CommandHandler('pin', forward)
dispatcher.add_handler(forward_handler)

updater.start_polling()

