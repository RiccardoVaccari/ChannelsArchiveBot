from pyrogram import Client, types
from ChannelsArchiveBot.config import Config
import json

CHANNEL_USERNAME = Config.CHANNEL_USERNAME

API_ID = Config.API_ID
API_HASH = Config.API_HASH
DB_URI = Config.DATABASE_URL

BOT_TOKEN = Config.BOT_TOKEN

LANGUAGES: dict[str, str] = json.load(open(Config.LANGUAGE_FILENAME))

bot = Client(name="ChannelsArchiveBot", api_id=API_ID,
             api_hash=API_HASH, bot_token=BOT_TOKEN)

print("[INFO]: Getting Bot Info...")
bot.start()
bot_user: types.User = bot.get_me()
BOT_ID = bot_user.id
BOT_USERNAME = bot_user.username
BOT_NAME = bot.name
bot.stop()
