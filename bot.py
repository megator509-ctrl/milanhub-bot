import logging
import urllib.parse
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = "8994843364:AAGj-MFneDBNqQ3PL2o4JMpbxkSOZzmUuWU"
YOUR_TELEGRAM_ID = 6509006033

logging.basicConfig(level=logging.INFO)

async def handle_channel_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
    await context.bot.send_message(
        chat_id=YOUR_TELEGRAM_ID,
        text=f"📢 Nuovo post!\n\n{text}",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.ChatType.CHANNEL, handle_channel_post))
app.run_polling()
