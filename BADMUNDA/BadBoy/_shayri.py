import asyncio
from random import choice

from pyrogram import Client, filters
from pyrogram.types import *
from SukhPB.raid import SHAYRI

from BADMUNDA.Config import *

from .. import sudos, sudo_filter, is_protected
from ..core.clients import *

Useru = False


@Client.on_message(sudo_filter & filters.command(["shayri"], prefixes=HANDLER))
async def shayri(Badmunda: Client, e: Message):
    usage = f"Command: {HANDLER}shayri -u \nCommand:{HANDLER}shayri -u (reply to anyone)\nCommand: {HANDLER}shayri (count) \nCommand: {HANDLER}shayri (count) (reply to anyone)"
    text = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
    flag = text[0]
    if not flag:
        return await e.reply_text(usage)
    if "-u" in flag:
        global Useru
        Useru = True
        if e.reply_to_message:
            lmao = e.reply_to_message
            status = is_protected(lmao.from_user)
            if status == "owner":
                return await e.reply_text("This is the owner of the bot!")
            elif status == "sudo":
                return await e.reply_text("This is a sudo user!")
            while Useru == True:
                for i in range(1, 26):
                    lol = globals()[f"Client{i}"]
                    if lol is not None:
                        try:
                            await lol.send_message(
                                e.chat.id, f"{lmao.from_user.mention}\n\n{choice(SHAYRI)}"
                            )
                        except Exception:
                            pass
                        await asyncio.sleep(0.3)
        else:
            while Useru == True:
                for i in range(1, 26):
                    lol = globals()[f"Client{i}"]
                    if lol is not None:
                        try:
                            await lol.send_message(e.chat.id, choice(SHAYRI))
                        except Exception:
                            pass
                        await asyncio.sleep(0.3)
    elif "-u" not in flag:
        try:
            counts = int(text[0])
        except ValueError:
            return await e.reply_text(usage)
        if e.reply_to_message:
            lmao = e.reply_to_message
            status = is_protected(lmao.from_user)
            if status == "owner":
                return await e.reply_text("This is the owner of the bot!")
            elif status == "sudo":
                return await e.reply_text("This is a sudo user!")
            for _ in range(counts):
                for i in range(1, 26):
                    lol = globals()[f"Client{i}"]
                    if lol is not None:
                        try:
                            await lol.send_message(
                                e.chat.id, f"{lmao.from_user.mention}\n\n{choice(SHAYRI)}"
                            )
                        except Exception:
                            pass
                        await asyncio.sleep(0.3)
        else:
            for _ in range(counts):
                for i in range(1, 26):
                    lol = globals()[f"Client{i}"]
                    if lol is not None:
                        try:
                            await lol.send_message(e.chat.id, choice(SHAYRI))
                        except Exception:
                            pass
                        await asyncio.sleep(0.3)
    else:
        await e.reply_text(usage)
    if LOG_CHANNEL:

        try:

            log_msg = f"🚨 **Shayari Spam Executed** 🚨\n━━━━━━━━━━━━━━━━━\n"

            log_msg += f"👤 **User:** {e.from_user.mention} (`{e.from_user.id}`)\n"

            log_msg += f"📍 **Chat:** `{e.chat.id}`\n"

            log_msg += f"🔢 **Counts:** `{counts}`\n"

            log_msg += "━━━━━━━━━━━━━━━━━"

            await Client1.send_message(LOG_CHANNEL, log_msg)

        except Exception as a:

            print(f"Log Error: {a}")


@Client.on_message(
    sudo_filter & filters.command(["stopshayri"], prefixes=HANDLER)
)
async def stopshayri(_, e: Message):
    global Useru
    Useru = False
    await e.reply_text("Stopped Unlimited Wish Shayri")
