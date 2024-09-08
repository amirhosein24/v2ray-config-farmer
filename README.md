# V2Ray Configuration Farmer

This is a Telegram bot that scrapes V2Ray proxy configurations from Telegram channels and saves them to a local repository.

## Features

- Uses Telethon to connect to Telegram and listen for messages in configured channels
- Searches messages for V2Ray proxy configurations and extracts them
- Saves configurations to local files
- Commits configurations to a Git repository hourly for distribution
- Includes a config manager component for testing configurations (not yet implemented)

## Components

- `main.py` - Starts Telethon client and handles new messages
- `posthandler.py` - Processes messages and extracts configurations
- `sublink.py` - Commits configs to Git repo hourly
- `log.py` - Stores logs of errors
- `pinger.py` - Will test proxy configurations (not implemented yet)
- `creds.py` - Imports the credentials from creds.json

## Setup

### 1. Install your own farmer

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Create `creds.json` file

3. Add Telegram API credentials to `creds.json`

4. Configure channels to listen to in `creds.json`

5. Final `creds.json` should look like this:
   ```json
   {
     "api_id": "----",
     "api_hash": "---",
     "git": {
       "name": "----",
       "email": "----@---.com",
       "token": "-----"
     }
   }
   ```

6. Start bot:
   ```
   python main.py
   ```

### 2. Use our pre-configured setup

Copy this link as a subscription link for your v2ray client:

```
https://raw.githubusercontent.com/amirhosein24/V2RAY-CONFIG-FARMER/main/zout.txt
```

## TODO

- Implement pinger for testing configurations
- Add support for more proxy protocols
- Containerize application

## Contributing

Contributions are welcome! Open an issue or PR if you would like to help add features or enhance this project.

## Warning

This app might get your Telegram account banned permanently, so use wisely.
