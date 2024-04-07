
# -*- coding: utf-8 -*-

import log

from git import Repo
from time import sleep
from base64 import b64encode
from os import path
from json import load
from creds import git_creds

def encoder(text):
    text = text.encode('utf-8')
    encoded_data = b64encode(text).decode('utf-8')
    return encoded_data
home = path.dirname(path.abspath(__file__))

def zout():
    while True:


        with open(home + "/configs.json", encoding='utf-8') as file:
            config_list = load(file)["configs"]

        """
                todo
                pinger should be here 
                it is supposed to get a v2ray config and return the real time daley of it (ping) 
                and so the app can remove the bad configs
        """

        main = ""
        for config in config_list:
                main += config + "\n"

        with open(home+"/zout.txt", "w") as file:
            file.write(encoder(main))

        try:
            repo = Repo(home)
            repo.git.add(".")
            repo.index.commit("auto commit for v2ray sub")
            repo.git.config('user.name', git_creds[0])
            repo.git.config('user.email', f'{git_creds[0]}@gmail.com')
            remote_url = f'https://{git_creds[0]}:{git_creds[1]}@github.com/amirhosein24/v2ray-config-farmer.git'
            origin = repo.remote(name="origin")
            origin.set_url(remote_url)
            origin.push()
        except Exception as e:
            log.addlog(str(e), "sublink-gitpusher")

        sleep(3600 * 5) # sleep for n hours and then start the first upload


from threading import Thread
Thread(target=zout).start()
