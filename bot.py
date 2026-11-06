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
    "كان ما تعلمش من الغلطة، تولي دجاجة مش ببغاء
