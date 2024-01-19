import requests

def get_links_from_github(username, repository, filename):
    url = f'https://raw.githubusercontent.com/{username}/{repository}/main/{filename}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.splitlines()
    else:
        raise Exception(f"Failed to retrieve links from GitHub. Status code: {response.status_code}")
    

print(get_links_from_github("amirhosein24", "X_poster", "main.py"))