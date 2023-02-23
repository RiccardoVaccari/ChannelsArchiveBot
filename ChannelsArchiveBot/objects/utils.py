from pyrogram import Client
from imgur_python import Imgur, Exceptions
from os import path, remove
from sqlalchemy.orm import Session

from ChannelsArchiveBot import IMGUR_CLIENT_ID, CHANNELS_PER_PAGE
from ChannelsArchiveBot.objects import text
from ChannelsArchiveBot.database import utils

class Utils(object):

    @staticmethod
    def upload_image(client: Client, small_file_id: str) -> str:
        photo_path = client.download_media(small_file_id, file_name=small_file_id)

        imgur_client = Imgur(config={"client_id": IMGUR_CLIENT_ID})
        try:
            image = imgur_client.image_upload(
                filename=path.realpath(photo_path),
                title=small_file_id,
                description=small_file_id
            )
        except Exceptions.ImgurException:
            return

        finally:
            remove(photo_path)

        if image["status"] == 200:
            return image["response"]["data"]["link"]
        return

    @staticmethod
    def get_query_page_text(data: dict, channels_text: str) -> str:
        if channels_text:
            return text.Info.QUERY_PAGE_SEARCH_CHANNEL.format(
                results=len(data["channels"]),
                query=data["query"],
                channels=channels_text,
                page_number=((data["index"] // CHANNELS_PER_PAGE) + 1),
                total_pages=len(data["channels"])//CHANNELS_PER_PAGE \
                                if (len(data["channels"]) % CHANNELS_PER_PAGE) == 0 \
                                else ((len(data["channels"])//CHANNELS_PER_PAGE) + 1)
            )
        
        return text.Info.ZERO_PAGE_SEARCH_QUERY.format(query=data["query"])

    @staticmethod
    def get_category_page_text(data: dict, channels_text: str) -> str:
        if channels_text:
            return text.Info.CATEGORY_PAGE_SEARCH_CHANNEL.format(
                category=data["category"],
                results=len(data["channels"]),
                channels=channels_text,
                page_number=((data["index"] // CHANNELS_PER_PAGE) + 1),
                total_pages=len(data["channels"])//CHANNELS_PER_PAGE \
                                if (len(data["channels"]) % CHANNELS_PER_PAGE) == 0 \
                                else ((len(data["channels"])//CHANNELS_PER_PAGE) + 1)
            )
        
        return text.Info.ZERO_PAGE_SEARCH_CATEGORY.format(category=data["category"])


    @staticmethod
    def get_channels_text(data: dict, session: Session) -> str:
        channels_text = ""

        for i in range(data["index"], min(len(data["channels"]), (data["index"]+CHANNELS_PER_PAGE))):
            channel = utils.get_channel(telegram_channel=data["channels"][i], session=session)

            channels_text += text.Info.PAGE_CHANNELS.format(
                link=channel.link,
                name=channel.name,
                description=channel.short_description,
                languages=" ".join(channel.languages),
                message=channel.message_link
            )
        
        return channels_text