from sys import platform
import time
# from sys import platform
#!/usr/bin/python

# -*- coding: utf8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pygologin.gologin import GoLogin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import json

from underthesea import ner
from bs4 import BeautifulSoup
import requests


from datetime import datetime
from datetime import timedelta


TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MzZiNjdiNTVhMTI5NzNmY2FiMzdlMTAiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MzZiNjgwNDczY2QwZDFiNjNmYmM5YTIifQ.VfF22lLEMP3JSklvuWTgOfkxEKKHCcsSYQotg6zMcac"
gl = GoLogin({
    "token": TOKEN,
    'profile_id': "636b67b55a12973346b37e12",
})


proxy_list=[]
for line in open("proxylist.txt","r"):
    line=line[:-1]
    proxy_list.append(line.split(":"))
proxy_check=[]


chrome_driver_path = "/Users/nguyenductai/Downloads/chromedriver"
debugger_address = gl.start()
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", debugger_address)
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
driver.close()

def creat_new_profile_id(gl, i):
    host=proxy_list[i][0]
    port=proxy_list[i][1]
    profile_id = gl.create({
        "name": 'profile_'+str(i),
        "os": 'mac',
        "proxyEnabled": True,
        "navigator": {
            "language": 'en-US,en;q=0.9,he;q=0.8',
            "userAgent": 'MyUserAgent',
            "resolution": '1024x768',
            "platform": 'darwin',
        },
        "proxy":{
            'mode': 'socks5',
            'host': host,
            'port': port,
            'username': "prateep6793",
            'password': "Zing1234",
        }
    });
    return profile_id

def clear_proxy_list(gl,driver):
    for i in range(len(proxy_list)-1):
        print(i)
        try:
            profile_id=creat_new_profile_id(gl,i)
            gl = GoLogin({
                "token": TOKEN,
                'profile_id': profile_id,
            })
            chrome_driver_path = "/Users/nguyenductai/Downloads/chromedriver"
            debugger_address = gl.start()
            chrome_options = Options()
            chrome_options.add_experimental_option("debuggerAddress", debugger_address)
            driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
            proxy_check.append(True)
            driver.get("https://www.google.com/")
            print("Okay")
        except:
            print("Error Proxy!")
            proxy_check.append(False)
        time.sleep(2)
        driver.refresh()
        driver.close()
        gl.delete(profile_id)


clear_proxy_list(gl,driver)
print(proxy_list)

