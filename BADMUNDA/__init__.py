import glob
import os
import time

from .Config import *
from .core import *

version = "v2"
group_username = "@CENSORED_POLITICSSS"
start_time = time.time()


# Sudo Users
from pyrogram import filters

sudos = []
if os.path.exists("sudos.txt"):
    with open("sudos.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line.isdigit():
                sudos.append(int(line))
            elif line:
                sudos.append(line)

if SUDO_USERS:
    try:
        sudouser = SUDO_USERS if isinstance(SUDO_USERS, list) else str(SUDO_USERS).split()
        for x in sudouser:
            if str(x).isdigit():
                val = int(x)
                if val not in sudos:
                    sudos.append(val)
            else:
                if x not in sudos:
                    sudos.append(x)
    except Exception as e:
        print("Sudo list error:", e)

if OWNER_ID and OWNER_ID not in sudos:
    sudos.append(OWNER_ID)

def save_sudos():
    with open("sudos.txt", "w") as f:
        for s in sudos:
            f.write(f"{s}\n")

async def is_sudo(_, __, message):
    if not message.from_user:
        return False
    return (message.from_user.id in sudos) or (message.from_user.username and message.from_user.username in sudos)

def is_protected(user):
    from .Config import OWNER_ID
    # Check owner
    if str(user.id) == str(OWNER_ID) or (user.username and str(user.username) == str(OWNER_ID)):
        return "owner"
    # Check sudo
    if user.id in sudos or (user.username and user.username in sudos):
        return "sudo"
    return None

sudo_filter = filters.create(is_sudo)
