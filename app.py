from flask import Flask, request, jsonify
from telethon import TelegramClient
from telethon.sessions import StringSession
import os
import asyncio
from threading import Thread

app = Flask(__name__)

# دریافت تنظیمات از محیط Railway
API_ID = int(os.environ.get('API_ID', 0))
API_HASH = os.environ.get('API_HASH', '')
SESSION_STRING = os.environ.get('SESSION_STRING', '')

# راه اندازی کلاینت تلگرام
client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

# اجرای کلاینت در یک رشته (Thread) جداگانه برای جلوگیری از تداخل
def start_client():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(client.start())
    loop.run_forever()

# استارت کلاینت در پس‌زمینه
Thread(target=start_client, daemon=True).start()

@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    phone = data.get('phone')
    message = data.get('message')

    try:
        # ارسال پیام با استفاده از کلاینتِ فعال در رشته‌ی جداگانه
        asyncio.run_coroutine_threadsafe(client.send_message(phone, message), client.loop).result()
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
