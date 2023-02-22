from pyrogram import Client, types, filters
from sqlalchemy.orm import Session

from ChannelsArchiveBot import bot
from ChannelsArchiveBot.database import utils
from ChannelsArchiveBot.objects import callback_data
from ChannelsArchiveBot.objects import state, text, keyboard


@bot.on_callback_query(filters.regex(pattern=callback_data.CallbackData.HOME))
@utils.db_session
def process_home_query(client: Client, callback_query: types.CallbackQuery, session: Session) -> None:
    u = utils.get_user(telegram_user=callback_query.from_user, session=session)

    u.state = state.State.HOME
    u.data = {}

    callback_query.edit_message_text(
        text=text.Info.HOME, reply_markup=keyboard.Keyboard.HOME)
