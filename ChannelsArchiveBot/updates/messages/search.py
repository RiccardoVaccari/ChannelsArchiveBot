from pyrogram import Client, types
from sqlalchemy.orm import Session

from ChannelsArchiveBot import CHANNELS_PER_PAGE
from ChannelsArchiveBot.database import utils
from ChannelsArchiveBot.database import models
from ChannelsArchiveBot.objects import keyboard, text


def process_query_search_message(client: Client, message: types.Message, session: Session) -> None:

    u = utils.get_user(telegram_user=message.from_user, session=session)

    # 1 & 2)
    channels_by_name = utils.get_channels_by_query(query=message.text, session=session, attribute=models.Channel.name)
    channels_by_description = utils.get_channels_by_query(query=message.text, session=session, attribute=models.Channel.description)

    channels = set(channels_by_name + channels_by_description)

    u.data["query"] = message.text
    u.data["channels"] = [channel.id for channel in channels]
    u.data["index"] = 0
    
    # 3)
    rows = list()
    if u.data["index"] > 0:
        rows.append([keyboard.Button.PREVIOUS_PAGE])
    if (u.data["index"]+CHANNELS_PER_PAGE) <= len(u.data["channels"]):
        try:
            rows[0].append(keyboard.Button.NEXT_PAGE)
        except IndexError:
            rows.append([keyboard.Button.NEXT_PAGE])
    
    rows.append([keyboard.Button.GO_BACK_SEARCH])
    
    reply_markup = types.InlineKeyboardMarkup(rows)

    channels_text = ""

    for i in range(u.data["index"], min(len(u.data["channels"]), (u.data["index"]+CHANNELS_PER_PAGE))):
        channel = utils.get_channel(telegram_channel=u.data["channels"][i], session=session)

        channels_text += (
            "\n📣<a href=\"{link}\">{name}</a>\n"
            "Descripion: {description}\n"
            "Languages: {languages}\n"
            "<a href=\"{message}\">More info</a>\n"
        ).format(
            link=channel.link,
            name=channel.name,
            description=channel.short_description,
            languages=" ".join(channel.languages),
            message=channel.message_link
        )


    results_text = text.Info.PAGE_SEARCH_CHANNEL.format(
        results=len(u.data["channels"]),
        query=u.data["query"],
        channels=channels_text,
        page_number=((u.data["index"] // 3) + 1),
        total_pages=len(u.data["channels"])//CHANNELS_PER_PAGE \
                        if (len(u.data["channels"]) % CHANNELS_PER_PAGE) == 0 \
                        else ((len(u.data["channels"])//CHANNELS_PER_PAGE) + 1)
    )


    message.reply(text=results_text, reply_markup=reply_markup, disable_web_page_preview=True)