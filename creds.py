from json import load

def load_json():
   with open(__file__[:-8] + "creds.json", encoding='utf-8') as file:
      config = load(file)

   api_id = config["api_id"]
   api_hash = config["api_hash"]
   channel_ids = config["channel_ids"]
   git = config["git"]

   return api_id, api_hash, channel_ids, git

api_id, api_hash, channel_ids, git = load_json()