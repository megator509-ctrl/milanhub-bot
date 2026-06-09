import telebot
import urllib.parse
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

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
    bot.send_message(YOUR_TELEGRAM_ID, f"📢 Nuovo post!\n\n{text}", reply_markup=keyboard)

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot attivo!")
    def log_message(self, format, *args):
        pass

def run_server():
    HTTPServer(("0.0.0.0", 10000), Handler).serve_forever()

threading.Thread(target=run_server, daemon=True).start()
bot.infinity_polling()
