from flask import Flask, request, jsonify
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
import os

app = Flask(__name__)

# گرفتن متغیرها
API_ID = int(os.environ.get('API_ID'))
API_HASH = os.environ.get('API_HASH')
SESSION_STRING = os.environ.get('SESSION_STRING')

# ایجاد کلاینت
client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    phone = data.get('phone')
    message = data.get('message')

    # اجرای عملیات async در یک حلقه رویداد جدید
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    try:
        # اتصال و ارسال
        loop.run_until_complete(client.start())
        loop.run_until_complete(client.send_message(phone, message))
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
