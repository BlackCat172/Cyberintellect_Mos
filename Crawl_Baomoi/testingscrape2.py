import requests
import random

import requests
from requests.auth import HTTPProxyAuth
from bs4 import BeautifulSoup as bs
import traceback
#from proxybroker import checker

url = "http://ipinfo.io/json"
proxy_list=[]
for line in open("proxylist.txt","r"):
    line=line[:-1]
    proxy_list.append(line)

print(proxy_list)
#checker.ProxyChecker()

auth=HTTPProxyAuth("prateep6793","Zing1234")

for i in range(len(proxy_list)):

    #printing req number
    print("Request Number : " + str(i+1))
    proxy = proxy_list[i]
    #print(proxy)
    try:
        response = requests.get(url, proxies = {"http":"socks5://"+proxy, "https":"socks5://"+proxy},auth=auth, timeout=10)
        print("ok!")
    except:
        # if the proxy Ip is pre occupied
        print("Not Available")

