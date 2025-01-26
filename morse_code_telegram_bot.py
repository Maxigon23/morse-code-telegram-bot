from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram.ext import CallbackContext

from morse_code import encript


async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello! Start by typing something for me to translate into morse code.")

async def help(update: Update, context: CallbackContext):
    await update.message.reply_text("Just type something in the chat, send it to me and i'll translate it into morse code.")

async def answer_morse_code(update: Update, context: CallbackContext):
    username = update.message.from_user.username
    user_message = update.message.text
    print(f"{username} sent {user_message}")
    await update.message.reply_text(encript(user_message))

def main():
    TOKEN = ''

    application = Application.builder().token(TOKEN).build()

    print(f"{application.bot} is now running!")

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, answer_morse_code))

    application.run_polling()

if __name__ == '__main__':
    main()