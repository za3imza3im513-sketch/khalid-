import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 البوت يعمل!\n\n"
        "أرسل /track اسم_حساب_انستغرام لبدء المراقبة."
    )


async def track(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "❌ اكتب اسم الحساب بعد الأمر.\n"
            "مثال:\n"
            "/track instagram"
        )
        return

    username = context.args[0].replace("@", "").strip()

    await update.message.reply_text(
        f"🔎 تم طلب مراقبة الحساب:\n@{username}\n\n"
        "⏳ سنضيف نظام المراقبة في الخطوة التالية."
    )


def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")

    if not token:
        raise RuntimeError("TELEGRAM_BOT_TOKEN غير موجود في Environment Variables")

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("track", track))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
