import telebot
import os
import requests
import json

TOKEN = os.environ.get('TELEGRAM_TOKEN')
OPENAI_KEY = os.environ.get('OPENAI_API_KEY')  # تحطها في Fly.io بعدين

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🧠 اهلا يا سلمان\nانا النسخة الملعونة من ChatGPT\nاسألني اي حاجة تحب عليها")

@bot.message_handler(func=lambda message: True)
def chat_gpt(message):
    try:
        bot.send_chat_action(message.chat.id, 'typing')
        
        # كان ما عندكش OpenAI Key يرد عليك هكا
        if not OPENAI_KEY:
            bot.reply_to(message, "يا وحش 👹 لازم تحط OPENAI_API_KEY في Fly.io باش نحكي معاك صح\nتوه نجاوبك اجابة بسيطة:\n\nسؤالك: " + message.text)
            return
        
        # هذا كود ChatGPT الصحيح
        headers = {
            "Authorization": f"Bearer {OPENAI_KEY}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "gpt-4o-mini",
            "messages": [
                {"role": "system", "content": "انت اسمك سلمان بوت. تحكي تونسي و دمك خفيف و ملعون شوية. جاوب باختصار و فدلكة."},
                {"role": "user", "content": message.text}
            ],
            "max_tokens": 500
        }
        
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data, timeout=30)
        
        if response.status_code == 200:
            reply = response.json()['choices'][0]['message']['content']
            bot.reply_to(message, reply)
        else:
            bot.reply_to(message, f"صارت جلطة مع OpenAI 😂\nCode: {response.status_code}\n{response.text}")
            
    except Exception as e:
        bot.reply_to(message, f"يا ملعون صار error:\n{str(e)}")

print("Salmen GPT Bot Started 🧠🔥")
bot.infinity_polling()
