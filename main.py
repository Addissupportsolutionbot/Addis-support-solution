import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = os.getenv("BOT_TOKEN")

# START COMMAND
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["📞 Contact Us", "💼 Services"],
        ["🌐 Website", "❓ Help"]
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "Welcome to Addis Support Solution 🇪🇹\nChoose an option below:",
        reply_markup=reply_markup
    )

# BUTTON REPLIES
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📞 Contact Us":
        await update.message.reply_text(
            "📱 Phone: +251993445794"
        )

    elif text == "💼 Services":
        await update.message.reply_text(
            "We provide:\n- Call Center Services\n- Customer Support\n- AI Chatbots\n- Training"
        )

    elif text == "🌐 Website":
        await update.message.reply_text(
            "Website coming soon 🚀"
        )

    elif text == "❓ Help":
        await update.message.reply_text(
            "Type /start anytime to open the menu."
        )

    else:
        await update.message.reply_text(
            "Please choose an option from the menu."
        )

# MAIN BOT
def main():
    print("Bot is ONLINE now!")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    app.run_polling()

if __name__ == "__main__":
    main()
