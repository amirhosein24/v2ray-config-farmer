# -*- coding: utf-8 -*-

import log

from re import compile
from uuid import uuid1
from os import mkdir, path

home = path.dirname(path.abspath(__file__))
print(home)
try:
    mkdir(home + "/cache")
except:
    pass

def handle(text):

    try:
        text = text["message"]
        proxy_url_pattern = r'(vmess|trojan|vless|ss)://[^\s]+'
        print(proxy_url_pattern)
        pattern = compile(proxy_url_pattern)
        full_urls = [match.group(0) for match in pattern.finditer(text)]
        
        for i in full_urls:
            with open(home + f"cache/{uuid1()}.txt", "w", encoding="utf8") as file:
                file.write(i)

    except Exception as e:
        log.addlog(str(e), "posthandler")