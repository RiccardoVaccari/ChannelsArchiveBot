from sqlalchemy import Boolean, ForeignKey, Integer, String, JSON, DateTime, ARRAY, func, select
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.orm import Session, Mapped, mapped_column
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.ext.hybrid import hybrid_method
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime
from statistics import mean
from enum import StrEnum

from sqlalchemy.sql import case

from ChannelsArchiveBot.objects.state import State
from ChannelsArchiveBot import SHORT_DESCRIPTION_LEN, CHANNEL_USERNAME


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[String] = mapped_column(
        "id", String, primary_key=True, index=True)
    username: Mapped[String] = mapped_column(
        "username", String, index=True, nullable=True)
    first_name: Mapped[String] = mapped_column("first_name", String)
    last_name: Mapped[String] = mapped_column(
        "last_name", String, nullable=True)
    name: Mapped[String] = mapped_column("name", String)
    description: Mapped[String] = mapped_column(
        "description", String, nullable=True)
    _state: Mapped[String] = mapped_column("state", String)
    data: Mapped[JSON] = mapped_column(
        "data", MutableDict.as_mutable(JSON), default={})

    channels: Mapped[list["Channel"]] = relationship(
        back_populates="owner")

    def __init__(self, id: int, username: str | None, name: str, first_name: str, last_name: str | None = None, description: str | None = None, data: dict | None = {}, state: StrEnum = State.HOME) -> None:
        self.id = str(id)
        self.username = username
        self.name = name
        self.first_name = first_name
        self.last_name = last_name
        self.description = description
        self.data = data
        self._state = state

    @hybrid_property
    def state(self) -> Mapped[str]:
        return self._state

    @state.setter
    def state(self, new_state: str | StrEnum) -> None:
        self._state = str(new_state)

    def __repr__(self) -> str:
        return f"[{self.id}] @{self.username} | {self.name}"


class Channel(Base):
    __tablename__ = "channels"

    id: Mapped[str] = mapped_column(
        "id", String, primary_key=True, index=True)
    name: Mapped[str] = mapped_column("name", String)
    link: Mapped[str] = mapped_column("link", String, unique=True)
    is_online: Mapped[bool] = mapped_column("is_online", Boolean, default=True)
    description: Mapped[str] = mapped_column(
        "description", String)
    tags: Mapped[list[str]] = mapped_column("tags", ARRAY(String))
    languages: Mapped[list[str]] = mapped_column(
        "languages", ARRAY(String))
    photo: Mapped[str] = mapped_column("photo", String, nullable=True)
    image: Mapped[str] = mapped_column(
        "image", String, nullable=True, default=None)
    category: Mapped[str] = mapped_column(
        "category", String)
    members: Mapped[int] = mapped_column("members", Integer)
    added_on: Mapped[datetime] = mapped_column(
        "added_on", DateTime, default=datetime.now())
    last_message: Mapped[datetime] = mapped_column(
        "last_message", DateTime, default=datetime.now())

    owner_id: Mapped[str] = mapped_column(
        "owner_id", String, ForeignKey("users.id"))
    owner: Mapped["User"] = relationship(back_populates="channels")

    message: Mapped["Message"] = relationship(back_populates="channel")
    ratings: Mapped[list["Rating"]] = relationship(
        back_populates="channel", viewonly=True)

    def __init__(self, id: int, name: str, link: str, description: str, tags: list[str], languages: list[str], photo: str | None, category: str, members: int, owner_id: int) -> None:
        self.id = str(id)
        self.name = name
        self.link = link
        self.description = description
        self.tags = tags
        self.languages = languages
        self.photo = photo
        self.category = category
        self.members = members
        self.owner_id = str(owner_id)

    def __repr__(self) -> str:
        return f"[{self.id}] {self.name} | {self.link} ({self.members} members)"

    @hybrid_property
    def short_description(self) -> str:
        return self.description \
            if len(self.description) <= SHORT_DESCRIPTION_LEN \
            else f"{self.description[:SHORT_DESCRIPTION_LEN]}..."

    @hybrid_property
    def message_link(self) -> str | None:
        return None \
            if not self.message \
            else f"http://t.me/{CHANNEL_USERNAME}/{self.message.id}"

    @hybrid_property
    def average_rating(self) -> float:
        if self.ratings:
            return mean([rating.rate for rating in self.ratings])
        else:
            return 0

    @average_rating.expression
    def average_rating(cls) -> float:
        return case(
            (
                select(func.count()).select_from(Rating).where(Rating.channel_id == cls.id).as_scalar() > 0,
                select(func.avg(Rating.rate)).where(Rating.channel_id == cls.id).as_scalar()
            ),
            else_=0
        )

    @hybrid_property
    def votes(self) -> int:
        return len(self.ratings)


class Rating(Base):
    __tablename__ = "ratings"

    user_id: Mapped[str] = mapped_column(
        "user_id", String, primary_key=True)
    channel_id: Mapped[str] = mapped_column(
        "channel_id", String, ForeignKey("channels.id"), primary_key=True)
    rate: Mapped[int] = mapped_column("rate", Integer)

    channel: Mapped["Channel"] = relationship(
        back_populates="ratings", viewonly=True)

    def __init__(self, user_id: int, channel_id: int, rate: int) -> None:
        self.user_id = str(user_id)
        self.channel_id = str(channel_id)
        self.rate = rate


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column("id", Integer, primary_key=True)
    last_update: Mapped[datetime] = mapped_column(
        "last_update", DateTime, default=datetime.now())
    channel_id: Mapped[str] = mapped_column(
        "channel_id", String, ForeignKey("channels.id"))

    channel: Mapped["Channel"] = relationship(back_populates="message")

    def __init__(self, id: int, channel_id: int | str) -> None:
        self.id = id
        self.channel_id = str(channel_id)
