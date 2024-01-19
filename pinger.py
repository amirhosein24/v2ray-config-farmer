import subprocess

def check_v2ray_ping(v2ray_link):
    command = f'litetest.exe {v2ray_link}'
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        print(output)
        output = output.decode('utf-8')
        ping = output.split('Ping: ')[1].split(' ms')[0]
        return float(ping)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.output.decode('utf-8')}")
        return None

# Example usage
v2ray_link = "vmess://eyJhZGQiOiAiMTA0LjI2LjE1Ljg1IiwgImFpZCI6ICIwIiwgImFscG4iOiAiaDIsaHR0cC8xLjEiLCAiZnAiOiAiYW5kcm9pZCIsICJob3N0IjogImNkbi5wb2tlcmFkLmZ1biIsICJpZCI6ICI1NjJhZTQxMi1kN2I1LTRmMWUtZGQwZC04MmUwNzMxOTNiMjEiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL2ZhIiwgInBvcnQiOiAiNDQzIiwgInBzIjogIkBIb3BlX05ldC1qb2luLXVzLW9uLVRlbGVncmFtIiwgInNjeSI6ICJhZXMtMTI4LWdjbSIsICJzbmkiOiAicG9rZXJhZC5mdW4iLCAidGxzIjogInRscyIsICJ0eXBlIjogIiIsICJ2IjogIjIifQ=="
ping = check_v2ray_ping(v2ray_link)
if ping is not None:
    print(f"Ping: {ping} ms")