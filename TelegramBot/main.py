import telegram.ext
from dotenv import load_dotenv
import os


load_dotenv()
TOKEN=os.getenv("TOKEN")
# print(TOKEN)


def start(update,context):
    update.message.reply_text("Hello welcome to pwskillstech bot.")

def help(update,context):
    update.message.reply_text(
        """
        hi there ! I'm Telegram bot created by bappy.plz follow these commands:-

        /start - to start the conversation
        /content - Information about PW Skills
        /contact - Information about contact of PW
        /help - to get this help menu

        I hope these helps.
        """
        )


def content(update,context):
    update.message.reply_text("content page")

def contact(update,context):
    update.message.reply_text("contact page")


def handle_message(update,context):
    update.message.reply_text(f"you said {update.message.text}")

updater=telegram.ext.Updater(TOKEN,use_context=True)
dispatch=updater.dispatcher


dispatch.add_handler(telegram.ext.CommandHandler('start',start))
dispatch.add_handler(telegram.ext.CommandHandler('help',help))
dispatch.add_handler(telegram.ext.CommandHandler('content',content))
dispatch.add_handler(telegram.ext.CommandHandler('contact',contact))
dispatch.add_handler(telegram.ext.CommandHandler(telegram.ext.MessageHandler(telegram.ext.Filters.text,handle_message)))
updater.start_polling()
updater.idle()