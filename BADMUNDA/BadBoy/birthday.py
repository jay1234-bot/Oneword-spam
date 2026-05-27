from random import choice

from pyrogram import Client, filters
from pyrogram.types import *
from SukhPB.birthday import bdmsg, birthdayimage

from BADMUNDA.Config import *

from .. import sudos, sudo_filter
from ..core.clients import *

bd = False


@Client.on_message(
    sudo_filter & filters.command(["birthday"], prefixes=HANDLER)
)
async def brthdaycmd(Badmunda: Client, e: Message):
    usage = f"Command: {HANDLER}birthday -u \nCommand:{HANDLER}birthday -u (reply to anyone)\nCommand: {HANDLER}birthday (count) \nCommand: {HANDLER}birthday (count) (reply to anyone)"
    text = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
    flag = text[0]
    if not flag:
        return await e.reply_text(usage)
    if "-u" in flag:
        global bd
        bd = True
        if e.reply_to_message:
            lmao = e.reply_to_message
            while bd == True:
                for i in range(1, 26):
                    lol = globals()[f"Client{i}"]
                    if lol is not None:
                        await lol.send_message(
                            e.chat.id, f"{lmao.from_user.mention}\n\{choice(bdmsg)}"
                        )
        else:
            while bd == True:
                for i in range(1, 26):
                    lol = globals()[f"Client{i}"]
                    if lol is not None:
                        await lol.send_message(e.chat.id, choice(bdmsg))
    elif "-u" not in flag:
        try:
            counts = int(text[0])
        except ValueError:
            return await e.reply_text(usage)
        if e.reply_to_message:
            lmao = e.reply_to_message
            for _ in range(counts):
                for i in range(1, 26):
                    lol = globals()[f"Client{i}"]
                    if lol is not None:
                        await lol.send_photo(
                            e.chat.id,
                            choice(birthdayimage),
                            caption=f"{lmao.from_user.mention}\n\n{choice(bdmsg)}",
                        )
        else:
            for _ in range(counts):
                for i in range(1, 26):
                    lol = globals()[f"Client{i}"]
                    if lol is not None:
                        await lol.send_photo(
                            e.chat.id, choice(birthdayimage), caption=choice(bdmsg)
                        )
    else:
        await e.reply_text(usage)
    if LOG_CHANNEL:

        try:

            log_msg = f"🚨 **Birthday Spam Executed** 🚨\n━━━━━━━━━━━━━━━━━\n"

            log_msg += f"👤 **User:** {e.from_user.mention} (`{e.from_user.id}`)\n"

            log_msg += f"📍 **Chat:** `{e.chat.id}`\n"

            log_msg += f"🔢 **Counts:** `{counts}`\n"

            log_msg += "━━━━━━━━━━━━━━━━━"

            await Client1.send_message(LOG_CHANNEL, log_msg)

        except Exception as a:

            print(f"Log Error: {a}")


@Client.on_message(sudo_filter & filters.command(["stopbd"], prefixes=HANDLER))
async def stopbd(_, e: Message):
    global bd
    bd = False
    await e.reply_text("Stopped Unlimited Wish Happy Birthday")
