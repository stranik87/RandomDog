from telegram import Bot

TOKEN = "5922381162:AAHZlv7P-uypWE8IzpQd0F6pZq9vex_IhyI"

bot = Bot(token=TOKEN)

print(bot.set_webhook("https://echobotdeploy.pythonanywhere.com"))