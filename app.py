import gspread
import time
import os
import json
from telethon import TelegramClient
from telethon.sessions import StringSession
from google.oauth2 import service_account

# تنظیمات کلاینت (مطمئن شو در Variables سایت Railway این‌ها را داری)
client = TelegramClient(StringSession(os.environ['SESSION_STRING']), 
                        int(os.environ['API_ID']), os.environ['API_HASH'])

def run_worker():
    client.start()
    
    # خواندن دسترسی از متغیر محیطی (بدون نیاز به فایل)
    creds_dict = json.loads(os.environ['GOOGLE_CREDENTIALS'])
    creds = service_account.Credentials.from_service_account_info(creds_dict)
    gc = gspread.authorize(creds)
    
    # نام شیت خود را اینجا بنویس
    sh = gc.open("n8n google sheet").sheet1 
    
    print("ربات شروع به کار کرد...")
    
    while True:
        try:
            rows = sh.get_all_records()
            for i, row in enumerate(rows):
                # اگر وضعیت 'done' نبود و شماره‌ای وجود داشت، پیام را بفرست
                if row.get('status') != 'done' and row.get('شماره'):
                    print(f"در حال ارسال به {row['شماره']}...")
                    client.send_message(row['شماره'], f"سلام {row['نام']} {row['نام خانوادگی']}، وقت بخیر")
                    
                    # ثبت وضعیت در ستون D (ستون چهارم)
                    sh.update_cell(i + 2, 4, 'done')
                    time.sleep(10) # تأخیر برای جلوگیری از اسپم
            
        except Exception as e:
            print(f"Error: {e}")
            
        time.sleep(60) # هر یک دقیقه چک کن

if __name__ == '__main__':
    run_worker()
