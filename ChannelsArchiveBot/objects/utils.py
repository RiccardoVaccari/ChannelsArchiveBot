from pyrogram import types, Client
from imgur_python import Imgur, Exceptions
from os import path, remove

from ChannelsArchiveBot import IMGUR_CLIENT_ID

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
