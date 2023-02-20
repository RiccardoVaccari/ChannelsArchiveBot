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


def get_channel(telegram_channel: types.Chat, session: Session) -> models.Channel:
    return session.query(models.Channel).filter(models.Channel.id == str(telegram_channel.id)).first()


def create_channel(telegram_channel: types.Chat, descritpion: str, tags: list[str], languages: list[str], category: str, telegram_user: types.User, session: Session) -> models.Channel:
    new_channel = models.Channel(
        id=telegram_channel.id,
        name=telegram_channel.title,
        link=telegram_channel.invite_link,
        description=descritpion,
        tags=tags,
        languages=languages,
        photo=telegram_channel.photo.big_file_id if telegram_channel.photo else None,
        category=category,
        members=telegram_channel.members_count,
        owner_id=telegram_user.id
    )

    session.add(new_channel)
    session.commit()
    session.refresh(new_channel)
    return new_channel
