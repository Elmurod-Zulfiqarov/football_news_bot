#!/usr/bin/env python
# pylint: disable=C0116,W0613


import logging
import requests
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
	format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
	"""Send a message when the command /start is issued."""
	user = update.effective_user
	update.message.reply_markdown_v2(
		f'URL tashla'
	)


def help_command(update: Update, context: CallbackContext) -> None:
	"""Send a message when the command /help is issued."""
	update.message.reply_text('Help!')


def url(update: Update, context: CallbackContext) -> None:
	"""Echo the user message."""
	import requests
	from bs4 import BeautifulSoup
	url = "https://sports.uz/news/football"
	page = requests.get(url)

	soup = BeautifulSoup(page.content, "html.parser")


	news_latest = soup.find("div", class_="news-list").find("div", class_="item")

	news_img = news_latest.find("div", class_="img-block").find("img")["data-src"]
	print(news_img)

	news_link = "https://sports.uz" + news_latest.find("div", class_="img-block").find("a").get("href")
	print(news_link)

	news_title = news_latest.find("div", class_="news-body").find("h3").text
	print(news_title)

	channel_id = [-1001597037892]
	context.bot.send_photo(chat_id=channel_id[0], photo=news_img, caption=f"{news_title} \n\n {news_link}")

def main() -> None:
	"""Start the bot."""
	# Create the Updater and pass it your bot's token.
	updater = Updater("5461385912:AAElaZu8JD376PCJTVvVsvhp9UmnxeJk_tQ")

	# Get the dispatcher to register handlers
	dispatcher = updater.dispatcher

	# on different commands - answer in Telegram
	dispatcher.add_handler(CommandHandler("start", start))

	# on non command i.e message - echo the message on Telegram
	dispatcher.add_handler(MessageHandler(
		Filters.text & ~Filters.command, url))

	# Start the Bot
	updater.start_polling()
	
	updater.idle()


if __name__ == '__main__':
	main()

