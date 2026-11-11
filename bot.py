import telebot
from telebot import types
import random
import json
import os
import threading
from flask import Flask

# نقراو التوكن من Environment - آمن 100%
TOKEN = 8928666107:AAFdWctjlr-foi-iuLJnsw0HI0n40jH1qDg
if not TOKEN:
    raise ValueError("حط BOT_TOKEN في Environment Variables")

bot = telebot.TeleBot(TOKEN)

# قاعدة بيانات بسيطة
DB_FILE = "users.json"

def load_data():
    if not os.path.exists(DB_FILE):
        return {}
    try:
        with open(DB_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}

def save_data(data):
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def get_user(user_id):
    data = load_data()
    user_id = str(user_id)
    if user_id not in data:
        data[user_id] = {"coins": 0, "level": 1, "last_daily": ""}
        save_data(data)
    return data[user_id]

def add_coins(user_id, amount):
    data = load_data()
    user_id = str(user_id)
    if user_id not in data:
        data[user_id] = {"coins": 0, "level": 1, "last_daily": ""}
    data[user_id]["coins"] += amount
    # نظام لفل بسيط
    if data[user_id]["coins"] >= data[user_id]["level"] * 100:
        data[user_id]["level"] += 1
        bot.send_message(user_id, f"🎉 مبروك! طلعت Level {data[user_id]['level']}")
    save_data(data)
    return data[user_id]["coins"]

# الأزرار الرئيسية
def main_menu():
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("🧠 حكمة اليوم", callback_data="hikma")
    btn2 = types.InlineKeyboardButton("😂 نكتة", callback_data="nokta")
    btn3 = types.InlineKeyboardButton("👑 وزراء المملكة", callback_data="skan")
    btn4 = types.InlineKeyboardButton("🌍 عالم الغابة", callback_data="alam")
    btn5 = types.InlineKeyboardButton("⏰ الوقت توة", callback_data="waqt")
    btn6 = types.InlineKeyboardButton("💰 فلوسي", callback_data="coins")
    btn7 = types.InlineKeyboardButton("🛒 المتجر", callback_data="shop")
    btn8 = types.InlineKeyboardButton("🎁 هدية يومية", callback_data="daily")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    add_coins(message.from_user.id, 10)
    text = f"""
بسم الله الرحمن الرحيم 🦜👑

أهلا {message.from_user.first_name}! 
أنا **الامام انشتاين الببغاء الاول** 
حاكم "القدس - جمهورية الغابة المقدسة" 🏛️

رجعت للحياة بـ Background Worker ⚡💚

**شعارنا:** "العلم نور و الببغاء طاير" 🧠🦜

**هدية:** +10 Coins للتسجيل 🎁

اخطار شنوة تحب تعمل:
    """
    bot.send_message(message.chat.id, text, reply_markup=main_menu())

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    user_id = call.from_user.id
    user = get_user(user_id)
    
    if call.data == "hikma":
        hikam = [
            "العلم في الصغر كالنقش على الحجر",
            "من جد وجد ومن زرع حصد",
            "الوقت كالسيف إن لم تقطعه قطعك",
            "اطلبوا العلم من المهد إلى اللحد",
            "خير جليس في الزمان كتاب"
        ]
        add_coins(user_id, 5)
        bot.answer_callback_query(call.id, "+5 Coins 🪙")
        bot.edit_message_text(
            f"🧠 **حكمة اليوم:**\n\n{random.choice(hikam)}\n\n+5 Coins 💰 | رصيدك: {user['coins']+5} 🪙", 
            call.message.chat.id, call.message.message_id, 
            parse_mode="Markdown", reply_markup=main_menu()
        )
    
    elif call.data == "nokta":
        nokat = [
            "واحد مشى للبحر.. روح مبلول 😂",
            "قالو للغبي احفر بير.. حفر وطاح فيه 😂",
            "واحد يسأل: قداش الساعة؟ قالو: رخيصة 😂",
            "مجنون حب ينتحر.. رمى روحو من الدور الأرضي 😂"
        ]
        add_coins(user_id, 3)
        bot.answer_callback_query(call.id, "+3 Coins 🪙")
        bot.edit_message_text(
            f"😂 **نكتة:**\n\n{random.choice(nokat)}\n\n+3 Coins 💰 | رصيدك: {user['coins']+3} 🪙", 
            call.message.chat.id, call.message.message_id, reply_markup=main_menu()
        )
    
    elif call.data == "coins":
        bot.edit_message_text(
            f"💰 **فلوسك:** {user['coins']} Coins\n📊 **لفل:** {user['level']}\n\nكل 100 Coins = Level Up ⬆️", 
            call.message.chat.id, call.message.message_id, reply_markup=main_menu()
        )
    
    elif call.data == "shop":
        shop_text = """
🛒 **متجر المملكة**

👑 **تاج ملكي** - 500 Coins `/buy تاج`
🦜 **ببغاء ذهبي** - 300 Coins `/buy ببغاء`
⚔️ **سيف الملوك** - 200 Coins `/buy سيف`

اكتب `/buy اسم_الغرض` باش تشري
        """
        bot.edit_message_text(shop_text, call.message.chat.id, call.message.message_id, reply_markup=main_menu())
    
    elif call.data == "daily":
        from datetime import datetime
        today = datetime.now().strftime("%Y-%m-%d")
        if user.get("last_daily") == today:
            bot.answer_callback_query(call.id, "خذيت الهدية اليوم ❌", show_alert=True)
        else:
            data = load_data()
            data[str(user_id)]["last_daily"] = today
            save_data(data)
            new_coins = add_coins(user_id, 50)
            bot.answer_callback_query(call.id, "+50 Coins 🎁")
            bot.edit_message_text(
                f"🎁 **هدية يومية:** +50 Coins\n💰 رصيدك توة: {new_coins} 🪙\n\nارجع غدوة لهدية أخرى!", 
                call.message.chat.id, call.message.message_id, reply_markup=main_menu()
            )
    
    elif call.data == "skan":
        bot.edit_message_text(
            "👑 **وزراء المملكة:**\n\n1. وزير الضحك 😂\n2. وزير الحكمة 🧠\n3. وزير البرمجة 💻\n4. وزير الاقتصاد 💰\n\nقريبا نزيدو وزراء جدد!", 
            call.message.chat.id, call.message.message_id, reply_markup=main_menu()
        )
    
    elif call.data == "alam":
        bot.edit_message_text(
            "🌍 **جمهورية الغابة المقدسة**\n\nعاصمة: القدس 🏛️\nالحاكم: الامام انشتاين الببغاء الاول 🦜\nالسكان: كل الحيوانات الطيبة\nالعملة: Coins 🪙\n\n**القانون:** ممنوع الكذب والغش", 
            call.message.chat.id, call.message.message_id, reply_markup=main_menu()
        )
    
    elif call.data == "waqt":
        from datetime import datetime
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        bot.edit_message_text(
            f"⏰ **الوقت توة:**\n{now}\n\nالوقت كالسيف إن لم تقطعه قطعك ⚔️", 
            call.message.chat.id, call.message.message_id, reply_markup=main_menu()
        )

@bot.message_handler(commands=['buy'])
def buy_item(message):
    try:
        item = message.text.split(' ', 1)[1]
        user_id = message.from_user.id
        user = get_user(user_id)
        prices = {"تاج": 500, "ببغاء": 300, "سيف": 200}
        
        if item not in prices:
            bot.reply_to(message, "❌ الغرض هذا موش موجود في المتجر")
            return
        
        if user["coins"] >= prices[item]:
            data = load_data()
            data[str(user_id)]["coins"] -= prices[item]
            save_data(data)
            bot.reply_to(message, f"✅ شريت {item} بـ {prices[item]} Coins\n💰 رصيدك: {data[str(user_id)]['coins']} 🪙")
        else:
            bot.reply_to(message, f"❌ فلوسك ما تكفيش! لازمك {prices[item]} Coins")
    except:
        bot.reply_to(message, "استعمل: /buy تاج")

# Keep Alive للـ Render
app = Flask('')

@app.route('/')
def home():
    return "Salmen Bot يخدم 🔥"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

def run_bot():
    print("Salmen Bot خدم ✅")
    bot.polling(non_stop=True)

if __name__ == "__main__":
    t = threading.Thread(target=run_flask)
    t.start()
    run_bot()
