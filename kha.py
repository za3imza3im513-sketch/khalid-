import os
import asyncio
from pyrogram import Client, filters

# البيانات الرسمية والخاصة بك
API_ID = 1921214471
API_HASH = "Qnbc-zzL1SuuM"
BOT_TOKEN = "6532575243:AAEiCe_EKEvDcuIFsJMKjNQnbc-zzL1SuuM"

app = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text("أهلاً بك! البوت يعمل الآن بنجاح 🚀")

async def main():
    print("البوت يعمل الآن ويتصل بتيليجرام بنجاح!")
    # بدء تشغيل البوت بطريقة متوافقة مع الخوادم
    await app.start()
    # إبقاء البوت قيد التشغيل دون توقف
    await asyncio.Event().wait()

if __name__ == "__main__":
    try:
        # تشغيل الدالة الرئيسية بشكل آمن
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
        
