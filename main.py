from os import path
from creds import api_hash, api_id, channel_ids
from telethon import TelegramClient, events
import posthandler



client = TelegramClient(path.dirname(path.abspath(__file__)) + "//" +'telethon', api_id, api_hash)


@client.on(events.NewMessage(chats=channel_ids))
async def handler(event):

    message_content = event.message.to_dict()
    posthandler.handle(message_content)


if __name__ == "__main__":
    with client:
        print("going live ...")
        client.run_until_disconnected()