
from os import path
from telethon import TelegramClient, events

import posthandler
# importing credentials from json file
from creds import api_hash, api_id, channel_ids

import sublink  # create a loop for uploading new configs to github

# client setting
# client = TelegramClient(path.dirname(path.abspath(__file__)) + "//" + 'telethon', api_id, api_hash)
client = TelegramClient(path.dirname(path.abspath(__file__)) + "//" +
                        'telethon', api_id, api_hash, proxy=('socks5', 'localhost', 2080))

# client handler for posts


@client.on(events.NewMessage())  # events.NewMessage(chats=channel_ids)
async def handler(event):
    message_content = event.message.to_dict()
    posthandler.handle(message_content["message"])

if __name__ == "__main__":
    # with client:
    client.start()
    print("going live ... returns error if unsuccessful")
    client.run_until_disconnected()
