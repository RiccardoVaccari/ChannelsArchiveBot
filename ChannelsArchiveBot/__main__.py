from ChannelsArchiveBot import (
    BOT_NAME,
    BOT_USERNAME,
    BOT_TOKEN,
    bot
)
from ChannelsArchiveBot.database import engine, models
import ChannelsArchiveBot.updates

if __name__ == "__main__":
    models.Base.metadata.create_all(bind=engine)

    print(f"[INFO]: {BOT_NAME} started!")
    bot.run()
