from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from envs import *
import logging
import telegram

# to get basic bot info
bot = telegram.Bot(token=testing_token)
print(bot.get_me())
# e.g. {'id': 1081436727, 'first_name': 'ABbot', 'is_bot': True, 'username': 
# 'ABLGbot', 'can_join_groups': True, 'can_read_all_group_messages': True, 
# 'supports_inline_queries': False}

# initialises the updater object
updater = Updater(token=testing_token, use_context=True)
# for quicker access to the dispatcher object
dispatcher = updater.dispatcher

# msg sent when /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='ALPHAAAAAAA')
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# to make the bot echo the user (only for pm)
def echo(update, context):
    print('echoing')
    print(context.args)
    context.bot.send_message(chat_id=update.effective_chat.id, \
        text=update.message.text)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)
# The Filters class contains a number of functions that filter incoming messages
# for texts, images, status updates and more

def caps(update, context):
    print(context.args)
    text_caps = ' '.join(context.args).upper()
    print(text_caps)
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)
caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)

# to start the bot
updater.start_polling()

# to stop the bot
updater.stop()

# to block execution
updater.idle()