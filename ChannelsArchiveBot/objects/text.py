from ChannelsArchiveBot import BOT_USERNAME, CHANNEL_USERNAME


class Text:
    pass


class Info(Text):
    HOME = (
        f"📣 <b>Welcome to @{CHANNEL_USERNAME}</b> 📣\n\n"
        "⇒<b>Search</b> and join other <b>channels</b>\n"
        "⇒<b>Recommend</b> your channel to improve the community and help other users"
    )

    # ---- ADD CHANNEL ----

    RECCOMEND_CHANNEL = (
        "<b>🗃 Reccomend Channel</b>\n\n"
        "In this section you can <b>reccomend a new channel</b>\n\n"
        "❕Prerequisites:\n"
        "• Be an <b>admin</b> of the channel\n"
        "• The channel can't be a <b>redirect channel</b>\n\n"
        "🔗Follow these 3 simple steps in order to add the channel:\n"
        f"1. Add @{BOT_USERNAME} to the channel as admin\n"
        "2. Check if the bot has the <i>\"Add members\"</i> premission\n"
        "3. <b><u>Forward</u></b> channel's last message in this chat\n\n"
        "<i><b>Now you can start!</b></i>"
    )

    DESCRIPTION_CHANNEL = (
        "✅ <b>Connecting Channel</b>\n"
        "☑️ <b><u>Description</u></b>\n"
        "☑️ <i>Tags</i>\n"
        "☑️ <i>Language</i>\n"
        "☑️ <i>Category</i>\n\n"
        "Now send me the channel's English <b>description</b> (max 100 characters)."
    )

    TAGS_CHANNEL = (
        "✅ <b>Connecting Channel</b>\n"
        "✅ <b>Description</b>\n"
        "☑️ <i><u>Tags</u></i>\n"
        "☑️ <i>Language</i>\n"
        "☑️ <i>Category</i>\n\n"
        "Now send me some tags to define your channel and help other users to find it.\n"
        "Every tag must start with <code>#</code> and divided from other by a space.\n"
        "<i>Restrictions: max 10 tags, max 15 characters for each</i>\n\n"
        "ex: #music #spotify #pop"
    )

    LANGUAGE_CHANNEL = (
        "✅ <b>Connecting Channel</b>\n"
        "✅ <b>Description</b>\n"
        "✅ <b>Tags</b>\n"
        "☑️ <i><u>Language</u></i>\n"
        "☑️ <i>Category</i>\n\n"
        "Now send me the channel's <b>language</b>. If it has many languages send them separeted by a space.\n\n"
        "ex: English Italian Hungarian"
    )

    CATEGORY_CHANNEL = (
        "✅ <b>Connecting Channel</b>\n"
        "✅ <b>Description</b>\n"
        "✅ <b>Tags</b>\n"
        "✅ <b>Language</b>\n"
        "☑️ <i><u>Category</u></i>\n\n"
        "Now choose the channel's category"
    )

    CHANNEL_COMPLETED = (
        "✅ <b>Connecting Channel</b>\n"
        "✅ <b>Description</b>\n"
        "✅ <b>Tags</b>\n"
        "✅ <b>Language</b>\n"
        "✅ <b>Category</b>\n\n"
        "You've successfully added <b>{}</b> to our archive!"
    )


class Errors(Text):

    SESSION_EXPIRED = (
        "❌ <b>Error:</b> "
        "This session has expired"
    )

    # ---- Reccomend Channel ----

    CHAT_TYPE_NOT_CHANNEL = (
        "❌ <b>Error:</b> "
        "The source chat is not a channel"
    )

    BOT_NOT_IN_CHANNEL = (
        "❌ <b>Error:</b> "
        "You should add this bot to the channel as admin"
    )

    WITHOUT_ADD_MEMBERS_PERM = (
        "❌ <b>Error:</b> "
        "You should give the <i>\"Add members\"</i> permission to the bot"
    )

    CHANNEL_EXIST = (
        "❌ <b>Error:</b> "
        "The channel is already in our archive"
    )

    # ---- Description Channel ----

    DESCRIPTION_TOO_LONG = (
        "❌ <b>Error:</b> "
        "The description is too long, remember max 100 characters"
    )

    # ---- Language Channel ----

    EMPTY_LANGUAGE = (
        "❌ <b>Error:</b> "
        "You should send at least 1 valid language, the name must be spelled in English"
    )
