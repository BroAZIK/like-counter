from telegram.ext import Dispatcher, Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from telegram import Update, Bot
import os
import time
from flask import Flask, request
from handlers import start, like_or_dislike, echo


TOKEN = '6056954180:AAEZsYsWmUuJaUkXGbEu-2RqDVgB3yPSq94'
bot = Bot(token=TOKEN)


like = 0
dislike = 0

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def hello_world():
    if request.method == 'GET':
        return "Webhook is working"
    elif request.method == 'POST':
        dp = Dispatcher(bot, None, workers=0)

        update = Update.de_json(request.get_json(force=True), bot)

        dp.add_handler(CommandHandler('start', start))
        dp.add_handler(handlewr=MessageHandler(filters=Filters.text(['👍', '👎'], callback=like_or_dislike)))

        dp.add_handler(MessageHandler(Filters.text, echo))

        dp.process_update(update)

        return 'Got a POST request!'