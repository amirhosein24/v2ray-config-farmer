from git import Repo
from os import path, listdir, getcwd
from base64 import b64encode
from time import sleep
from creds import github_password, github_username, repo_name
from datetime import datetime
def encoder(text):
    text = text.encode('utf-8')
    encoded_data = b64encode(text).decode('utf-8')
    return encoded_data
home = path.dirname(path.abspath(__file__))

def zout():
    while True:
        files = listdir(home+"/cache/")

        """
                todo
                pinger should be here and update the files list with good configs and remove the trash ones

        """

        main = ""
        for i in files:
            with open(home+"/cache/"+i, "r") as file:
                link = file.read()
                main += link + "\n"
        with open(home+"/zout.txt", "w") as file:
            file.write(encoder(main))


        repo = Repo(getcwd())
        repo.git.add(all=True)
        commit_message = "config update on zout commit"
        repo.index.commit(commit_message)
        origin = repo.remote(name="origin")
        origin.push()
        try:
            origin_url = f"https://github.com/{github_username}/{repo_name}.git"
            origin = repo.create_remote('origin', origin_url)
            origin.fetch()
            origin.push(refspec=repo.head.ref)
            origin = repo.create_remote('origin', origin_url.replace("https://", f"https://{github_username}:{github_password}@"))
            origin.fetch()
            origin.push(refspec=repo.head.ref)
        except Exception as e:
            with open(home+"/error_log.txt", "a") as file:
                file.write(str(e))
                file.write(f"\n-----------------error in git push on {datetime.now()}\n\n\n")

        sleep(3600) # sleep for an hour

from threading import Thread
Thread(target=zout).start()


# import requests
# import base64
# def get_links_from_github():
#     url = f'https://raw.githubusercontent.com/amirhosein24/V2RAY-CONFIG-FARMER/main/zout.txt'   # sub link
#     response = requests.get(url)
#     if response.status_code == 200:
#         return base64.b64decode(response.text).decode('utf-8')
#     else:
#         return f"Failed to retrieve links from GitHub. Status code: {response.status_code}"
# print(get_links_from_github())