from pyrogram import types
from sqlalchemy.orm import Session
import functools

from ChannelsArchiveBot.database import models
from ChannelsArchiveBot.database import SessionLocal


def db_session(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        try:
            session = SessionLocal()
            if kwargs:
                kwargs["session"] = session
            else:
                args += (session,)

            value = func(*args, **kwargs)

        finally:
            session.commit()
            session.close()
        return value
    return wrapper_decorator


# ---- User ---

def get_user(telegram_user: types.User, session: Session) -> models.User:
    return session.query(models.User).filter(models.User.id == str(telegram_user.id)).first()


def create_user(telegram_user: types.User, session: Session) -> models.User:
    new_user = models.User(
        id=telegram_user.id,
        username=telegram_user.username,
        name=telegram_user.first_name,
        first_name=telegram_user.first_name,
        last_name=telegram_user.last_name,
    )

    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user


# ---- Channel ----

def get_channel(telegram_channel: types.Chat | str | int, session: Session) -> models.Channel:
    if not isinstance(telegram_channel, types.Chat):
        return session.query(models.Channel).filter(models.Channel.id == str(telegram_channel)).first()
    return session.query(models.Channel).filter(models.Channel.id == str(telegram_channel.id)).first()


def create_channel(telegram_channel: types.Chat, descritpion: str, tags: list[str], languages: list[str], category: str, telegram_user: types.User, session: Session) -> models.Channel:
    new_channel = models.Channel(
        id=telegram_channel.id,
        name=telegram_channel.title,
        link=telegram_channel.invite_link,
        description=descritpion,
        tags=tags,
        languages=languages,
        photo=telegram_channel.photo.small_file_id if telegram_channel.photo else None,
        category=category,
        members=telegram_channel.members_count,
        owner_id=telegram_user.id
    )

    session.add(new_channel)
    session.commit()
    session.refresh(new_channel)
    return new_channel

def get_not_pubilshed_channels(session: Session, n: int = 3) -> list[models.Channel]:
    return session.query(models.Channel).filter(models.Channel.message == None).order_by(models.Channel.added_on).all()[:n]

# ---- Rating ----

def get_ratings_by_channel(channel: models.Channel | str | int, session: Session) -> list[models.Rating] | None:
    if not isinstance(channel, models.Channel):
        channel = get_channel(telegram_channel=channel, session=session)
    
    return session.query(models.Rating).filter(models.Rating.channel_id == channel.id).all()


# ---- Message ----

def create_message(message_id: int, channel_id: str, session: Session) -> models.Message:
    new_message = models.Message(
        id=message_id,
        channel_id=channel_id
    )

    session.add(new_message)
    session.commit()
    session.refresh(new_message)
    return new_message

def get_message_by_channel(channel: models.Channel | str | int, session: Session) -> models.Message | None:
    if not isinstance(channel, models.Channel):
        channel = get_channel(telegram_channel=channel, session=session)
    
    return session.query(models.Message).filter(models.Message.channel == channel).first()