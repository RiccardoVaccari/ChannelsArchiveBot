from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from ChannelsArchiveBot.objects.callback_data import CallbackData
from ChannelsArchiveBot.objects.category import Category


class Button(object):
    GO_BACK = InlineKeyboardButton(
        text="🔙 Go Back",
        callback_data=CallbackData.HOME
    )

    GO_BACK_SEARCH = InlineKeyboardButton(
        text="🔙 Go Back",
        callback_data=CallbackData.SEARCH
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

    QUERY_SEARCH = InlineKeyboardButton(
        text="🔎 Search by query",
        callback_data=CallbackData.QUERY_SEARCH
    )

    CATEGORY_SEARCH = InlineKeyboardButton(
        text="📁 Categories",
        callback_data=CallbackData.CATEGORY_CHANNEL
    )

    NEXT_PAGE = InlineKeyboardButton(
        text="➡️",
        callback_data=CallbackData.NEXT_PAGE
    )

    PREVIOUS_PAGE = InlineKeyboardButton(
        text="⬅️",
        callback_data=CallbackData.PREVIOUS_PAGE
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
    
    GO_BACK_SEARCH = InlineKeyboardMarkup(
        [
            [Button.GO_BACK_SEARCH]
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

    SEARCH_OPTIONS = InlineKeyboardMarkup([
        [Button.QUERY_SEARCH],
        [Button.CATEGORY_SEARCH],
        [Button.GO_BACK]
    ])

    