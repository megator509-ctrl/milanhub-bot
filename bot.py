import telebot
import urllib.parse

BOT_TOKEN = "8994843364:AAGj-MFneDBNqQ3PL2o4JMpbxkSOZzmUuWU"
YOUR_TELEGRAM_ID = 6509006033

bot = telebot.TeleBot(BOT_TOKEN)

@bot.channel_post_handler(content_types=['text'])
def handle_channel_post(message):
    text = message.text or ""
    if not text:
        return
    tweet_text = text[:277] + "..." if len(text) > 280 else text
    encoded_text = urllib.parse.quote(tweet_text)
    twitter_url = f"https://x.com/intent/tweet?text={encoded_text}"
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton("🐦 Pubblica su X", url=twitter_url))
    bot.send_message(
        YOUR_TELEGRAM_ID,
        f"📢 Nuovo post!\n\n{text}",
        reply_markup=keyboard
    )

bot.infinity_polling()
