from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from telegram import Update
import os

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

def echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)

