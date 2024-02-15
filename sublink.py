# -*- coding: utf-8 -*-

import log

from git import Repo
from time import sleep
from base64 import b64encode
from os import path, listdir, remove


def encoder(text):
    text = text.encode('utf-8')
    encoded_data = b64encode(text).decode('utf-8')
    return encoded_data
home = path.dirname(path.abspath(__file__))

def zout():
    while True:

        sleep(3600 * 3) # sleep for n hours and then start the first upload

        files = listdir(home+"/cache/")

        """
                todo
                pinger should be here 
                it is supposed to get a v2ray config and return the real time daley of it (ping) 
                and so the app can remove the bad configs

        """

        main = ""
        for config in files:
            with open(home+"/cache/"+config, "r") as file:
                link = file.read()
                main += link + "\n"
            #remove(home+"/cache/"+config)
        with open(home+"/zout.txt", "w") as file:
            file.write(encoder(main))

        try:
            repo = Repo(home)
            repo.git.add(".")
            repo.index.commit("auto commit for v2ray sub")
            repo.remote().push()
        except Exception as e:
            log.addlog(str(e), "sublink-gitpusher")


from threading import Thread
Thread(target=zout).start()
