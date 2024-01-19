import requests

def get_links_from_github(username, repository, filename):
    url = f'https://raw.githubusercontent.com/{username}/{repository}/main/{filename}'


    url = "https://javad-ghazvin.sbs/?token=a330da232ff4124a39c63faf2c7b5a97"
    
    response = requests.get(url)
    # print(response.json())

    # print(response.text)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to retrieve links from GitHub. Status code: {response.status_code}")
    

print(get_links_from_github("amirhosein24", "X_poster", "main.py"))


import requests
import base64


def get_v2ray_links(subscription_link):
    try:
        response = requests.get(subscription_link)

        subscription_data = response.text.strip()

        decoded_data = base64.b64decode(subscription_data).decode('utf-8')


        # lissss = decoded_data.split("\n")
        # print(lissss)

    except Exception as e:
        print(f"Error fetching subscription link: {e}")

