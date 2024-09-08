
from os import path
from telethon import TelegramClient, events

import creds
import sublink  # create a loop for uploading new configs to github
import posthandler

client = TelegramClient(path.dirname(path.abspath(__file__)) + "//" + 'telethon', creds.api_id, creds.api_hash)

# # incase of proxy need use this one
#client = TelegramClient(path.dirname(path.abspath(__file__)) + "//" 'telethon', api_id, api_hash, proxy=('socks5', 'localhost', 2080))


@client.on(events.NewMessage())
async def handler(event):
    message_content = event.message.to_dict()
    posthandler.handle(message_content["message"])

if __name__ == "__main__":
    client.start()
    print("going live ... returns error if unsuccessful")
    client.run_until_disconnected()
