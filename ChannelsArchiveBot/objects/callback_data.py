from enum import StrEnum, auto


class CallbackData(StrEnum):
    HOME = auto()

    RECCOMEND_CHANNEL = auto()
    CATEGORY_CHANNEL = auto()

    SEARCH = auto()
    QUERY_SEARCH = auto()

    NEXT_PAGE = auto()
    PREVIOUS_PAGE = auto()