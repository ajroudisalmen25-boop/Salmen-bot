import telebot
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import io
import requests
import arabic_reshaper
from bidi.algorithm import get_display

TOKEN = os.environ.get('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TOKEN)

# فونت عربي مضمون من جوجل
FONT_URL = "https://github.com/googlefonts/noto-fonts/raw/main/hinted/ttf/NotoSansArabic/NotoSansArabic-Black.ttf"
FONT_PATH = "/tmp/noto_arabic.ttf"

if not os.path.exists(FONT_PATH):
    r = requests.get(FONT_URL)
    with open(FONT_PATH, 'wb') as f:
        f.write(r.content)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🧠🔥 ابعت كلمة نعملك بيها لوقو ميتال")

@bot.message_handler(func=lambda message: True)
def make_logo(message):
    text = message.text
    
    # هاذي اهم خطوة: نصلحو العربي
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    
    img = Image.new('RGB', (1080, 1080), color=(5, 0, 10))
    draw = ImageDraw.Draw(img)
    
    font = ImageFont.truetype(FONT_PATH, 300) # اكبر حجم
    
    bbox = draw.textbbox((0, 0), bidi_text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (1080 - text_width) / 2
    y = (1080 - text_height) / 2
    
    # عروق المخ
    for _ in range(100):
        x1 = random.randint(int(x-60), int(x+text_width+60))
        y1 = random.randint(int(y-60), int(y+text_height+60))
        x2 = x1 + random.randint(-50, 50)
        y2 = y1 + random.randint(-50, 50)
        draw.line([(x1,y1), (x2,y2)], fill=(150, 0, 150), width=3)
    
    # ظلال ميتال
    for i in range(18, 2, -3):
        draw.text((x+i, y+i), bidi_text, fill=(0, 0, 0), font=font)
    draw.text((x+8, y+8), bidi_text, fill=(120, 0, 120), font=font)
    draw.text((x+4, y+4), bidi_text, fill=(220, 0, 0), font=font)
    draw.text((x, y), bidi_text, fill=(255, 100, 150), font=font)
    draw.text((x, y-5), bidi_text, fill=(255, 255, 255), font=font)
    
    # شرار
    for _ in range(40):
        sx = random.randint(int(x), int(x+text_width))
        sy = random.randint(int(y), int(y+text_height))
        draw.ellipse([(sx,sy), (sx+8,sy+8)], fill=(255, 200, 0))
    
    img = img.filter(ImageFilter.SMOOTH_MORE)
    
    bio = io.BytesIO()
    bio.name = 'brain_metal.png'
    img.save(bio, 'PNG')
    bio.seek(0)
    bot.send_photo(message.chat.id, bio, caption=f"🧠🔥 لوقو العقل الملعون: {text}")

print("Bot started - Final Arabic Version 🧠🔥")
bot.infinity_polling(skip_pending=True)
