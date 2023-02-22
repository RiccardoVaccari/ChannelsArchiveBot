from pyrogram import Client, types, filters
from sqlalchemy.orm import Session

from ChannelsArchiveBot import bot
from ChannelsArchiveBot.database import utils


@bot.on_callback_query(filters.regex(pattern="[1-5]\|-?[0-9]+"))
@utils.db_session
def process_rating_query(client: Client, callback_query: types.CallbackQuery, session: Session) -> None:
    rate, channel_id = callback_query.data.split("|")

    rating = utils.get_rating(user=callback_query.from_user.id, channel=channel_id, session=session)
    if not rating:
        utils.create_rating(
            user=callback_query.from_user.id,
            channel=channel_id,
            rate=int(rate),
            session=session
        )
    else:
        rating.rate = int(rate)
        
    callback_query.answer(text=f"You voted {rate} ⭐")