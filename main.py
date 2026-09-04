import os
from pyrogram import Client, filters

API_ID = int(os.environ.get("API_ID", "123456"))
API_HASH = os.environ.get("API_HASH", "your_api_hash")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "your_bot_token")

app = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text("أهلاً بك! بوت مراقبة إنستغرام يعمل الآن بنجاح 🚀")

print("البوت يعمل الآن ويتصل بتيليجرام...")
app.run()
