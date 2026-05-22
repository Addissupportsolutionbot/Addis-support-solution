async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "contact" in text:
        await update.message.reply_text(
            "📱 Phone: +251900000000"
        )

    elif "service" in text:
        await update.message.reply_text(
            "We provide:\n- Call Center Services\n- Customer Support\n- AI Chatbots\n- Training"
        )

    elif "website" in text:
        await update.message.reply_text(
            "Website coming soon 🚀"
        )

    elif "help" in text:
        await update.message.reply_text(
            "Type /start anytime to open the menu."
        )

    else:
        await update.message.reply_text(
            "Please choose a button from the menu."
        )
