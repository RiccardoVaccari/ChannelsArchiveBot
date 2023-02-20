from ChannelsArchiveBot import (
    BOT_NAME,
    BOT_USERNAME,
    BOT_TOKEN,
    bot,
    scheduler
)
from ChannelsArchiveBot.database import engine, models
from ChannelsArchiveBot import updates

if __name__ == "__main__":
    models.Base.metadata.create_all(bind=engine)

    scheduler.add_job(updates.schedulers.publish_channel, "cron", hour="9,19", minute=0, second=0)
    scheduler.start()

    print(f"[INFO]: {BOT_NAME} started!")
    # bot.start()
    
    # bot.stop()
    bot.run()
