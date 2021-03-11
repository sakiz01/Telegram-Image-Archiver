from telethon import TelegramClient
from datetime import datetime, timedelta
import os

# To connect Telegram, remember to use your own values from my.telegram.org
api_id = <your_api_id>    # Ex. 1234567
api_hash = <your_api_hash>    # Ex. '0a1b2c3d4e5f60a1b2c3d4e5f60a1b2c'

# These are the options you can specify according to your needs
home_dir = "/path/to/dir/"    # Home directory to download pictures  
chat_list = ["https://t.me/someone", "https://t.me/channel_1", "https://t.me/channel_2"]    # List of chats with pictures
start_from = "2020-08-28"    # On the first run, all pictures posted after this date will be downloaded

