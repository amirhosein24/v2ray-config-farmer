# -*- coding: utf-8 -*-

from os import mkdir, path
from re import compile
from uuid import uuid1
from datetime import datetime

try:
    mkdir(path.dirname(path.abspath(__file__)) + "/cache")
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
            with open(f"cache//{uuid1()}.txt", "w", encoding="utf8") as file:
                file.write(i)
    except Exception as e:
        with open(path.dirname(path.abspath(__file__))+"/error_log.txt", "a") as file:
            file.write(str(e))
            file.write(f"\n-----------------error in posthandler on {datetime.now()}\n\n\n")