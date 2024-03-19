# -*- coding: utf-8 -*-

import log

from re import compile
from os import mkdir, path

from json import load, dump

home = path.dirname(path.abspath(__file__)) + "/"

try:
    mkdir(home + "/cache")
except:
    pass


def handle(text):
    try:

        pattern = compile(r'(vmess|trojan|vless|ss)://\S+')
        urls = [match.group(0) for match in pattern.finditer(text)]

        with open(home + "configs.json", encoding='utf-8') as file:
            config_list = load(file)["configs"]

        for url in urls:
            if url in config_list:
                continue
            else:
                config_list.append(url)

        with open(home + "configs.json", 'w', encoding="UTF-8") as file:
            dump({"configs" : config_list}, file, indent=4)

    except Exception as e:
        log.addlog(str(e), "posthandler")


# handle("""

# """)