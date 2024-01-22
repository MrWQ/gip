import requests
url = "https://mrwq.github.io/"
h = {"user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12A365 MicroMessenger/5.4.1 NetType/WIFI"}
resp = requests.get(url,headers=h)
print(resp.text)
