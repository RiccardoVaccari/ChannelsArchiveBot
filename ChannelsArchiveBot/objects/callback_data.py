from enum import StrEnum, auto


class CallbackData(StrEnum):
    HOME = auto()

    RECCOMEND_CHANNEL = auto()
    CATEGORY_CHANNEL = auto()

    SEARCH = auto()
    QUERY_SEARCH = auto()
    CATEGORY_SEARCH = auto()
    CATEGORY_SEARCH_SELECTION = auto()

    NEXT_PAGE = auto()
    PREVIOUS_PAGE = auto()

