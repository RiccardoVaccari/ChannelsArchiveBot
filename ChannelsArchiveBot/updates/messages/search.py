from pyrogram import Client, types
from sqlalchemy.orm import Session

from ChannelsArchiveBot import CHANNELS_PER_PAGE
from ChannelsArchiveBot.database import utils
from ChannelsArchiveBot.database import models
from ChannelsArchiveBot.objects import keyboard, state
from ChannelsArchiveBot.objects.utils import Utils


def process_query_search_message(client: Client, message: types.Message, session: Session) -> None:

    u = utils.get_user(telegram_user=message.from_user, session=session)
    u.state = state.State.SEARCH_QUERY_RESULT

    # 1 & 2)
    channels_by_name = utils.get_channels_by_query(query=message.text, session=session, attribute=models.Channel.name)
    channels_by_description = utils.get_channels_by_query(query=message.text, session=session, attribute=models.Channel.description)

    channels = set(channels_by_name + channels_by_description)

    u.data["query"] = message.text
    u.data["channels"] = [channel.id for channel in channels]
    u.data["index"] = 0
    
    # 3)
    reply_markup = keyboard.Keyboard.PAGES_CONTROL(index=u.data["index"], channels=u.data["channels"])

    channels_text = Utils.get_channels_text(data=u.data, session=session)

    message.reply(text=Utils.get_query_page_text(data=u.data, channels_text=channels_text), reply_markup=reply_markup, disable_web_page_preview=True)