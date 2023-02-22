from pyrogram import types
from sqlalchemy.orm import Session

from ChannelsArchiveBot import bot, CHANNEL_ID, IMAGE_FLAG
from ChannelsArchiveBot.database import utils
from ChannelsArchiveBot.objects import text

@utils.db_session
def publish_channel(session: Session) -> None:
    # 1)
    channels = utils.get_not_pubilshed_channels(session=session)
    
    for channel in channels:
        # 2)
        publish_text = text.Info.PUBLISH_CHANNEL.format(
            image=channel.image if IMAGE_FLAG else None,
            name=channel.name,
            link=channel.link,
            stars="⭐️" * int(channel.average_rating),
            rating=channel.average_rating,
            votes=channel.votes,
            description=channel.description,
            languages=" ".join(channel.languages),
            tags=" ".join(channel.tags)
        )

        # 3)
        rows = list()
        for i in range(5):
            button = types.InlineKeyboardButton(
                text=f"{i+1} ⭐️",
                callback_data=f"{i+1}|{channel.id}"
            )
            try:
                rows[i//3].append(button)
            except IndexError:
                rows.append([button])
            
        keyboard = types.InlineKeyboardMarkup(rows)

        # 4)
        message = bot.send_message(chat_id=CHANNEL_ID, text=publish_text, disable_web_page_preview=((channel.image == None) and not IMAGE_FLAG), reply_markup=keyboard)

        # 5)
        if not utils.get_message_by_channel(channel=channel, session=session):
            utils.create_message(message_id=message.id, channel_id=channel.id, session=session)

