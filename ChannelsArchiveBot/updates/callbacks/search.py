from pyrogram import Client, types, filters, errors
from sqlalchemy.orm import Session

from ChannelsArchiveBot import bot
from ChannelsArchiveBot.objects import callback_data, text, keyboard, state
from ChannelsArchiveBot.database import utils

@bot.on_callback_query(filters.regex(pattern=f"^{callback_data.CallbackData.SEARCH}$"))
def process_search_query(client: Client, callback_query: types.CallbackQuery) -> None:
    callback_query.edit_message_text(text=text.Info.SEARCH_CHANNEL, reply_markup=keyboard.Keyboard.SEARCH_OPTIONS)


@bot.on_callback_query(filters.regex(pattern=f"{callback_data.CallbackData.QUERY_SEARCH}"))
@utils.db_session
def process_query_search_query(client: Client, callback_query: types.CallbackQuery, session: Session) -> None:
    u = utils.get_user(telegram_user=callback_query.from_user, session=session)

    u.state = state.State.SEARCH_QUERY
    u.data = {}

    callback_query.edit_message_text(text=text.Info.QUERY_SEARCH_CHANNEL, reply_markup=keyboard.Keyboard.GO_BACK_SEARCH)