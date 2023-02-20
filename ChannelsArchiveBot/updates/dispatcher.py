from pyrogram import filters, types, Client
from sqlalchemy.orm import Session

from ChannelsArchiveBot import bot
from ChannelsArchiveBot.database import utils
from ChannelsArchiveBot.objects.state import State
from ChannelsArchiveBot.updates.messages import channel


@bot.on_message(filters.private)
@utils.db_session
def process_message(client: Client, message: types.Message, session: Session) -> None:

    u = utils.get_user(telegram_user=message.from_user, session=session)

    paths = {
        State.RECCOMEND_CHANNEL: channel.process_reccomend_channel_message,
        State.DESCRIPTION_CHANNEL: channel.process_description_channel_message,
        State.TAGS_CHANNEL: channel.process_tags_channel_message,
        State.LANGUAGE_CHANNEL: channel.process_language_channel_message
    }

    if u.state in paths:
        paths[u.state](client, message, session)
