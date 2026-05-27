import os

from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv(".env")

try:
    from config import *
except ImportError:
    from sample_config import *

