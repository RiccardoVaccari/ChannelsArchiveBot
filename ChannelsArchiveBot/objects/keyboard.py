from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from ChannelsArchiveBot.objects.callback_data import CallbackData
from ChannelsArchiveBot.objects.category import Category


class Button(object):
    GO_BACK = InlineKeyboardButton(
        text="🔙 Go Back",
        callback_data=CallbackData.HOME
    )

    CANCEL = InlineKeyboardButton(
        text="🔙 Cancel",
        callback_data=CallbackData.HOME
    )

    SEARCH = InlineKeyboardButton(
        text="🔎 Search",
        callback_data=CallbackData.SEARCH
    )

    RECCOMEND_CHANNEL = InlineKeyboardButton(
        text="🗃 Reccomend Channel",
        callback_data=CallbackData.RECCOMEND_CHANNEL
    )


class Keyboard(object):

    HOME = InlineKeyboardMarkup(
        [
            [Button.SEARCH],
            [Button.RECCOMEND_CHANNEL]
        ]
    )

    GO_BACK = InlineKeyboardMarkup(
        [
            [Button.GO_BACK]
        ]
    )
    CANCEL = InlineKeyboardMarkup(
        [
            [Button.CANCEL]
        ]
    )
    CATEGORIES = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                text=list(Category)[i],
                callback_data=f"{CallbackData.CATEGORY_CHANNEL}-{list(Category)[i]}"
            ), InlineKeyboardButton(
                text=list(Category)[i+1],
                callback_data=f"{CallbackData.CATEGORY_CHANNEL}-{list(Category)[i+1]}"
            )
        ] for i in range(0, len(Category)-1, 2)
    ])
