from ChannelsArchiveBot import BOT_USERNAME, CHANNEL_USERNAME, IMAGE_FLAG


class Text:
    pass


class Info(Text):
    HOME = (
        f"ð£ <b>Welcome to @{CHANNEL_USERNAME}</b> ð£\n\n"
        "â<b>Search</b> and join other <b>channels</b>\n"
        "â<b>Recommend</b> your channel to improve the community and help other users"
    )

    # ---- ADD CHANNEL ----

    RECCOMEND_CHANNEL = (
        "<b>ð Reccomend Channel</b>\n\n"
        "In this section you can <b>reccomend a new channel</b>\n\n"
        "âPrerequisites:\n"
        "â¢ Be an <b>admin</b> of the channel\n"
        "â¢ The channel can't be a <b>redirect channel</b>\n\n"
        "ðFollow these 3 simple steps in order to add the channel:\n"
        f"1. Add @{BOT_USERNAME} to the channel as admin\n"
        "2. Check if the bot has the <i>\"Add members\"</i> premission\n"
        "3. <b><u>Forward</u></b> channel's last message in this chat\n\n"
        "<i><b>Now you can start!</b></i>"
    )

    DESCRIPTION_CHANNEL = (
        "â <b>Connecting Channel</b>\n"
        "âï¸ <b><u>Description</u></b>\n"
        "âï¸ <i>Tags</i>\n"
        "âï¸ <i>Language</i>\n"
        "âï¸ <i>Category</i>\n\n"
        "Now send me the channel's English <b>description</b> (max 100 characters)."
    )

    TAGS_CHANNEL = (
        "â <b>Connecting Channel</b>\n"
        "â <b>Description</b>\n"
        "âï¸ <i><u>Tags</u></i>\n"
        "âï¸ <i>Language</i>\n"
        "âï¸ <i>Category</i>\n\n"
        "Now send me some tags to define your channel and help other users to find it.\n"
        "Every tag must start with <code>#</code> and divided from other by a space.\n"
        "<i>Restrictions: max 10 tags, max 15 characters for each</i>\n\n"
        "ex: #music #spotify #pop"
    )

    LANGUAGE_CHANNEL = (
        "â <b>Connecting Channel</b>\n"
        "â <b>Description</b>\n"
        "â <b>Tags</b>\n"
        "âï¸ <i><u>Language</u></i>\n"
        "âï¸ <i>Category</i>\n\n"
        "Now send me the channel's <b>language</b>. If it has many languages send them separeted by a space.\n\n"
        "ex: English Italian Hungarian"
    )

    CATEGORY_CHANNEL = (
        "â <b>Connecting Channel</b>\n"
        "â <b>Description</b>\n"
        "â <b>Tags</b>\n"
        "â <b>Language</b>\n"
        "âï¸ <i><u>Category</u></i>\n\n"
        "Now choose the channel's category"
    )

    CHANNEL_COMPLETED = (
        "â <b>Connecting Channel</b>\n"
        "â <b>Description</b>\n"
        "â <b>Tags</b>\n"
        "â <b>Language</b>\n"
        "â <b>Category</b>\n\n"
        "You've successfully added <b>{}</b> to our archive!"
    )

    # ---- Publish Channel ----

    PUBLISH_CHANNEL = (
        "<a href=\"{image}\">ð£</a> <b>New Channel</b>\n"
        # "ð£ <b>New Channel</b>\n"
        "<b>â¢ Name:</b> {name}\n"
        "<b>â¢ Link:</b> <a href=\"{link}\">Click here to join!</a>\n"
        "<b>â¢ Rating:</b> {stars} ({rating}/5 on {votes} votes)\n\n"
        "<b>âï¸ Description:</b> {description}\n"
        "<b>ð Languages:</b> {languages}\n"
        "<b>#ï¸â£ Tags:</b> {tags}"
    )

    # ---- Search Channel ----
    SEARCH_CHANNEL = (
        "<b>ð Search Channel</b>\n\n"
        "In this section you can <b>search</b> a channel in our archive"
    )

    # ---- Search Query Channel ----
    QUERY_SEARCH_CHANNEL = (
        "<b>ð Search Channel by query</b>\n\n"
        "Send me keywords to find the channel you're searching"
    )

    PAGE_CHANNELS = (
         "\nð£<a href=\"{link}\">{name}</a>\n"
        "Descripion: {description}\n"
        "Languages: {languages}\n"
        "<a href=\"{message}\">More info</a>\n"
    )

    QUERY_PAGE_SEARCH_CHANNEL = (
        "ð <b>I've found {results} results for <code>{query}</code></b>\n"
        "{channels}\n"
        "<b>Page <i>{page_number}</i> of <i>{total_pages}</i></b>"
    )

    ZERO_PAGE_SEARCH_QUERY = (
        "<b>I've found 0 channels with query: <code>{query}</code></b>"
    )

    # ---- Search Category Channel ----
    CATEGORY_SEARCH_SELECTION = (
        "<b>ð Search Channel by category</b>\n\n"
        "Select one category to find channels related to it"
    )

    CATEGORY_PAGE_SEARCH_CHANNEL = (
        "<b>{category}: {results} results found</b>\n"
        "{channels}\n"
        "<b>Page <i>{page_number}</i> of <i>{total_pages}</i></b>"
    )

    ZERO_PAGE_SEARCH_CATEGORY = (
        "<b>I've found 0 channels in category: {category}</b>"
    )

class Errors(Text):

    SESSION_EXPIRED = (
        "â <b>Error:</b> "
        "This session has expired"
    )

    # ---- Reccomend Channel ----

    CHAT_TYPE_NOT_CHANNEL = (
        "â <b>Error:</b> "
        "The source chat is not a channel"
    )

    BOT_NOT_IN_CHANNEL = (
        "â <b>Error:</b> "
        "You should add this bot to the channel as admin"
    )

    WITHOUT_ADD_MEMBERS_PERM = (
        "â <b>Error:</b> "
        "You should give the <i>\"Add members\"</i> permission to the bot"
    )

    CHANNEL_EXIST = (
        "â <b>Error:</b> "
        "The channel is already in our archive"
    )

    # ---- Description Channel ----

    DESCRIPTION_TOO_LONG = (
        "â <b>Error:</b> "
        "The description is too long, remember max 100 characters"
    )

    # ---- Language Channel ----

    EMPTY_LANGUAGE = (
        "â <b>Error:</b> "
        "You should send at least 1 valid language, the name must be spelled in English"
    )
