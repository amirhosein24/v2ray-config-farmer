
import posthandler
from os import path
from creds import api_hash, api_id, channel_ids # importing credentials from json file
from telethon import TelegramClient, events


import sublink # starts a loop for config manager on a new thread

# client setting
client = TelegramClient(path.dirname(path.abspath(__file__)) + "//" +'telethon', api_id, api_hash, proxy=('socks5', 'localhost', 2080))

# client handler for posts
@client.on(events.NewMessage(chats=channel_ids))
async def handler(event):
    message_content = event.message.to_dict()
    posthandler.handle(message_content)






if __name__ == "__main__":
    with client:
        print("going live ..., if unsuccessful returns error ")
        client.run_until_disconnected()