from pyrogram import types, Client, enums, errors
from sqlalchemy.orm import Session

from ChannelsArchiveBot import LANGUAGES
from ChannelsArchiveBot.database import utils
from ChannelsArchiveBot.objects import text, keyboard, state


def process_reccomend_channel_message(client: Client, message: types.Message, session: Session) -> None:
    """
    1. Il messaggio non è inoltrato
    2. Il messaggio non è inoltrato da un canale
    3. Il bot non è nel canale
    4. Il bot non è admin del canale (impossibile)
    5. Il bot non ha il permesso "add members"
    6. Il canale è già nel database
    """

    if not message.forward_from_chat or message.forward_from_chat.type != enums.ChatType.CHANNEL:
        message.reply(text=text.Errors.CHAT_TYPE_NOT_CHANNEL,
                      reply_markup=keyboard.Keyboard.CANCEL)
        return

    try:
        telegram_channel: types.Chat = client.get_chat(
            chat_id=message.forward_from_chat.id)
    except errors.ChannelPrivate:
        message.reply(text=text.Errors.BOT_NOT_IN_CHANNEL,
                      reply_markup=keyboard.Keyboard.CANCEL)
        return

    if not telegram_channel.invite_link:
        message.reply(text=text.Errors.WITHOUT_ADD_MEMBERS_PERM,
                      reply_markup=keyboard.Keyboard.CANCEL)
        return

    channel = utils.get_channel(
        telegram_channel=telegram_channel, session=session)

    if channel:
        message.reply(text=text.Errors.CHANNEL_EXIST,
                      reply_markup=keyboard.Keyboard.CANCEL)
        return

    u = utils.get_user(telegram_user=message.from_user, session=session)
    u.state = state.State.DESCRIPTION_CHANNEL
    u.data["channel_id"] = telegram_channel.id

    message.reply(text=text.Info.DESCRIPTION_CHANNEL,
                  reply_markup=keyboard.Keyboard.GO_BACK)


def process_description_channel_message(client: Client, message: types.Message, session: Session) -> None:
    if len(message.text) > 100:
        message.reply(text=text.Errors.DESCRIPTION_TOO_LONG,
                      reply_markup=keyboard.Keyboard.CANCEL)
        return

    u = utils.get_user(telegram_user=message.from_user, session=session)
    u.data["channel_description"] = message.text
    u.state = state.State.TAGS_CHANNEL

    message.reply(text=text.Info.TAGS_CHANNEL,
                  reply_markup=keyboard.Keyboard.GO_BACK)


def process_tags_channel_message(client: Client, message: types.Message, session: Session) -> None:
    tag_list = message.text.split(" ")

    for i, tag in enumerate(tag_list):
        if tag and not tag.startswith("#"):
            tag_list[i] = f"#{tag}"

    tag_list = list(filter(lambda tag: tag != "", tag_list))

    u = utils.get_user(telegram_user=message.from_user, session=session)
    u.data["channel_tags"] = tag_list
    u.state = state.State.LANGUAGE_CHANNEL

    message.reply(text=text.Info.LANGUAGE_CHANNEL,
                  reply_markup=keyboard.Keyboard.GO_BACK)


def process_language_channel_message(client: Client, message: types.Message, session: Session) -> None:
    languages_list = message.text.split(" ")

    languages_list = list(
        filter(lambda language: language != "", languages_list))

    languages_list = [l.capitalize() for l in languages_list]

    languages_list = list(
        filter(lambda language: language in LANGUAGES.values(), languages_list))

    if not languages_list:
        message.reply(text=text.Errors.EMPTY_LANGUAGE,
                      reply_markup=keyboard.Keyboard.CANCEL)
        return

    u = utils.get_user(telegram_user=message.from_user, session=session)
    u.data["channel_language"] = languages_list
    u.state = state.State.HOME

    kbrd = keyboard.Keyboard.CATEGORIES.inline_keyboard + \
        [[keyboard.Button.GO_BACK]]

    message.reply(text=text.Info.CATEGORY_CHANNEL,
                  reply_markup=types.InlineKeyboardMarkup(kbrd))
