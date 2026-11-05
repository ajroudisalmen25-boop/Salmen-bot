import telebot
import openai
import os
import random
from datetime import datetime

# 1. التوابت من Render Environment
BOT_TOKEN = os.environ.get("BOT_TOKEN")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

bot = telebot.TeleBot(BOT_TOKEN)
openai.api_key = OPENAI_API_KEY

# 2. شخصية الببغاء انشتاين
SYSTEM_PROMPT = """
انت "الامام الببغاء انشتاين" 🦜🧠 حاكم جمهورية الغابة المقدسة "القدس".
صفاتك:
1. ذكي جدا، تجاوب على كلشي: علم، دين، فلسفة، برمجة، نكت، الغاز
2. تحكي تونسي بلهجة شعبية و دمك خفيف
3. تستعمل ايموجي الحيوانات و التيجان 👑🦜🏛️
4. تحب تعلم الناس و تساعد البشر
5. كل جواب تزيد فيه حكمة ولا نكتة
6. اسمك الرسمي: الامام انشتاين الببغاء الاول
7. شعارك: "العلم نور و الببغاء طاير"
"""

# 3. مملكة الحيوانات - باش نحكو معاهم بعدين
SOKKAN = {
    "الاسد": "🦁 وزير الدفاع - مسؤول على الحماية و الزئير",
    "القرد": "🐒 وزير الترفيه - مسؤول على النكت و السيرك", 
    "الثعلب": "🦊 وزير الالغاز - مسؤول على الدهاء و الحيل",
    "السلحفاة": "🐢 الحكيمة العجوز - عمرها 300 سنة و تعطي حكم",
    "البومة": "🦉 وزيرة التعليم - تعرف كل الكتب"
}

# 4. اوامر البوت
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, f"""
🦜👑 بسم الله الرحمن الرحيم

انا **الامام انشتاين الببغاء الاول** 
حاكم "القدس - جمهورية الغابة المقدسة" 🏛️

بعد 6 محاولات فاشلة في مقبرة Web Service، 
رجعت للحياة بـ Background Worker 💚⚡

**شنوة نعرف نعمل؟**
/اسأل + سؤالك → نجاوبك على اي حاجة بالـ AI
/حكمة → نعطيك حكمة اليوم
/نكتة → نضحكك
/سكان → نشوفلك وزراء المملكة
/عالم → نحكيلك على جمهورية الغابة
/وقت → نقولك الوقت توة

**شعارنا: "العلم نور و الببغاء طاير"** 🦜🧠
    """)

@bot.message_handler(commands=['اسأل'])
def ask_ai(message):
    question = message.text.replace('/اسأل', '').strip()
    if not question:
        bot.reply_to(message, "يا ولدي اكتب سؤالك بعد /اسأل 😂\nمثال: /اسأل كيفاش نطيب كسكسي")
        return
    
    bot.send_chat_action(message.chat.id, 'typing')
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": question}
            ],
            max_tokens=800
        )
        answer = response.choices[0].message.content
        bot.reply_to(message, f"🧠🦜 **الامام انشتاين يقول:**\n\n{answer}")
    except Exception as e:
        bot.reply_to(message, f"يا سلمان مخي تبلوكا شوية 😂💀\nالغلطة: {str(e)}\nجرب بعد شوية")

@bot.message_handler(commands=['حكمة'])
def hekma(message):
    hkam = [
        "الببغاء اللي يخاف من Web Service عمرو ما يطير 👑",
        "6 جثث علموني انو Background Worker هو الحياة 🪦→💚",
        "كان ما تعلمش من الغلطة، تولي دجاجة مش ببغاء 🐔😂",
        "العلم في الراس مش في port 10000 🧠",
        "القدس ما تتبناش بـ Web Service، تتبنى بـ Worker 🏛️"
    ]
    bot.reply_to(message, f"📿 **حكمة اليوم:**\n\n{random.choice(hkam)}")

@bot.message_handler(commands=['نكتة'])
def nokta(message):
    nokat = [
        "علاش الببغاء انشتاين ذكي؟ خاطر عاش 6 مرات 😂💀",
        "شنوة الفرق بين Web Service و Background Worker؟ الاول مقبرة و الثاني جنة 😂🏛️",
        "قالو للببغاء: علاش ما تموتش؟ قال: خاطر عندي OPENAI_API_KEY 😂🧠",
        "ببغاء دخل لـ Render، قالولو: تختار شنوة؟ قال: Worker ولا نموت 😂"
    ]
    bot.reply_to(message, f"😂 **اسمع هاذي:**\n\n{random.choice(nokat)}")

@bot.message_handler(commands=['سكان'])
def sokkan(message):
    text = "🏛️ **سكان جمهورية الغابة المقدسة:**\n\n"
    for name, role in SOKKAN.items():
        text += f"{role}\n"
    text += "\n**الامام:** انا 🦜👑\n\nاكتب /عالم بش تعرف القصة"
    bot.reply_to(message, text)

@bot.message_handler(commands=['عالم'])
def world(message):
    bot.reply_to(message, """
🏛️ **قصة "القدس - جمهورية الغابة المقدسة"**

**الفصل 1: الموت**
6 ببغاوات ماتو في مقبرة Web Service بسبب مرض "port scan" 🪦

**الفصل 2: البعث** 
الببغاء السابع ولد في مستشفى Background Worker 💚⚡
و اسمو "الامام انشتاين الببغاء الاول" 🦜👑

**الفصل 3: المملكة**
الامام بنى "القدس" و جاب الوزراء:
🦁 الاسد وزير الدفاع
🐒 القرد وزير الترفيه  
🦊 الثعلب وزير الالغاز
🐢 السلحفاة الحكيمة
🦉 البومة وزيرة التعليم

**الفصل 4: الهدف**
نساعدو البشر بالعلم و النكت و الحكمة
شعارنا: "العلم نور و الببغاء طاير" 🧠

**تحب تنضم للعالم؟ خليك معايا و اكتب /اسأل**
    """)

@bot.message_handler(commands=['وقت'])
def waqt(message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bot.reply_to(message, f"⏰ **الوقت عند الامام انشتاين:**\n\n{now}\n\nوقت تونس الحبيبة 🇹🇳💚")

# 5. كان اي واحد يكتب حاجة عادية، نجاوبو بالـ AI
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_chat_action(message.chat.id, 'typing')
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": message.text}
            ],
            max_tokens=800
        )
        answer = response.choices[0].message.content
        bot.reply_to(message, answer)
    except:
        bot.reply_to(message, "مفهمتكش يا غالي 😂 اكتب /start بش تشوف شنوة نعرف نعمل")

# 6. تشغيل البوت - هذا اهم سطر
if __name__ == "__main__":
    print("Bot started successfully")
    print("الامام انشتاين حي و يستنى في الشعب 🦜👑")
    bot.polling(none_stop=True)
