from pyrogram import Client, filters
from pyrogram.types import Message
from BADMUNDA.Config import LOG_CHANNEL
from ..core.clients import Client1

@Client.on_message(filters.new_chat_members)
async def new_chat_member_logger(client: Client, message: Message):
    me = await client.get_me()
    for member in message.new_chat_members:
        if member.id == me.id:
            if LOG_CHANNEL:
                try:
                    log_msg = f"🚨 **Bot Added to New Group!** 🚨\n━━━━━━━━━━━━━━━━━\n"
                    log_msg += f"📌 **Group Name:** {message.chat.title}\n"
                    log_msg += f"📍 **Group ID:** `{message.chat.id}`\n"
                    if message.chat.username:
                        log_msg += f"🔗 **Username:** @{message.chat.username}\n"
                    if message.from_user:
                        log_msg += f"👤 **Added By:** {message.from_user.mention} (`{message.from_user.id}`)\n"
                    log_msg += "━━━━━━━━━━━━━━━━━"
                    await client.send_message(LOG_CHANNEL, log_msg)
                except Exception as e:
                    print(f"Group Log Error: {e}")
            break
