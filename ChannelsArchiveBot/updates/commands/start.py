from pyrogram import filters, types, Client
from sqlalchemy.orm import Session

from ChannelsArchiveBot import bot
from ChannelsArchiveBot.database import utils
from ChannelsArchiveBot.objects import state, text, keyboard


@bot.on_message(filters.private & filters.command("start"))
@utils.db_session
def process_start_command(client: Client, message: types.Message, session: Session) -> None:
    u = utils.get_user(telegram_user=message.from_user, session=session)
    if not u:
        u = utils.create_user(telegram_user=message.from_user, session=session)

    u.state = state.State.HOME
    u.data = {}

    message.reply(text=text.Info.HOME, reply_markup=keyboard.Keyboard.HOME)
