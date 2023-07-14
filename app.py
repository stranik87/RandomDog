from flask import Flask, request

from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters
from handlers import start, help, echo

import os

TOKEN = os.environ.get('TOKEN')
bot = Bot(token=TOKEN)


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return 'webhook is working!'

    elif request.method == 'POST':
        dp = Dispatcher(bot, None, workers=0)

        update = Update.de_json(request.get_json(force=True), bot)
        
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("help", help))

        dp.add_handler(MessageHandler(Filters.text, echo))

        dp.process_update(update)

        return {'ok': True}


@app.route('/setwebhook')
def set_webhook():
    s = bot.set_webhook("http://stranik.pythonanywhere.com/")
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"