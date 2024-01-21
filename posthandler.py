# -*- coding: utf-8 -*-

from os import mkdir, path
from re import compile
from uuid import uuid1


try:
    mkdir(path.dirname(path.abspath(__file__)) + "//cache")
except:
    pass

def handle(text):
    text = text["message"]

    proxy_url_pattern = r'(vmess|trojan|vless|ss)://[^\s]+'
    pattern = compile(proxy_url_pattern)
    full_urls = [match.group(0) for match in pattern.finditer(text)]

    for i in full_urls:
        with open(f"cache//{uuid1()}.txt", "w", encoding="utf8") as file:
            file.write(i)