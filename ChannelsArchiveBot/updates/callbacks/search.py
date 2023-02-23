from pyrogram import Client, types, filters
from sqlalchemy.orm import Session

from ChannelsArchiveBot import bot, CHANNELS_PER_PAGE 
from ChannelsArchiveBot.objects import callback_data, text, keyboard, state
from ChannelsArchiveBot.database import utils, models
from ChannelsArchiveBot.objects.utils import Utils

@bot.on_callback_query(filters.regex(pattern=f"^{callback_data.CallbackData.SEARCH}$"))
@utils.db_session
def process_search_query(client: Client, callback_query: types.CallbackQuery, session: Session) -> None:
    u = utils.get_user(telegram_user=callback_query.from_user, session=session)

    u.state = state.State.HOME
    u.data = {}

    callback_query.edit_message_text(text=text.Info.SEARCH_CHANNEL, reply_markup=keyboard.Keyboard.SEARCH_OPTIONS)


# ---- QUERY ----

@bot.on_callback_query(filters.regex(pattern=f"{callback_data.CallbackData.QUERY_SEARCH}"))
@utils.db_session
def process_query_search_query(client: Client, callback_query: types.CallbackQuery, session: Session) -> None:
    u = utils.get_user(telegram_user=callback_query.from_user, session=session)

    u.state = state.State.SEARCH_QUERY
    u.data = {}

    callback_query.edit_message_text(text=text.Info.QUERY_SEARCH_CHANNEL, reply_markup=keyboard.Keyboard.GO_BACK_SEARCH)


# ---- CATEGORY ----

@bot.on_callback_query(filters.regex(pattern=f"^{callback_data.CallbackData.CATEGORY_SEARCH}$"))
def process_category_search_query(client: Client, callback_query: types.CallbackQuery) -> None:
    callback_query.edit_message_text(text=text.Info.CATEGORY_SEARCH_SELECTION, reply_markup=keyboard.Keyboard.SEARCH_CATEGORIES)


@bot.on_callback_query(filters.regex(pattern=f"^{callback_data.CallbackData.CATEGORY_SEARCH_SELECTION}-(.+)$"))
@utils.db_session
def process_category_search_selection_query(client: Client, callback_query: types.CallbackQuery, session: Session) -> None:
    _, category = callback_query.data.split("-")
    u = utils.get_user(telegram_user=callback_query.from_user, session=session)
    u.state = state.State.CATEGORY_SEARCH

    channels = utils.get_channels_by_query(query=category, session=session, attribute=models.Channel.category)

    u.data["category"] = category
    u.data["channels"] = [channel.id for channel in channels]
    u.data["index"] = 0


    reply_markup = keyboard.Keyboard.PAGES_CONTROL(index=u.data["index"], channels=u.data["channels"])

    channels_text = Utils.get_channels_text(data=u.data, session=session)

    callback_query.edit_message_text(text=Utils.get_category_page_text(data=u.data, channels_text=channels_text), reply_markup=reply_markup, disable_web_page_preview=True)

    
@bot.on_callback_query(filters.regex(pattern=f"{callback_data.CallbackData.NEXT_PAGE}|{callback_data.CallbackData.PREVIOUS_PAGE}"))
@utils.db_session
def process_pages_query(client: Client, callback_query: types.CallbackQuery, session: Session) -> None:
    u = utils.get_user(telegram_user=callback_query.from_user, session=session)

    try:
        if callback_query.data == callback_data.CallbackData.NEXT_PAGE:
            u.data["index"] += CHANNELS_PER_PAGE
        elif callback_query.data == callback_data.CallbackData.PREVIOUS_PAGE:
            u.data["index"] -= CHANNELS_PER_PAGE
    except KeyError:
        callback_query.edit_message_text(
            text=text.Errors.SESSION_EXPIRED, reply_markup=keyboard.Keyboard.GO_BACK)
        return

    reply_markup = keyboard.Keyboard.PAGES_CONTROL(index=u.data["index"], channels=u.data["channels"])

    channels_text = Utils.get_channels_text(data=u.data, session=session)

    page_text_dispatcher = {
        state.State.SEARCH_QUERY_RESULT: Utils.get_query_page_text,
        state.State.CATEGORY_SEARCH: Utils.get_category_page_text,
    }
    
    callback_query.edit_message_text(text=page_text_dispatcher[u.state](u.data, channels_text=channels_text), reply_markup=reply_markup, disable_web_page_preview=True)
