import asyncio
import os
from pyrogram import Client, filters
from pyrogram.types import Message

from BADMUNDA.Config import *
from .. import sudos, sudo_filter, is_protected
from ..core.clients import *

oneword_active = False

@Client.on_message(sudo_filter & filters.command(["oneword"], prefixes=HANDLER))
async def oneword_cmd(Badmunda: Client, e: Message):
    global oneword_active
    usage = f"Command: {HANDLER}oneword (reply to a message)"
    
    if not e.reply_to_message:
        return await e.reply_text(usage)
        
    target_msg = e.reply_to_message
    status = is_protected(target_msg.from_user)
    if status == "owner":
        return await e.reply_text("This is the owner of the bot!")
    elif status == "sudo":
        return await e.reply_text("This is a sudo user!")
        
    if not os.path.exists("oneword.txt"):
        return await e.reply_text("Error: oneword.txt file not found!")
        
    with open("oneword.txt", "r", encoding="utf-8") as f:
        words = [line.strip() for line in f.read().split(",") if line.strip()]
        
    if not words:
        return await e.reply_text("Error: oneword.txt is empty or invalid format!")

    import random
    
    active_clients = []
    for i in range(1, 26):
        client = globals().get(f"Client{i}")
        if client is not None:
            active_clients.append(client)
            
    if not active_clients:
        return await e.reply_text("Error: No active clients found!")
        
    random.shuffle(active_clients)
    
    oneword_active = True
    word_index = 0
    total_words = len(words)
    
    worker_client = None
    
    # Test clients by sending the first word
    first_word = words[word_index]
    for client in active_clients:
        try:
            await client.send_message(
                chat_id=e.chat.id,
                text=first_word,
                reply_to_message_id=target_msg.id
            )
            worker_client = client
            break
        except Exception:
            continue
            
    if not worker_client:
        oneword_active = False
        return await e.reply_text("Error: None of the clients could send a message here!")
        
    await e.reply_text("Started OneWord spam using a random active client...")
    word_index = (word_index + 1) % total_words
    await asyncio.sleep(5)
    
    while oneword_active:
        for _ in range(5):
            if not oneword_active:
                break
            word = words[word_index]
            try:
                await worker_client.send_message(
                    chat_id=e.chat.id,
                    text=word,
                    reply_to_message_id=target_msg.id
                )
            except Exception:
                pass
                
            word_index = (word_index + 1) % total_words
            await asyncio.sleep(0.3)
            
        if oneword_active:
            await asyncio.sleep(5)
        
    if LOG_CHANNEL:
        try:
            log_msg = f"🚨 **OneWord Spam Executed** 🚨\n━━━━━━━━━━━━━━━━━\n"
            log_msg += f"👤 **User:** {e.from_user.mention} (`{e.from_user.id}`)\n"
            log_msg += f"📍 **Chat:** `{e.chat.id}`\n"
            log_msg += "━━━━━━━━━━━━━━━━━"
            await Badmunda.send_message(LOG_CHANNEL, log_msg)
        except Exception as a:
            print(f"Log Error: {a}")

@Client.on_message(sudo_filter & filters.command(["onestop"], prefixes=HANDLER))
async def onestop_cmd(_, e: Message):
    global oneword_active
    oneword_active = False
    await e.reply_text("Stopped OneWord spam.")
