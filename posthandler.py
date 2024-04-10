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
                if len(config_list) >= 500:
                    config_list.pop(0)
                config_list.append(url)

        with open(home + "configs.json", 'w', encoding="UTF-8") as file:
            dump({"configs" : config_list}, file, indent=4)

    except Exception as e:
        log.addlog(str(e), "posthandler")


# handle("""
# vmess://eyJhZGQiOiIxMDQuMjEuMTUuMzYiLCJhaWQiOiIwIiwiYWxwbiI6IiIsImZwIjoiIiwiaG9zdCI6ImxpbmRlMDYuaW5kaWF2aWRlby5zYnMiLCJpZCI6ImVkYmIxMDU5LTE2MzMtNDI3MS1iNjZlLWVkNGZiYTQ3YTFiZiIsIm5ldCI6IndzIiwicGF0aCI6Ii9saW5rd3MiLCJwb3J0IjoiNDQzIiwicHMiOiLwn5SrVGVsZWdyYW06QE1BUkFNQkFTSEkgVGVsZWdyYW06QE1BUkFNQkFTSEkgVGVsZWdyYW06QE1BUkFNQkFTSEkiLCJzY3kiOiJhdXRvIiwic25pIjoibGluZGUwNi5pbmRpYXZpZGVvLnNicyIsInRscyI6InRscyIsInR5cGUiOiIiLCJ2IjoiMiJ9
# vless://8721355e-96d5-4bb9-a99b-b6119d6b1cd4@Www.ZULA.iR:8443?path=%2F&security=tls&encryption=none&alpn=h2,http/1.1&host=uD2kp0fx53e15EHUFNo2LJ7mHRsDgTYET8xzmA7tXh40tR606ogTx280VN.PaGEs.dEv&fp=chrome&type=ws&sni=uD2kp0fx53e15EHUFNo2LJ7mHRsDgTYET8xzmA7tXh40tR606ogTx280VN.PaGEs.dEv#%F0%9F%94%ABTelegram%3A%40@MARAMBASHI+Telegram%3A%40@MARAMBASHI+Telegram%3A%40@MARAMBASHI
# vless://51905fd3-29de-4b4e-b351-83542f1d5390@172.67.24.121:443?path=%2F%3Fed%3D2048&security=tls&encryption=none&alpn=h2,http/1.1&host=biA.ALlhub.LTD&fp=random&type=ws&sni=Bia.alLhub.Ltd#%F0%9F%94%ABTelegram%3A%40@MARAMBASHI+Telegram%3A%40@MARAMBASHI+Telegram%3A%40@MARAMBASHI
# vless://d672ec4f-afba-4f61-af09-eec872f97e99@188.114.98.220:443?path=%2Ffreecodes&security=tls&encryption=none&host=test57.pages.dev&fp=chrome&type=ws&sni=test57.pages.dev#%F0%9F%92%9CTelegram%3A%40@MARAMBASHI+Telegram%3A%40@MARAMBASHI+Telegram%3A%40@MARAMBASHI
# """)
