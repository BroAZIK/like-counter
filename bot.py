from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from telegram import Update
import os
import time

TOKEN = os.environ.get('TOKEN')

like = 0
dislike = 0

def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    text = 'salom xush kelipsiz'

    context.bot.sendMessage(chat_id, text)

def like_or_dislike(update: Update, context: CallbackContext):
    global like
    global dislike

    if update.message.text == '👍': like += 1
    if update.message.text == '👎': dislike += 1

    chat_id = update.message.chat.id

    context.bot.sendMessage(chat_id, f'likes: {like}\ndislikes: {dislike}')


updater = Updater(token=TOKEN)
dp = updater.dispatcher

dp.add_handler(handler=CommandHandler(command='start', callback=start))
dp.add_handler(handler=MessageHandler(filters=Filters.text(['👍', '👎']), callback=like_or_dislike))

updater.start_polling()
updater.idle()