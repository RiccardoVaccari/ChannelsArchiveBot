from pyrogram import Client, types, filters, errors
from sqlalchemy.orm import Session

from ChannelsArchiveBot import bot
from ChannelsArchiveBot.database import utils
from ChannelsArchiveBot.objects import callback_data
from ChannelsArchiveBot.objects import state, text, keyboard
from ChannelsArchiveBot.objects.utils import Utils


@bot.on_callback_query(filters.regex(pattern=callback_data.CallbackData.RECCOMEND_CHANNEL))
@utils.db_session
def process_reccomend_channel_query(client: Client, callback_query: types.CallbackQuery, session: Session):
    u = utils.get_user(telegram_user=callback_query.from_user, session=session)

    u.state = state.State.RECCOMEND_CHANNEL

    callback_query.edit_message_text(
        text=text.Info.RECCOMEND_CHANNEL, reply_markup=keyboard.Keyboard.GO_BACK)


@bot.on_callback_query(filters.regex(pattern=f"^{callback_data.CallbackData.CATEGORY_CHANNEL}-(.+)$"))
@utils.db_session
def process_reccomend_channel_query(client: Client, callback_query: types.CallbackQuery, session: Session):
    _, category = callback_query.data.split("-")
    u = utils.get_user(telegram_user=callback_query.from_user, session=session)
    u.data["channel_category"] = category

    try:
        telegram_channel: types.Chat = client.get_chat(
            chat_id=u.data["channel_id"])
        channel = utils.get_channel(
            telegram_channel=telegram_channel, session=session)
        if not channel:

            # if the bot has the "Add Members" permission
            if not telegram_channel.invite_link:
                callback_query.edit_message_text(text=text.Errors.WITHOUT_ADD_MEMBERS_PERM,
                                                 reply_markup=keyboard.Keyboard.CANCEL)
                return

            channel = utils.create_channel(
                telegram_channel=telegram_channel,
                descritpion=u.data["channel_description"],
                tags=u.data["channel_tags"],
                languages=u.data["channel_language"],
                category=u.data["channel_category"],
                telegram_user=callback_query.from_user,
                session=session
            )
    # Session expired
    except KeyError:
        callback_query.edit_message_text(
            text=text.Errors.SESSION_EXPIRED, reply_markup=keyboard.Keyboard.GO_BACK)
        return

    # Bot not in channel
    except errors.ChannelPrivate:
        callback_query.edit_message_text(text=text.Errors.BOT_NOT_IN_CHANNEL,
                                         reply_markup=keyboard.Keyboard.CANCEL)
        return

    callback_query.edit_message_text(
        text=text.Info.CHANNEL_COMPLETED.format(channel.name), reply_markup=keyboard.Keyboard.GO_BACK)

    if channel.photo:
        image = Utils.upload_image(client=client, small_file_id=channel.photo)
        channel.image = image