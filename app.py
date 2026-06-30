import os
from flask import Flask, request, jsonify
from telethon import TelegramClient
from telethon.sessions import StringSession

app = Flask(__name__)

# دریافت تنظیمات از متغیرهای محیطی Render
API_ID = int(os.environ.get('API_ID'))
API_HASH = os.environ.get('API_HASH')
SESSION_STRING = os.environ.get('SESSION_STRING', '')

# ایجاد کلاینت با سشنِ استرینگ (برای پایداری)
client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

@app.route('/send', methods=['POST'])
async def send_message():
    data = request.json
    phone = data.get('phone')
    message = data.get('message')
    
    try:
        await client.send_message(phone, message)
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# استارت کلاینت قبل از اجرای وب‌سرور
if __name__ == '__main__':
    client.start()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
