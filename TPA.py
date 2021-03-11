from telethon import TelegramClient
from datetime import datetime, timedelta
import os

# To connect Telegram, remember to use your own values from my.telegram.org
api_id = <your_api_id>    # Ex. 1234567
api_hash = <your_api_hash>    # Ex. '0a1b2c3d4e5f60a1b2c3d4e5f60a1b2c'

# These are the options you can specify according to your needs
home_dir = "/path/to/dir/"    # Home directory to download pictures  
# List of chats with pictures
chat_list = ["https://t.me/someone", "https://t.me/channel_1"]
# On the first run, all pictures posted after this date will be downloaded
start_from = "2020-08-28"

# Connect to Telegram
client = TelegramClient('anon', api_id, api_hash)

def detect_date(chat_name):
    """This function ensures that only the pictures after the required date 
    will be downloaded """
    
    # Check folders named with previous dates already exist or not
    directory_list = [f.name for f in os.scandir(home_dir+chat_name) \ 
        if f.is_dir()]
        
    if directory_list:
        # Only an incremental download required
        return datetime.strptime(directory_list[len(directory_list)-1], \ 
            '%Y-%m-%d').date() - timedelta(days=1)
    else:
        # Full download since "start_from" required
        return datetime.fromisoformat(start_from)


async def main():
    message_list = []
    for full_chat_name in chat_list:
        # Loop over each chat on chat_list
        # 
        # Assign last part of full_chat_name to chat_name  
        chat_name = os.path.basename(os.path.normpath(full_chat_name))
        if not os.path.isdir(home_dir + chat_name):
            # If a directory named as chat_name does not exist, create it
            os.mkdir(home_dir + chat_name)

        # Process only the messages after the required date 
        messages_from_this_date = detect_date(chat_name)

        async for message in client.iter_messages(full_chat_name):
            # Loop over each message in this chat
            
            # Update the timestamp of the message with UTC+2
            message.date = message.date + timedelta(hours=2)    
            
            if message.date.replace(tzinfo=None) > datetime.fromisoformat( \ 
                str(messages_from_this_date)):
                # Proceed with only the messages from the relevant date


async with client:
    await main()