import sys
assert sys.version_info >= (3, 13), "Python 3.13.0 yoki yangi versiya talab qilinadi"

import requests
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
async def search_image(update: Update, context):
    query = update.message.text.strip()  # Bo'sh joylarni olib tashlash
    
    if not query:
        await update.message.reply_text("Iltimos, qidiruv so'zini kiriting!")
        return
        
    await update.message.reply_text(f"'{query}' bo'yicha rasm qidirilmoqda...")
    
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://www.google.com/search?q={query}&tbm=isch",
                headers=headers
            ) as response:
                if response.status != 200:
                    raise Exception("Google qidiruv xizmati javob bermadi")
                    
                html = await response.text()
                soup = BeautifulSoup(html, "html.parser")
                img = soup.find("img")
                
                if not img or not img.get("src"):
                    raise Exception("Rasm topilmadi")
                    
                await update.message.reply_photo(photo=img["src"])
                
    except Exception as e:
        error_msg = f"Xatolik yuz berdi: {str(e)}"
        print(error_msg)  # Logga yozish
        await update.message.reply_text("Kechirasiz, rasm topishda xatolik yuz berdi. Iltimos qaytadan urinib ko'ring.")
async def main():
    try:
        token = "YOUR_TELEGRAM_BOT_TOKEN"
        if not token or token == "YOUR_TELEGRAM_BOT_TOKEN":
            raise ValueError("Bot tokeni ko'rsatilmagan")
            
        app = ApplicationBuilder().token(token).build()
        
        # Handlerlarni qo'shish
        app.add_handler(CommandHandler("start", start))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search_image))
        
        print("Bot ishga tushdi...")
        await app.run_polling(allowed_updates=Update.ALL_TYPES)
        
    except Exception as e:
        print(f"Botni ishga tushirishda xatolik: {e}")
        sys.exit(1)
import os
token = os.getenv("TELEGRAM_BOT_TOKEN")
from urllib.parse import quote_plus
query = quote_plus(query)  # URL-safe qilish
from collections import defaultdict
from datetime import datetime, timedelta

user_requests = defaultdict(list)

async def check_rate_limit(user_id: int, limit: int = 5, window: int = 60) -> bool:
    now = datetime.now()
    user_requests[user_id] = [t for t in user_requests[user_id] if now - t < timedelta(seconds=window)]
    user_requests[user_id].append(now)
    return len(user_requests[user_id]) <= limit
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)
import aiohttp

async def get_image_url(query: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://www.google.com/search?q={query}&tbm=isch") as response:
            return await response.text()
