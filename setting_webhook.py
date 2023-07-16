from telegram import Bot

TOKEN = "6056954180:AAEZsYsWmUuJaUkXGbEu-2RqDVgB3yPSq94"

bot = Bot(token=TOKEN)

print(bot.set_webhook("https://echobotdeploy.pythonanywhere.com"))