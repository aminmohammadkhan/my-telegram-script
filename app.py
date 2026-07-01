import gspread
import time
import os
import json
from telethon import TelegramClient
from telethon.sessions import StringSession
from google.oauth2 import service_account

# رشته خود را اینجا مستقیماً قرار دهید (مطمئن شوید `=` در انتهای آن باشد)
my_session = "1BJWap1wBu4fLnQ769tuqZyfiL3gHB9IfKkazUWkvdycxNBu6zCHfPlmQLr_UsnoTikVUnMcMXD3QeHbFcc4m6qBIfCMPv0hcqO7L1HtLTv7Yx6vhUJ8YLz0GLwJ1ZPNKAd8apAEbxt9UVGyvXY6qgyKj4aRWeoqMPCNIqd3O84kS2Qtu0LsFJKUPNV1j5lDPTmtJDUEZ04HYJ7gb35aI9b7ft1XqedosOpb-s8_2dnDF08liyj469tojeyXv3l1lg1Tb4B470UubVFZLDdqSyJ5jswo-NyDERC_fw-lD9LQ6Pa2ISybGbrXbW9ap9Mw8EEEfImN6Ib2hWGzC2kE3GsUDM7_kTMc="

client = TelegramClient(StringSession(my_session), int(os.environ['API_ID']), os.environ['API_HASH'])
def run_worker():
    client.start()
    scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]
    # خواندن دسترسی از متغیر محیطی (بدون نیاز به فایل)
    creds = service_account.Credentials.from_service_account_file('credential.json', scopes=scopes)
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
        import os

# این کد مسیرِ دقیقِ فایل را پیدا می‌کند، فارغ از اینکه کد در چه پوشه‌ای اجرا شود
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'credentials.json')
if __name__ == '__main__':
    run_worker()
