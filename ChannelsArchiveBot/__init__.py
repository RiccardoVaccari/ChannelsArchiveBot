from pyrogram import Client, types
from apscheduler.schedulers.background import BackgroundScheduler
import json

from ChannelsArchiveBot.development_config import Config

IMGUR_CLIENT_ID = Config.IMGUR_CLIENT_ID
IMAGE_FLAG = Config.IMAGE_FLAG

CHANNEL_USERNAME = Config.CHANNEL_USERNAME
CHANNEL_ID = Config.CHANNEL_ID

API_ID = Config.API_ID
API_HASH = Config.API_HASH
DB_URI = Config.DATABASE_URL

BOT_TOKEN = Config.BOT_TOKEN

LANGUAGES: dict[str, str] = json.load(open(Config.LANGUAGE_FILENAME))

scheduler = BackgroundScheduler()
bot = Client(name="ChannelsArchiveBot", api_id=API_ID,
             api_hash=API_HASH, bot_token=BOT_TOKEN)

print("[INFO]: Getting Bot Info...")
bot.start()
bot_user: types.User = bot.get_me()
BOT_ID = bot_user.id
BOT_USERNAME = bot_user.username
BOT_NAME = bot.name
bot.stop()
