from pyrogram import Client, filters
from pyrogram.types import Message
from BADMUNDA.Config import HANDLER, OWNER_ID, OWNER_IDS
from BADMUNDA import sudos, save_sudos, sudo_filter

def is_owner(user_id):
    """Check if user_id is one of the owner IDs"""
    try:
        return user_id in OWNER_IDS
    except:
        # Fallback to single owner
        return user_id == OWNER_ID

@Client.on_message(sudo_filter & filters.command(["sudo", "addsudo"], prefixes=HANDLER))
async def add_sudo_cmd(Badmunda: Client, message: Message):
    if not is_owner(message.from_user.id):
        return await message.reply_text("✦ ꜱᴏʀʀʏ, ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.")
    
    target = None
    if message.reply_to_message:
        target = message.reply_to_message.from_user.id
    elif len(message.command) > 1:
        target = message.command[1]
        if target.isdigit():
            target = int(target)
            
    if not target:
        return await message.reply_text("✦ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ ᴏʀ ɢɪᴠᴇ ᴜꜱᴇʀ ɪᴅ/ᴜꜱᴇʀɴᴀᴍᴇ.")
        
    if target in sudos:
        return await message.reply_text("✦ ᴛʜɪꜱ ᴜꜱᴇʀ ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ !!")
        
    sudos.append(target)
    save_sudos()
    await message.reply_text(f"✦ **ɴᴇᴡ ꜱᴜᴅᴏ ᴜꜱᴇʀ ᴀᴅᴅᴇᴅ** ➥ `{target}`")

@Client.on_message(sudo_filter & filters.command(["dsudo", "rmsudo", "delsudo"], prefixes=HANDLER))
async def del_sudo_cmd(Badmunda: Client, message: Message):
    if not is_owner(message.from_user.id):
        return await message.reply_text("✦ ꜱᴏʀʀʏ, ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.")
    
    target = None
    if message.reply_to_message:
        target = message.reply_to_message.from_user.id
    elif len(message.command) > 1:
        target = message.command[1]
        if target.isdigit():
            target = int(target)
            
    if not target:
        return await message.reply_text("✦ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ ᴏʀ ɢɪᴠᴇ ᴜꜱᴇʀ ɪᴅ/ᴜꜱᴇʀɴᴀᴍᴇ.")
        
    if target not in sudos:
        return await message.reply_text("✦ ᴛʜɪꜱ ᴜꜱᴇʀ ɪꜱ ɴᴏᴛ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ !!")
        
    sudos.remove(target)
    save_sudos()
    await message.reply_text(f"✦ **ꜱᴜᴅᴏ ᴜꜱᴇʀ ʀᴇᴍᴏᴠᴇᴅ** ➥ `{target}`")
