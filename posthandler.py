# -*- coding: utf-8 -*-

import log

import json
import base64
from re import compile
from os import path

home = path.dirname(path.abspath(__file__)) + "/"


def handle(text):
    try:

        pattern = compile(r'(vmess|trojan|vless|ss)://\S+')
        urls = [match.group(0) for match in pattern.finditer(text)]

        with open(home + "configs.json", encoding='utf-8') as file:
            config_list = json.load(file)["configs"]

        for url in urls:

            if not url.startswith("vmess"):
                url = url.split("#")[0] + "#@garshaspX کانال تلگرام گرشاسپـــ"
            else:
                vmess_conf = json.loads(
                    base64.b64decode(url[8:]).decode('utf-8'))
                vmess_conf["ps"] = "@garshaspX کانال تلگرام گرشاسپـــ"
                vmess_conf = json.dumps(
                    vmess_conf, ensure_ascii=False).encode('utf-8')
                url = "vmess://" + base64.b64encode(vmess_conf).decode('utf-8')

            if url in config_list:
                continue
            else:
                if len(config_list) >= 500:
                    config_list.pop(0)
                config_list.append(url)

        with open(home + "configs.json", 'w', encoding="UTF-8") as file:
            json.dump({"configs": config_list}, file, indent=4)

    except Exception as e:
        log.addlog(str(e), "posthandler")
