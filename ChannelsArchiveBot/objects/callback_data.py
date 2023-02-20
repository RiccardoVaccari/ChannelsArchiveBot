from enum import StrEnum, auto


class CallbackData(StrEnum):
    HOME = auto()
    SEARCH = auto()
    RECCOMEND_CHANNEL = auto()
    CATEGORY_CHANNEL = auto()
