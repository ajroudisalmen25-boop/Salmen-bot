import telebot
import os
from PIL import Image, ImageDraw, ImageFont
import textwrap

TOKEN = 8928666107:AAFdWctjlr-foi-iuLJnsw0HI0n40jH1qDg
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👹 ابعتلي أي كلمة تو نعملك بيها لوقو ملعون")

@bot.message_handler(func=lambda message: True)
def make_logo(message):
    text = message.text
    img = Image.new('RGB', (800, 400), color=(0, 0, 0))
    d = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype("arial.ttf", 60)
    except:
        font = ImageFont.load_default()
    
    # خطوط حمراء مخيفة
    d.text((400, 200), text, fill=(180, 0, 0), font=font, anchor="mm")
    
    img.save("logo.png")
    bot.send_photo(message.chat.id, open("logo.png", "rb"))

print("Bot is running...")
bot.polling()
