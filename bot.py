# bot.py
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Define a command handler
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your bot.')

# Define a message handler
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def main() -> None:
    # Replace 'YOUR_TOKEN' with your bot's token
    updater = Updater("YOUR_TOKEN")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()