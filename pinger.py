
import socket
import base64
import json

def check_connection(url):
    try:

        ip, port = False, False

        if url.startswith(('vless', "trojan")):
            config = url.split("@")[1].split('?')[0]
            ip, port = config.split(':')

        elif url.startswith('ss'):
            config = url.split("@")[1].split('#')[0]
            ip, port = config.split(':')

        elif url.startswith('vmess'):
            config = json.loads(base64.b64decode(url[8:]).decode('utf-8'))
            ip, port = config["add"], config["port"]


        if ip and port:
            sock = socket.create_connection((ip, port), timeout=5)
            sock.close()
            return True
        else:
            return False

    except:
        return False
