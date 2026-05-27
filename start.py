import os
from threading import Thread
from http.server import BaseHTTPRequestHandler, HTTPServer

from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# =========================
# KEEP ALIVE SERVER
# =========================

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running successfully!")

def run_web():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(("0.0.0.0", port), Handler)
    print(f"Keep Alive Server Running On Port {port}")
    server.serve_forever()

Thread(target=run_web, daemon=True).start()

# =========================
# CHECK REQUIRED VARIABLES
# =========================

required_vars = [
    "APP_ID",
    "API_HASH",
    "BOT_TOKEN",
    "SUDO_USERS"
]

missing = []

for var in required_vars:
    if not os.getenv(var):
        missing.append(var)

if missing:
    print("\n❌ Missing Required Variables:\n")
    
    for var in missing:
        print(f"• {var}")
    
    print("\nAdd them in Railway Variables or .env file.\n")
    exit()

# =========================
# START BOT
# =========================

print("🚀 Starting Bot...")

os.system("python3 -m BADMUNDA")
