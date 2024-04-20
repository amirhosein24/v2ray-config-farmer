
# -*- coding: utf-8 -*-

import log
import pinger
from creds import git_creds

from git import Repo
from time import sleep
from base64 import b64encode
from os import path
from json import load

home = path.dirname(path.abspath(__file__))


def encoder(text):
    text = text.encode('utf-8')
    encoded_data = b64encode(text).decode('utf-8')
    return encoded_data


def zout():
    while True:
        try:

            with open(home + "/configs.json", encoding='utf-8') as file:
                config_list = load(file)["configs"][::-1]

            main = ""
            for config in config_list:
                if pinger.check_connection(config): # checks the connection of the config
                    main += config + "\n"

            with open(home+"/zout.txt", "w") as file:
                file.write(encoder(main))

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

        sleep(3600 * 1) # sleep for n hours and then push the new configs to github


from threading import Thread
Thread(target=zout).start()
