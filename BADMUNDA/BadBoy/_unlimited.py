from random import choice

from SukhPB.raid import RAID as galia
from pyrogram import Client, filters
from pyrogram.types import Message
from SukhPB.get_user import user_only
from SukhPB.raid import RAID

from BADMUNDA.Config import *

from .. import sudos, sudo_filter, is_protected
from ..core.clients import *

unlimited = False


@Client.on_message(sudo_filter & filters.command(["uspam"], prefixes=HANDLER))
async def uspam(Badmunda: Client, e: Message):
    global unlimited
    unlimited = True
    msg = str(e.text[6:])
    if not msg:
        await e.reply("Gime Spam message bruh!")
        return
    if e.reply_to_message:
        lmao = e.reply_to_message
        status = is_protected(lmao.from_user)
        if status == "owner":
            return await e.reply_text("This is the owner of the bot!")
        elif status == "sudo":
            return await e.reply_text("This is a sudo user!")
        while unlimited == True:
            for i in range(1, 26):
                lol = globals()[f"Client{i}"]
                if lol is not None:
                    await lol.send_message(e.chat.id, f"{lmao.from_user.mention} {msg}")
    else:
        while unlimited == True:
            for i in range(1, 26):
                lol = globals()[f"Client{i}"]
                if lol is not None:
                    await lol.send_message(e.chat.id, msg)
    if LOG_CHANNEL:

        try:

            log_msg = f"🚨 **Unlimited Spam Executed** 🚨\n━━━━━━━━━━━━━━━━━\n"

            log_msg += f"👤 **User:** {e.from_user.mention} (`{e.from_user.id}`)\n"

            log_msg += f"📍 **Chat:** `{e.chat.id}`\n"

            log_msg += f"💬 **Message:** {msg}\n"

            log_msg += "━━━━━━━━━━━━━━━━━"

            await Client1.send_message(LOG_CHANNEL, log_msg)

        except Exception as a:

            print(f"Log Error: {a}")


@Client.on_message(sudo_filter & filters.command(["uraid"], prefixes=HANDLER))
async def uraid(Badmunda: Client, e: Message):
    global unlimited
    unlimited = True
    user = await user_only(Badmunda, e)
    status = is_protected(user)
    if status == "owner":
        return await e.reply_text("This is the owner of the bot!")
    elif status == "sudo":
        return await e.reply_text("This is a sudo user!")
    mention = user.mention
    if e.reply_to_message:
        lmao = e.reply_to_message
        while unlimited == True:
            reply = choice(RAID)
            raid_msg = f"{lmao.from_user.mention} {reply}"
            for i in range(1, 26):
                lol = globals()[f"Client{i}"]
                if lol is not None:
                    await lol.send_message(e.chat.id, raid_msg)
    else:
        while unlimited == True:
            reply = choice(RAID)
            raid_msg = f"{mention} {reply}"
            for i in range(1, 26):
                lol = globals()[f"Client{i}"]
                if lol is not None:
                    await lol.send_message(e.chat.id, raid_msg)
    if LOG_CHANNEL:

        try:

            log_msg = f"🚨 **Raid Executed** 🚨\n━━━━━━━━━━━━━━━━━\n"

            log_msg += f"👤 **User:** {e.from_user.mention} (`{e.from_user.id}`)\n"

            log_msg += f"📍 **Chat:** `{e.chat.id}`\n"

            log_msg += "━━━━━━━━━━━━━━━━━"

            await Client1.send_message(LOG_CHANNEL, log_msg)

        except Exception as a:

            print(f"Log Error: {a}")


@Client.on_message(
    sudo_filter & filters.command(["abuse", "gali"], prefixes=HANDLER)
)
async def abuse(Badmunda: Client, e: Message):
    global unlimited
    unlimited = True
    if e.reply_to_message:
        lmao = e.reply_to_message
        status = is_protected(lmao.from_user)
        if status == "owner":
            return await e.reply_text("This is the owner of the bot!")
        elif status == "sudo":
            return await e.reply_text("This is a sudo user!")
        while unlimited == True:
            msg = choice(galia)
            for i in range(1, 26):
                lol = globals()[f"Client{i}"]
                if lol is not None:
                    await lol.send_message(e.chat.id, f"{lmao.from_user.mention} {msg}")
    else:
        while unlimited == True:
            msg = choice(galia)
            for i in range(1, 26):
                lol = globals()[f"Client{i}"]
                if lol is not None:
                    await lol.send_message(e.chat.id, f"{msg}")
    if LOG_CHANNEL:

        try:

            log_msg = f"🚨 **Raid Executed** 🚨\n━━━━━━━━━━━━━━━━━\n"

            log_msg += f"👤 **User:** {e.from_user.mention} (`{e.from_user.id}`)\n"

            log_msg += f"📍 **Chat:** `{e.chat.id}`\n"

            log_msg += "━━━━━━━━━━━━━━━━━"

            await Client1.send_message(LOG_CHANNEL, log_msg)

        except Exception as a:

            print(f"Log Error: {a}")


@Client.on_message(sudo_filter & filters.command(["stop"], prefixes=HANDLER))
async def stop(_, e: Message):
    global unlimited
    unlimited = False
    await e.reply_text("Stopped Unlimited Spam/Raid/abuse -;")


@Client.on_message(
    sudo_filter & filters.command(["echo", "repeat"], prefixes=HANDLER)
)
async def echo_(Badmunda: Client, message: Message):
    txt = " ".join(message.command[1:])
    if message.reply_to_message:
        msg = message.reply_to_message.text.markdown
    elif txt:
        msg = str(txt)
    else:
        await message.reply_text(
            f"**Wrong Usage!** \n\n Syntax: {HANDLER}echo (message or reply to message)"
        )
        return

    try:
        await message.delete()
        await Badmunda.send_message(message.chat.id, msg)
    except Exception as a:
        await Badmunda.send_message(message.chat.id, msg)
        print(str(a))
