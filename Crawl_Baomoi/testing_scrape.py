from bs4 import BeautifulSoup
import requests

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

from googlesearch import *

from datetime import datetime
from datetime import timedelta
"""
TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MzNkZDJlOWYwMzIwMjBkYWQwNDU2ZTciLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MzNkZDM0YWM5OWFmMmMzMzdkMjNmNGQifQ.7UmxqoGmN25EwG1DmN-2aJZqbBUY3R4hgKJciKgUwRg"

link="https://ipinfo.io/"

gl = GoLogin({
	"token": TOKEN,
    'tmpdir':"/tmp/",
    "local":True,
    "credentials_enable_service": False,
})

profile_id = gl.create({
    "name": 'profile_1',
    "os": 'mac',
    "proxyEnabled": True,
    "navigator": {
        "language": 'en-US,en;q=0.9,he;q=0.8',
        "userAgent": 'MyUserAgent',
        "resolution": '1024x768',
        "platform": 'darwin',
    },
    "proxy":{
        'mode': 'http',
        'host': "139.99.237.62",
        'port': "80",
        'username': "",
        'password': "",
    }
});
'host': "139.99.237.62",
        'port': ,
        'username': "",
        'password': "",



gl = GoLogin({
	"token": TOKEN,
    'profile_id':profile_id,
})

chrome_driver_path = "/Users/nguyenductai/Downloads/chromedriver"
debugger_address = gl.start()
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", debugger_address)
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

driver.get(link)
gl.delete(profile_id)
driver.close()
print("end session!")
# ----------------------------



"""
link="https://toquoc.vn/van-hoa-khong-co-su-cao-thap-nho-hay-lon-ma-chi-co-su-da-dang-net-dac-sac-tieu-bieu-can-duoc-ton-trong-ton-vinh-phat-huy-giu-gin-20221006225030042.htm"
news = {}
t_title = ""
t_description = ""
t_contents = ''
url = requests.get(link)
t_soup = BeautifulSoup(url.text, 'lxml')


for title in t_soup.findAll('h1', {'class': 'entry-title'}):
    t_title = title.text
for description in t_soup.findAll('h2', {'class': 'sapo'}):
    t_description = description.text
for contents in t_soup.findAll('div', {'data-role': 'content'}):
    for content in contents.findAll('p'):
        t_contents += content.text + ". "



news = {'title': t_title, 'description': t_description, 'content': t_contents, 'category': "",'date':""}
print(news)