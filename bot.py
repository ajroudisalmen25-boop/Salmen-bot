import os
import telebot

# يقرا التوكن من Render. اسمو لازم يكون BOT_TOKEN
TOKEN = os.environ.get('BOT_TOKEN')

# اذا ما لقاش التوكن يوقف و يقلك الغلطة
if not TOKEN:
    print("ERROR: BOT_TOKEN موش موجود في Environment Variables")
    exit()

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """👹 اهلا بيك يا سلمان
انا البوت متاعك و نخدم.
اكتبلي اي حاجة نجاوبك عليها 🔥""")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    text = message.text
    bot.reply_to(message, f"قلت: {text}\n\nمازلت بوت بسيط. بش نطورني بعدين 😎")

print("البوت يخدم توة...")
bot.infinity_polling()
