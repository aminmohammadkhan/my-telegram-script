from flask import Flask, request, jsonify
from telethon import TelegramClient
from telethon.sessions import StringSession
import os
import asyncio
from threading import Thread

app = Flask(__name__)

# دریافت تنظیمات
API_ID = int(os.environ.get('API_ID'))
API_HASH = os.environ.get('API_HASH')
SESSION_STRING = os.environ.get('SESSION_STRING')

# راه اندازی کلاینت
client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

# تابع کمکی برای اجرای کارهای تلگرامی در لوپ جداگانه
def run_async(coro):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop.run_until_complete(coro)

# استارت اولیه کلاینت
run_async(client.start())

@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    phone = data.get('phone')
    message = data.get('message')

    try:
        # ارسال پیام
        run_async(client.send_message(phone, message))
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
