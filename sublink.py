
# -*- coding: utf-8 -*-

from git import Repo

import log
import pinger
from creds import git_creds

from os import path
from json import load
from time import sleep
from base64 import b64encode
from threading import Thread

home = path.dirname(path.abspath(__file__))


def encoder(text):
    text = text.encode('utf-8')
    encoded_data = b64encode(text).decode('utf-8')
    return encoded_data


def zout():
    while True:
        sleep(3600 * 1)  # sleep for n hours and then push the new configs to github

        try:

            with open(home + "/configs.json", encoding='utf-8') as file:
                config_list = load(file)["configs"][::-1]

            main = ""
            for config in config_list:
                # checks the connection of the config
                if pinger.check_connection(config):
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


Thread(target=zout).start()
