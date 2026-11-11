import os
import telebot
from flask import Flask
import threading

# يجيب التوكن من Environment متع Render - ما تحطوش هنا
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN موش موجود! حطو في Environment Variables في Render")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# هذا باش Render ما يعطيكش Error متع Port
@app.route('/')
def home():
    return "Salmen Bot خدم ✅"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "أهلا سلمان، البوت يخدم 🔥")

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(message, "ابعث أي حاجة ونجاوبك")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"قلت: {message.text}")

if __name__ == "__main__":
    # شغل Flask في thread وحدو
    threading.Thread(target=run_flask).start()
    print("Salmen Bot خدم ✅")
    bot.infinity_polling()
