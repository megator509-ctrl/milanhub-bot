import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import urllib.parse

# CONFIG
BOT_TOKEN = "8994843364:AAGj-MFneDBNqQ3PL2o4JMpbxkSOZzmUuWU"
CHANNEL_USERNAME = "@MilanHubOff"
YOUR_TELEGRAM_ID = "6509006033"

logging.basicConfig(level=logging.INFO)

async def handle_channel_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.channel_post

    if not message:
        return

    # Prendi il testo del post
    text = message.text or message.caption or ""

    if not text:
        return

    # Prepara il testo per X (max 280 caratteri)
    tweet_text = text[:277] + "..." if len(text) > 280 else text

    # Crea il link diretto alla composizione del tweet
    encoded_text = urllib.parse.quote(tweet_text)
    twitter_url = f"https://x.com/intent/tweet?text={encoded_text}"

    # Bottone che apre X con il testo già pronto
    keyboard = [[InlineKeyboardButton("🐦 Pubblica su X", url=twitter_url)]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Manda il messaggio privato a te
    await context.bot.send_message(
        chat_id=YOUR_TELEGRAM_ID,
        text=f"📢 Nuovo post sul canale!\n\n{text}\n\n👆 Clicca il bottone per pubblicare su X",
        reply_markup=reply_markup
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.ChatType.CHANNEL, handle_channel_post))
    print("Bot avviato!")
    app.run_polling()

if __name__ == "__main__":
    main()
