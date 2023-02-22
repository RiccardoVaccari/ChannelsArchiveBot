from enum import StrEnum, auto


class State(StrEnum):
    HOME = auto()

    RECCOMEND_CHANNEL = auto()
    DESCRIPTION_CHANNEL = auto()
    TAGS_CHANNEL = auto()
    LANGUAGE_CHANNEL = auto()

    SEARCH_QUERY = auto()

