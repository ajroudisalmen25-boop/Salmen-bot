import os
import telebot
import time
import logging

# شغّل الـ Logs باش تشوف الأخطاء في Render
logging.basicConfig(level=logging.INFO)

# جيب التوكن من Environment Variables
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN موش موجود! حطو في Environment Variables في Render")

bot = telebot.TeleBot(TOKEN)

# أمر /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلا سلمان 🔥\nالبوت يخدم 24/7 وموش باش يطيح راسك")

# أمر /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "ابعت أي حاجة ونجاوبك\n/Start - نبداو\n/Help - المساعدة")

# أي رسالة أخرى
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        bot.reply_to(message, f"قلت: {message.text}")
    except Exception as e:
        logging.error(f"Error: {e}")

# هذا أهم سطر: يخلي البوت يخدم وما يموتش
def main():
    logging.info("Salmen Bot Starting...")
    while True:
        try:
            logging.info("Bot is polling...")
            bot.infinity_polling(timeout=60, long_polling_timeout=60)
        except Exception as e:
            logging.error(f"Bot crashed: {e}")
            logging.info("Restarting in 15 seconds...")
            time.sleep(15)

if __name__ == '__main__':
    main()
