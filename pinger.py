# i dont know what to doooooooooooooooooooooooooooooooooooooo help ╰（‵□′）╯
#    it is supposed to get a v2ray url and check real time delay and connectivity and return true of false

import socket

def check_connection(url):
    try:
        
        if url.startswith(('vless', "trojan")):
            data = url.split("@")[1].split('?')[0]
            ip, port = data.split(':')
            
        elif url.startswith('ss'):
            data = url.split("@")[1].split('#')[0]
            ip, port = data.split(':')

        elif url.startswith('vmess'):
            return True #TODO

        sock = socket.create_connection((ip, port), timeout=5)
        sock.close()

        return True
    except:
        return False
