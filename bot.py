from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Your bot's token from BotFather
TOKEN = "7760359550:AAGIDakI__sCuxgON4LgHG1tThzvvyvhLmg"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am your bot. How can I assist you today?")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("You can interact with me by sending any message.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # This function will echo back any text message sent by the user.
    await update.message.reply_text(update.message.text)

def main():
    # Set up the bot
    app = Application.builder().token(TOKEN).build()

    # Add command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    # Add a message handler for all text messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user interrupts it
    app.run_polling()

if __name__ == "__main__":
    main()
