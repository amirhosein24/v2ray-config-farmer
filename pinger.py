# i dont know what to doooooooooooooooooooooooooooooooooooooo ╰（‵□′）╯
# it is supposed to get a v2ray url and check real time delay and connectivity and return true of false

import socket
import time
import requests
from requests.exceptions import RequestException
from contextlib import closing

def url_test(url, timeout=1000):
    times = 3 if "true" not in url else 1
    rtt_times = 2 if "true" in url else 1
    start = time.time()
    for i in range(times):
        try:
            requests.get(url, timeout=timeout/1000) 
        except RequestException as e:
            return 0, e
    duration = (time.time() - start) * 1000
    return round(duration / rtt_times), None

def tcp_ping(host, port, timeout=1000):
    start = time.time()
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        sock.settimeout(timeout / 1000) 
        try:
            sock.connect((host, port))
        except socket.error as err:
            return 0, err
        duration = (time.time() - start) * 1000    
    return round(duration), None



# link = "vless://1175cb41-5e0d-4953-9e0d-6248b9554788@85.85.85.85:443?security=reality&pbk=Cul4tQATj5jk_yImxwIQ_3vNyywaRZMEeJaVwPS8oF8&sid=ef170a21&type=http&path=/HGUggFFRYHFrEDVhyyDBTYrEEU#@Hope_Net-join-us-on-Telegram"
# print(url_test(link))


# import socket
# import json

# config = """vless://-----Digiv2ray------@all.digiv2ray.shop:2053?security=tls&sni=Digi-V2rayng-ConneCtion.Digiv2ray.shop&type=ws&path=/&host=Digi-V2rayng-ConneCtion.Digiv2ray.shop#@Hope_Net-join-us-on-Telegram
# {"dns":{"fallbackStrategy":"disabled_if_any_match","servers":[{"address":"https://8.8.8.8/dns-query","domains":[],"queryStrategy":""},{"address":"localhost","domains":["full:all.digiv2ray.shop"],"fallbackStrategy":"disabled","queryStrategy":""}],"tag":"dns"},"inbounds":[{"listen":"127.0.0.1","port":2080,"protocol":"socks","settings":{"udp":true},"sniffing":{"destOverride":["http","tls","quic"],"enabled":true,"metadataOnly":false,"routeOnly":true},"tag":"socks-in"}],"log":{"loglevel":"warning"},"outbounds":[{"domainStrategy":"AsIs","protocol":"vless","settings":{"vnext":[{"address":"all.digiv2ray.shop","port":2053,"users":[{"encryption":"none","id":"-----Digiv2ray------"}]}]},"streamSettings":{"network":"ws","security":"tls","tlsSettings":{"serverName":"Digi-V2rayng-ConneCtion.Digiv2ray.shop"},"wsSettings":{"headers":{"Host":"Digi-V2rayng-ConneCtion.Digiv2ray.shop"},"path":"/"}},"tag":"proxy"},{"protocol":"freedom","tag":"direct"},{"protocol":"freedom","tag":"bypass"},{"protocol":"blackhole","tag":"block"},{"protocol":"dns","proxySettings":{"tag":"proxy","transportLayer":true},"settings":{"address":"8.8.8.8","network":"tcp","port":53,"userLevel":1},"tag":"dns-out"}],"policy":{"levels":{"1":{"connIdle":30}},"system":{"statsOutboundDownlink":true,"statsOutboundUplink":true}},"routing":{"domainMatcher":"mph","domainStrategy":"AsIs","rules":[{"inboundTag":["socks-in","http-in"],"outboundTag":"dns-out","port":"53","type":"field"},{"outboundTag":"proxy","port":"0-65535","type":"field"}]},"stats":{}}
# """
# config = json.loads(config)

# outbounds = config["outbounds"]
# for outbound in outbounds:
#     if outbound["tag"] == "proxy":
#         vnext = outbound["settings"]["vnext"][0]
        
#         address = vnext["address"]
#         port = vnext["port"]
        
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         result = sock.connect_ex((address, port))
#         if result == 0:
#             print(f"Connection succeeded to {address}:{port}")
#         else:
#             print(f"Connection failed to {address}:{port}")



# import json
# import socket
# import shadowsocks

# config = """{"dns":{"fallbackStrategy":"disabled_if_any_match","servers":[{"address":"https://8.8.8.8/dns-query","domains":[],"queryStrategy":""},{"address":"localhost","domains":["full:masting.xyz"],"fallbackStrategy":"disabled","queryStrategy":""}],"tag":"dns"},"inbounds":[{"listen":"127.0.0.1","port":2080,"protocol":"socks","settings":{"udp":true},"sniffing":{"destOverride":["http","tls","quic"],"enabled":true,"metadataOnly":false,"routeOnly":true},"tag":"socks-in"}],"log":{"loglevel":"warning"},"outbounds":[{"domainStrategy":"AsIs","protocol":"shadowsocks","settings":{"servers":[{"address":"masting.xyz","method":"chacha20-ietf-poly1305","password":"XvK0ltH67Xhv9ht9RhYsFy","port":8080}]},"streamSettings":{"network":"tcp"},"tag":"proxy"},{"protocol":"freedom","tag":"direct"},{"protocol":"freedom","tag":"bypass"},{"protocol":"blackhole","tag":"block"},{"protocol":"dns","proxySettings":{"tag":"proxy","transportLayer":true},"settings":{"address":"8.8.8.8","network":"tcp","port":53,"userLevel":1},"tag":"dns-out"}],"policy":{"levels":{"1":{"connIdle":30}},"system":{"statsOutboundDownlink":true,"statsOutboundUplink":true}},"routing":{"domainMatcher":"mph","domainStrategy":"AsIs","rules":[{"inboundTag":["socks-in","http-in"],"outboundTag":"dns-out","port":"53","type":"field"},{"outboundTag":"proxy","port":"0-65535","type":"field"}]},"stats":{}}
# """

# #ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpYdkswbHRINjdYaHY5aHQ5UmhZc0Z5@masting.xyz:8080#@Hope_Net
# config = json.loads(config)



# server = config["outbounds"][0]["settings"]["servers"][0]

# address = server["address"]
# port = server["port"]
# method = server["method"] 
# password = server["password"]
# print(password, "===========================")
# ss_client = shadowsocks.Shadowsocks()
# ss_client.set_config(password, method, address, port)

from pythonping import ping

def measure_delay(url):
    ping_result = ping(target=url, count=10, timeout=2)

    return {
        'url': url,
        'avg_latency': ping_result.rtt_avg_ms,
        'min_latency': ping_result.rtt_min_ms,
        'max_latency': ping_result.rtt_max_ms,
        'packet_loss': ping_result.packet_loss
    }

v2ray_url = 'ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpYdkswbHRINjdYaHY5aHQ5UmhZc0Z5@masting.xyz:8080#@Hope_Net'

result = measure_delay(v2ray_url)
print(result)