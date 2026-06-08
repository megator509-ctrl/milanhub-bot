import logging
import urllib.parse
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, MessageHandler, Filters

BOT_TOKEN = "8994843364:AAGj-MFneDBNqQ3PL2o4JMpbxkSOZzmUuWU"
YOUR_TELEGRAM_ID = 6509006033

logging.basicConfig(level=logging.INFO)

def handle_channel_post(update, context):
    message = update.channel_post
    if not message:
        return
    text = message.text or message.caption or ""
    if not text:
        return
    tweet_text = text[:277] + "..." if len(text) > 280 else text
    encoded_text = urllib.parse.quote(tweet_text)
    twitter_url = f"https://x.com/intent/tweet?text={encoded_text}"
    keyboard = [[InlineKeyboardButton("🐦 Pubblica su X", url=twitter_url)]]
    context.bot.send_message(
        chat_id=YOUR_TELEGRAM_ID,
        text=f"📢 Nuovo post!\n\n{text}",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

updater = Updater(BOT_TOKEN)
updater.dispatcher.add_handler(MessageHandler(Filters.update.channel_posts, handle_channel_post))
updater.start_polling()
updater.idle()
