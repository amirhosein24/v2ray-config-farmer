# -*- coding: utf-8 -*-

import log

from git import Repo
from time import sleep
from base64 import b64encode
from os import path, listdir


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

        try:
            repo = Repo(home)
            repo.git.add(".")
            repo.index.commit("auto commit for v2ray sub")
            repo.remote().push()
            
        except Exception as e:
            log.addlog(str(e), "sublink-gitpusher")

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