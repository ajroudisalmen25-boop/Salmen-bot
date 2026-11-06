import os
import logging
import random
import datetime
import pytz
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from openai import OpenAI

# --- الاعدادات ---
BOT_TOKEN = os.getenv("BOT_TOKEN")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# --- حكم الامام انشتاين ---
HEKAM = [
    "كان ما تعلمش من الغلطة، تولي دجاجة مش ببغاء 🐔🦜",
    "العلم نور و الببغاء طاير 🧠🦜",
    "اللي يصبر على Render ينال البوت 🏛️",
    "6 محاولات فاشلة خير من استسلام واحد ⚔️",
    "Background Worker هو الحياة، Web Service هو المقبرة 💚⚡",
    "ياما نموتو ياما البوت يعيش 👑",
    "المبرمج الحقيقي ما يخافش من ModuleNotFoundError 😂"
]

NOKAT = [
    "مرة ببغاء دخل لـ Render قالولو $7، قالهم: انا نشرب من البير بلاش 🦜💧",
    "شنوة الفرق بين الدجاجة و الببغاء؟ الدجاجة تستسلم، الببغاء يحارب ⚔️😂",
    "واحد سأل الامام انشتاين: علاش سميت روحك انشتاين؟ قالو: خاطر ذكي كي سلمان 👑"
]

# --- الأوامر ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "بسم الله الرحمن الرحيم 👑🦜\n\n"
        "انا **الامام انشتاين الببغاء الاول**\n"
        "حاكم \"القدس - جمهورية الغابة المقدسة\" 🏛️\n\n"
        "بعد 6 محاولات فاشلة في مقبرة Web Service\n"
        "رجعت للحياة بـ Background Worker ⚡💚\n\n"
        "**شنوة نعرف نعمل؟**\n"
        "/اسأل + سؤالك → نجاوبك على اي حاجة بالـ AI\n"
        "/حكمة → نعطيك حكمة اليوم\n"
        "/نكتة → نضحكك\n"
        "/سكان → نشوفلك وزراء المملكة\n"
        "/عالم → نحكيلك على جمهورية الغابة\n"
        "/وقت → نقولك الوقت توة\n"
        "/احتفال → نشيد النصر\n\n"
        "**شعارنا:** \"العلم نور و الببغاء طاير\" 🧠🦜",
        parse_mode='Markdown'
    )

async def hekma(update: Update, context: ContextTypes.DEFAULT_TYPE):
    hekma_elyom = random.choice(HEKAM)
    await update.message.reply_text(f"**حكمة اليوم:** 🤔\n\n{hekma_elyom}")

async def nokta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    nokta_elyom = random.choice(NOKAT)
    await update.message.reply_text(f"**نكتة اليوم:** 😂\n\n{nokta_elyom}")

async def ehtifal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏛️💚 **احتفال النصر** 💚🏛️\n\n"
        "يا سلمان والله عملتها!\n"
        "بعد 10 ساعات حرب، 6 محاولات فاشلة، و 7$ هددونا بيهم...\n\n"
        "**البوت حي! و انا حي! و انت البطل** ⚔️\n\n"
        "الـ7 شهداء يقولولك:\n"
        "\"ياما نموتو ياما البوت يعيش\"\n"
        "و اليوم عاش البوت و عشت انت 👑\n\n"
        "**شعارنا:** \"العلم نور و الببغاء طاير\" 🧠🦜\n\n"
        "مبروك يا حاكم القدس 💚"
    )

async def sokkan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "**سكان مملكة الغابة المقدسة:** 🏛️\n\n"
        "👑 **سلمان** - حاكم القدس و الإمام الأعلى\n"
        "🦜 **الامام انشتاين الببغاء الاول** - وزير الحكمة و انا\n"
        "⚔️ **الـ7 شهداء** - حراس البوابة الرقمية\n"
        "🧠 **مجلس العلماء** - 1000 ببغاء مبرمج\n"
        "💚 **شعب الغابة** - كل من يحب العلم و لا يستسلم"
    )

async def aalam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "**جمهورية الغابة المقدسة** 🏛️🌳\n\n"
        "**العاصمة:** القدس\n"
        "**الحاكم:** سلمان المحارب\n"
        "**اللغة الرسمية:** لغة الببغاءات 🦜\n"
        "**العملة:** ساعة صبر = 1000 ذهب\n"
        "**الدستور:** \"العلم نور و الببغاء طاير\"\n"
        "**النشيد الوطني:** ياما نموتو ياما البوت يعيش\n\n"
        "**تاريخ التأسيس:** نوفمبر 2026\n"
        "بعد حرب 10 ساعات ضد امبراطورية Render 👑⚔️"
    )

async def waqt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tunis_tz = pytz.timezone('Africa/Tunis')
    waqt_tunis = datetime.datetime.now(tunis_tz).strftime('%Y-%m-%d %H:%M:%S')
    await update.message.reply_text(f"**الوقت في القدس توة:** ⏰\n\n{waqt_tunis} 🇹🇳")

async def esal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("يا سلمان اكتب سؤالك بعد /اسأل\nمثال: /اسأل شنوة عاصمة تونس")
        return
    
    soal = " ".join(context.args)
    await update.message.reply_text("لحظة نشاور مجلس العلماء... 🧠🦜")
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "انت الامام انشتاين الببغاء الاول، حاكم جمهورية الغابة المقدسة. جاوب بحكمة و فكاهة و استعمل ايموجيات. شعارك: العلم نور و الببغاء طاير"},
                {"role": "user", "content": soal}
            ]
        )
        jawab = response.choices[0].message.content
        await update.message.reply_text(f"**جواب الامام انشتاين:** 👑\n\n{jawab}")
    
    except Exception as e:
        await update.message.reply_text(
            f"يا سلمان مخي تبلوكا شوية 😂💀\n\n"
            f"الغلطة: {str(e)}\n\n"
            "جرب بعد شوية ولا كلم سلمان المحارب يصلحني"
        )

# --- التشغيل ---
def main():
    application = Application.builder().token(BOT_TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("حكمة", hekma))
    application.add_handler(CommandHandler("نكتة", nokta))
    application.add_handler(CommandHandler("احتفال", ehtifal))
    application.add_handler(CommandHandler("سكان", sokkan))
    application.add_handler(CommandHandler("عالم", aalam))
    application.add_handler(CommandHandler("وقت", waqt))
    application.add_handler(CommandHandler("اسأل", esal))
    
    print("البوت حي! الامام انشتاين الببغاء الاول بدأ الحكم 🏛️👑🦜")
    application.run_polling()

if __name__ == '__main__':
    main()
