import requests
import re
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TELEGRAM_BOT_TOKEN = '6689106743:AAFwsV2CClSpoEJqUsG_uXfvxVDh3x3AZeA'

BASE_URL = 'https://berry-chill-wallflower.glitch.me/dec'

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Proporcione el SSH para decodificar.")

def process_text(update: Update, context: CallbackContext):
    
    text = update.message.text
    chat_id = update.message.chat_id  
    message_id = update.message.message_id  

    response = requests.get(BASE_URL, params={'cipher': text})

    if response.status_code == 200:
        
        dec_content = response.text
        dec_content = add_p_tags_to_content(dec_content)  

        response_text = f"𝐒𝐒𝐇 𝐃𝐄𝐂𝐑𝐘𝐏𝐓𝐎𝐑\n━━━━━━━━━━━━━━━━━━━━━━━━\n 𝐆𝐑𝐎𝐔𝐏 : t.me/file_decryptors\n━━━━━━━━━━━━━━━━━━━━━━━━\n{dec_content}\n━━━━━━━━━━━━━━━━━━━━━━━━\n*"
        context.bot.send_message(chat_id=chat_id, text=response_text, reply_to_message_id=message_id)
    else:
        update.message.reply_text("Error getting result.")

def add_p_tags_to_content(content):

    lines = content.split('\n')
    formatted_content = '\n'.join([f'[*] SSH: {line}' for line in lines if line.strip()])
    return formatted_content

def main():
    updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, process_text))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()