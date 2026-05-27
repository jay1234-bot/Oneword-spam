from pyrogram.types import InlineKeyboardButton


class Data:
    HELP_MENU1 = [
        [
            InlineKeyboardButton(text="✯ ʙᴀɴᴀʟʟ ✯", callback_data="banall"),
            InlineKeyboardButton(text="✯ ʙɪʀᴛʜᴅᴀʏ ✯", callback_data="birthday"),
        ],
        [
            InlineKeyboardButton(text="✯ ᴘɪɴɢ ✯", callback_data="core_help1"),
            InlineKeyboardButton(text="✯ ʀᴇsᴛᴀʀᴛ ✯", callback_data="core_help2"),
        ],
        [
            InlineKeyboardButton(text="𓅓 ᴇᴠᴀʟ 𓅓", callback_data="evaluators_help1"),
        ],
        [
            InlineKeyboardButton(text="✯ ᴇxᴇᴄ ✯", callback_data="evaluators_help2"),
            InlineKeyboardButton(text="✯ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ✯", callback_data="gwish_help1"),
        ],
        [
            InlineKeyboardButton(
                text="✯ ɢᴏᴏᴅ ᴀғᴛᴇʀɴᴏᴏɴ ✯", callback_data="gwish_help2"
            ),
            InlineKeyboardButton(text="✯ ɢᴏᴏᴅ ɴɪɢʜᴛ ✯", callback_data="gwish_help3"),
        ],
        [
            InlineKeyboardButton(text="𓅓 ʀᴀɪᴅ 𓅓", callback_data="raid_help1"),
        ],
        [
            InlineKeyboardButton(text="✯ ʀᴇᴘʟʏ ʀᴀɪᴅ ✯", callback_data="raid_help2"),
            InlineKeyboardButton(text="✯ ᴅʀᴇᴘʟʏ ʀᴀɪᴅ ✯", callback_data="raid_help3"),
        ],
        [
            InlineKeyboardButton(text="✯ ʟɪsᴛ ʀᴀɪᴅ ✯", callback_data="raid_help4"),
            InlineKeyboardButton(text="✯ sʜᴀʏʀɪ ✯", callback_data="shayri_help1"),
        ],
        [
            InlineKeyboardButton(text="𓅓 sᴛᴏᴘ 𓅓", callback_data="shayri_help2"),
        ],
        [
            InlineKeyboardButton(text="✯ sᴘᴀᴍ ✯", callback_data="spam_help1"),
            InlineKeyboardButton(text="✯ ᴅᴇʟᴀʏ sᴘᴀᴍ ✯", callback_data="spam_help2"),
        ],
        [
            InlineKeyboardButton(text="✯ ᴘᴏʀɴ sᴘᴀᴍ ✯", callback_data="spam_help3"),
            InlineKeyboardButton(text="✯ ʜᴀɴɢ sᴘᴀᴍ ✯", callback_data="spam_help4"),
        ],
        [
            InlineKeyboardButton(text="𓅓 ᴜ sᴘᴀᴍ 𓅓", callback_data="unlimited_help1"),
        ],
        [
            InlineKeyboardButton(text="✯ ᴜ ʀᴀɪᴅ ✯", callback_data="unlimited_help2"),
            InlineKeyboardButton(text="✯ ᴀʙᴜsᴇ ✯", callback_data="unlimited_help3"),
        ],
        [
            InlineKeyboardButton(text="✯ sᴛᴏᴘ ✯", callback_data="unlimited_help4"),
            InlineKeyboardButton(text="✯ ᴇᴄʜᴏ ✯", callback_data="unlimited_help5"),
        ],
        [
            InlineKeyboardButton(text="𓅓 ᴏɴᴇᴡᴏʀᴅ 𓅓", callback_data="oneword_help1"),
            InlineKeyboardButton(text="✯ ᴏɴᴇsᴛᴏᴘ ✯", callback_data="oneword_help2"),
        ],
        [
            InlineKeyboardButton(text="💢 ᴄʟᴏsᴇ 💢", callback_data="close"),
        ],
    ]
    REVERT = [
        [
            InlineKeyboardButton("Reopen Help Menu", callback_data="helpmenu1"),
        ],
    ]
    HELP_MENU2 = [
        [
            InlineKeyboardButton(text="⬅️ ᴘʀᴇᴠɪᴏᴜs", callback_data="helpmenu1"),
        ],
        [
            InlineKeyboardButton(text="Close ", callback_data="close"),
        ],
        [
            InlineKeyboardButton(text="ɴᴇxᴛ ➡️", callback_data="helpmenu3"),
        ],
    ]
    HELP_MENU3 = [
        [
            InlineKeyboardButton(text="⬅️ ᴘʀᴇᴠɪᴏᴜs", callback_data="helpmenu2"),
        ],
        [
            InlineKeyboardButton(text="Close ", callback_data="close"),
        ],
        [
            InlineKeyboardButton(text="ɴᴇxᴛ ➡️", callback_data="helpmenu1"),
        ],
    ]
