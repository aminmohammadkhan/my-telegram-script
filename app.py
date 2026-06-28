import os
import logging
from flask import Flask, request, jsonify
from telethon.sync import TelegramClient
from telethon.errors import (
    PhoneNumberInvalidError,
    UserIsBlockedError,
    PeerIdInvalidError,
    FloodWaitError
)
import asyncio
from functools import wraps

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

API_ID = os.environ.get('API_ID')
API_HASH = os.environ.get('API_HASH')
PHONE_NUMBER = os.environ.get('PHONE_NUMBER')
SESSION_NAME = os.environ.get('SESSION_NAME', 'n8n_telegram_session')

if not all([API_ID, API_HASH, PHONE_NUMBER]):
    raise ValueError("Missing required environment variables")

client = TelegramClient(SESSION_NAME, int(API_ID), API_HASH)

def async_route(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return asyncio.run(f(*args, **kwargs))
    return wrapper

@app.route('/sendTelegram', methods=['POST'])
@async_route
async def send_telegram():
    data = request.get_json()
    user_id = data.get('user_id')
    text = data.get('text')
    
    if not client.is_connected():
        await client.connect()
            
    try:
        message = await client.send_message(user_id, text)
        return jsonify({"success": True, "message_id": message.id}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/authenticate', methods=['POST'])
@async_route
async def authenticate():
    await client.connect()
    await client.send_code_request(PHONE_NUMBER)
    return jsonify({"message": "Code sent to Telegram"}), 200

@app.route('/verify', methods=['POST'])
@async_route
async def verify():
    code = request.get_json().get('code')
    await client.connect()
    await client.sign_in(PHONE_NUMBER, code)
    return jsonify({"message": "Success"}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
