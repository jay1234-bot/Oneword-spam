import platform

from pyrogram import Client
from pyrogram import __version__ as py_version
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, Message
from SukhPB.start import start_cmd

from BADMUNDA.Config import *

from ..core.clients import *

# Default START_PIC if not set
if not START_PIC:
    START_PIC = "https://envs.sh/fS5.jpg"


@Client.on_message(filters.command(["start"], prefixes=HANDLER))
async def _start(Badmunda: Client, message: Message):
    my_detail = await Badmunda.get_me()
    my_mention = my_detail.mention

    # Determine start message for this user
    if START_MESSAGE:
        start_msg = START_MESSAGE.replace("{mention}", message.from_user.mention).replace("{first_name}", message.from_user.first_name)
    else:
        start_msg = (
            f"ʜᴇʏ💫 {message.from_user.mention}🌸\n"
            f"✥ ɪ ᴀᴍ {my_mention}\n\n"
            "❖━━━━•❅•°•❈•°•❅•━━━━❖\n\n"
            f"✥ **__ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ__** = {py_version}\n"
            f"✥ **__ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ__** = {platform.python_version()}\n"
            f"✥ **__ʙᴏᴛsᴘᴀᴍ ᴠᴇʀsɪᴏɴ__** = {version}\n"
            "❖━━━━•❅•°•❈•°•❅•━━━━❖"
        )

    from pyrogram.types import InlineKeyboardButton
    # Getting start buttons
    start_buttons = [
        [InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/censored_politics")],
        [InlineKeyboardButton("sᴜᴅᴏ", url="https://t.me/+TbsWobFwMPY1YjNl")]
    ]

    if START_PIC.lower().endswith((".jpg", ".png")):
        await Badmunda.send_photo(
            message.chat.id,
            START_PIC,
            caption=start_msg,
            reply_markup=InlineKeyboardMarkup(start_buttons),
        )
    elif START_PIC.lower().endswith(".mp4"):
        await Badmunda.send_video(
            message.chat.id,
            START_PIC,
            caption=start_msg,
            reply_markup=InlineKeyboardMarkup(start_buttons),
        )
    else:
        await Badmunda.send_message(
            message.chat.id,
            start_msg,
            reply_markup=InlineKeyboardMarkup(start_buttons),
        )

    if LOG_CHANNEL:
        try:
            log_msg = f"🚨 **New User Started Bot** 🚨\n━━━━━━━━━━━━━━━━━\n"
            log_msg += f"👤 **User:** {message.from_user.mention} (`{message.from_user.id}`)\n"
            if message.from_user.username:
                log_msg += f"🔗 **Username:** @{message.from_user.username}\n"
            log_msg += f"📍 **Chat:** `{message.chat.id}`\n"
            log_msg += "━━━━━━━━━━━━━━━━━"
            await Badmunda.send_message(LOG_CHANNEL, log_msg)
        except Exception as e:
            print(f"Start Log Error: {e}")
