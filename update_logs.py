import os
import re
import glob

# Files to process
files = glob.glob('BADMUNDA/BadBoy/*.py')

def replace_log_block(match):
    indent = match.group(1)
    full_block = match.group(0)
    
    # Extract components from the original f-string
    f_string = match.group(2)
    
    # Try to determine spam type
    spam_type = "Spam"
    if "Delay Spam" in f_string: spam_type = "Delay Spam"
    elif "Porn Spam" in f_string: spam_type = "Porn Spam"
    elif "Hang Spam" in f_string: spam_type = "Hang Spam"
    elif "Reply Raid" in f_string: spam_type = "Reply Raid"
    elif "Delay Raid" in f_string: spam_type = "Delay Raid"
    elif "Raid" in f_string: spam_type = "Raid"
    elif "Gwish" in f_string: spam_type = "Global Wish"
    elif "Shayri" in f_string: spam_type = "Shayari Spam"
    elif "Unlimited Delay" in f_string: spam_type = "Unlimited Delay Spam"
    elif "Unlimited" in f_string: spam_type = "Unlimited Spam"
    elif "Birthday" in f_string: spam_type = "Birthday Spam"
    
    # Extract variables
    counts_match = re.search(r'Counts:\s*\{([^}]+)\}', f_string)
    message_match = re.search(r'(?:Spam Message|Gwish Message):\s*\{([^}]+)\}', f_string)
    sleep_match = re.search(r'Sleep Time:\s*\{([^}]+)\}', f_string)
    
    counts_var = counts_match.group(1) if counts_match else None
    msg_var = message_match.group(1) if message_match else None
    sleep_var = sleep_match.group(1) if sleep_match else None
    
    # Construct new formatted message
    new_code = f"{indent}if LOG_CHANNEL:\n"
    new_code += f"{indent}    try:\n"
    new_code += f"{indent}        log_msg = f\"🚨 **{spam_type} Executed** 🚨\\n━━━━━━━━━━━━━━━━━\\n\"\n"
    new_code += f"{indent}        log_msg += f\"👤 **User:** {{e.from_user.mention}} (`{{e.from_user.id}}`)\\n\"\n"
    new_code += f"{indent}        log_msg += f\"📍 **Chat:** `{{e.chat.id}}`\\n\"\n"
    
    if counts_var:
        new_code += f"{indent}        log_msg += f\"🔢 **Counts:** `{{{counts_var}}}`\\n\"\n"
    if sleep_var:
        new_code += f"{indent}        log_msg += f\"⏱ **Delay:** `{{{sleep_var}}}s`\\n\"\n"
    if msg_var:
        new_code += f"{indent}        log_msg += f\"💬 **Message:** {{{msg_var}}}\\n\"\n"
        
    new_code += f"{indent}        log_msg += \"━━━━━━━━━━━━━━━━━\"\n"
    new_code += f"{indent}        await Client1.send_message(LOG_CHANNEL, log_msg)\n"
    new_code += f"{indent}    except Exception as a:\n"
    new_code += f"{indent}        print(f\"Log Error: {{a}}\")"
    
    return new_code


pattern = re.compile(r'(\s+)if LOG_CHANNEL:\s+try:\s+await [A-Za-z0-9_]+\.send_message\(\s*LOG_CHANNEL,\s*f"([^"]+)",?\s*\)\s+except Exception as [a-zA-Z0-9_]+:\s+print\([a-zA-Z0-9_]+\)')

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    new_content, count = pattern.subn(replace_log_block, content)
    
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {count} log blocks in {filepath}")
