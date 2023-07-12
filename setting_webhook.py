from telegram import Bot

TOKEN = "6130157096:AAHgjNJMWeQhYdT5mMJd3jQgFJgz8O7JBtA"

bot = Bot(token=TOKEN)


def get_info():
    print(bot.get_webhook_info())

def seting_webhook():
    print(bot.set_webhook("https://echobotdeploy.pythonanywhere.com/"))

def delete_webhook():
    print(bot.delete_webhook())

get_info()