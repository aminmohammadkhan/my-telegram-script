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
    
    # خواندن دسترسی از متغیر محیطی (بدون نیاز به فایل)
    creds_dict = json.loads(os.environ['{
  "type": "service_account",
  "project_id": "telegram-bot-project-501010",
  "private_key_id": "8407456c1c650fd8be80c7a38d31ba039916aab9",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDL5o47u/PqpoVM\nYYYm8warSy4TgXjXbdZ/elHY7Sjd41RgS+UN5+jcZ3YdBBI94+f4TkQWlyB2bHeO\nz1sAQ18D9XxYOpv+08jOE2Cp4isNZmidAX+EuFNpopwR0YzBQKTPlB098hwz4sZf\nwH1Uu2fX2NygV05s1kAfviJASHmCBBDp6kI7yfUM5NvVSm8iotMq424IlTp4CKSb\nSkzT7kKrgjhiajZpQEa2+ir/vYjCdlEL/II+lHl6kbeIujB/k9YypMn/RVYCTv7H\nGVibmEZpsiRcthsAQxRbsdTGq/guPCrRegGAGn4/eFj+zcO2AYYFm42Qsw7fbSYK\nqHQPNmibAgMBAAECggEAUB7QVPiN5+53AoRvym5EeJqaCGAfs8cdOgo+jxbhsA7b\n4Nrxrn0qKzEcYFpxMJCVXiSi7J2FzALjF+Kyx2+xrkSQD7s4APIHPbKvkRGmCSXs\nhYVJLkWfwSp8WSQWQvm7yTVSKD0yh9DcUlO468qYC2DTkM29q1ak69QycUAJPuTV\nqpcDOe48JN0KxvmlR5zWdxvE4Kd7QQzTy+iuGOTlAIGBirF8jE0QEf0/TcqYZvEw\nc/E93ELg/gOxk2MbFyjMZKBhT58UXi0vMiCCJZq+UB9M62CtnIURaXWZStvHPc33\nRTKCxQc+joyTzEV0ynXWYOqkP6s3jvo718n9ewSTgQKBgQD8pNLT8+yQDTgAdlL/\nBY5CvSoYPxbAyCNMh6Sq9532wPMYjNRKU1tVst7KNVojhYlUFP+xw8+79uU2ZzKy\nszkOcnBw+0100d48pbpzWp7CadPv/aB37nHB+Qs+8nEZHaj06OJ+Fdlee3TZA7o4\n6s9Uy6qrYoW+4Hc7sytkj8ZlaQKBgQDOm/gJ/J3zUpxl8q9sSKP4zzPtZxMnSn9C\n/ptuycECI+nYYGk8MSgE/Khykxj5s3xh/l3mX+F6JTpOexxNlPbwBHiuvxfjwupN\njKgZH+wJVtDLNYPuphxB8A+dOHbQftQOCJ+0fQDAHZw/33e8lDdabyKJe+GHuR4M\nhMLpwHiJYwKBgQCV0+G8FQKMA2rcy085MkBF0A0wx+lkdsyITEEZqzOg7Ji+THZx\nhbG6xxNc8/r66eyhUrq435lIrYkNlHH6jFMgADoyprYuu2+Co/5I/sr8HOq1fsI1\nndEU6e8Da6Aq9u4GID6B6883Oxv2v0EnFAnVDduvPAR5SIEthHoNbz6HUQKBgFQN\ns90sPn4NL79x+dgNvVetxCxi8LHdZuS0fDuYLMNYJPx4TJfGT8enmkfyfAip8oJT\nX5Qnka2Fk7D1+M+/OK7wwsAk0e1BEN03yfNev0IVZaAmR2RBg+F3boLBw+SSlGaZ\nL4/YAwQlh7mcijPYAKTz7ZMNKPV0ZDsnj7xVJzSNAoGANAEdSU219uNrs3VzAAEu\nEaIqotR3VzMBDRKBn0+vje+2PeBJJPyt/koIi+oNT7zVdpvrl29M2t9OI7b42CIO\nBcdL2vyJkuPEkEvNFEeEwmmbj4eNYhTG7pu81mIE2qqwMdDJuloRkh/wADE+1+id\n56PH4kvMEi4poOsuPMFlfbw=\n-----END PRIVATE KEY-----\n",
  "client_email": "telegram-bot-worker@telegram-bot-project-501010.iam.gserviceaccount.com",
  "client_id": "104072263689929937136",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/telegram-bot-worker%40telegram-bot-project-501010.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}'])
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
# # فایلِ نشست به صورت خودکار خوانده می‌شود
# client = TelegramClient('session', int(os.environ['38107594']), os.environ['41c14c86d3b16088c264fb68cd8fc050'])
if __name__ == '__main__':
    run_worker()
