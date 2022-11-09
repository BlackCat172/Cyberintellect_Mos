import requests
import random
from bs4 import BeautifulSoup as bs
import traceback
import time

def get_free_proxies():
    url = "https://free-proxy-list.net/"
    # request and grab content
    soup = bs(requests.get(url).content, 'html.parser')
    # to store proxies
    proxies = []
    for row in soup.find("table", attrs={"class": "table-striped"}).find_all("tr")[1:]:
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            proxies.append(str(ip) + ":" + str(port))
        except IndexError:
            continue
    return proxies

url = "http://ipinfo.io/json"
proxies = get_free_proxies()
print(proxies)

def first_proxy(proxies):
    while True:
        proxy = proxies[random.randint(0,len(proxies)-1)]
        try:
            response = requests.get(url, proxies = {"http":"http://"+str(proxy), "https":"https://"+str(proxy)}, timeout=1)
            print(response.json()['country'])
            print(response.json()['region'])
            print(response.text)
            break
        except:
            pass
            # if the proxy Ip is preoccupied
            # print("Not Available")
    return proxy

print(first_proxy(proxies))