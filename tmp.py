import sys
import time
# from sys import platform
#!/usr/bin/python

# -*- coding: utf8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pygologin.gologin import GoLogin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import json

from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests

'''gl = GoLogin({
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MmY3Yjk3NGQxZGNkYmJjYzA5ODUyODciLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MmY3Y2E2OTgwZGRjMDU1YjliZTVlMjMifQ.__GwUyY80hIVJ8o2Ak0wntHYizNwWrm42h-k7q0xxJE",
    "profile_id": "62f7b974d1dcdb43cb985289",
    # "port": random_port
}'''
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"

chrome_driver_path = "/Users/nguyenductai/Downloads/chromedriver2"
#debugger_address = gl.start()
chrome_options = Options()
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
#chrome_options.add_experimental_option("debuggerAddress", debugger_address)
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options, desired_capabilities=capa)
#driver=webdriver.Chrome("/Users/nguyenductai/Downloads/chromedriver2")'''
# ----------------------------

f=open("linksthethao.txt", "w")

for i in range(2,3):
    url='https://thanhnien.vn/thoi-su/chinh-tri/?trang='+str(i)
    url1 = requests.get(url)
    soup = BeautifulSoup(url1.content, 'lxml')
    #items = soup.findAll('item')

    for links in soup.findAll('article', {'class': "story"}):
        for a in links.findAll('a', {'class': "story__title cms-link"} ,href=True):
            f.write(a['href'])
            f.write('\n')

    print(i,'\n')


"""    
url1=requests.get('https://vnexpress.net/rss/the-thao.rss')
soup=BeautifulSoup(url1.content, 'xml')
items=soup.find_all('item')
wait=WebDriverWait(driver,200)

'''driver.get("https://vnexpress.net/neymar-mbappe-va-vu-penaltygate-2-0-4501139.html")
wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/section[4]/div/div[2]/h1')))
str = driver.find_element(By.XPATH, '/html/body/section[4]/div/div[2]/article').text
str=str[:str.rfind('\n')]
str=str[:str.rfind('\n')]
str=str[:str.rfind('\n')]
print(str)'''

i=0
for item in items:
    i+=1
    title=item.title.text
    link=item.link.text
    #print("Link: ", link, '\n\n')
    url2=requests.get(link)
    #---------
    t_soup=BeautifulSoup(url2.content,'lxml')
    for headline in t_soup.findAll('h1',{'class':'title-detail'}):
        f.write(headline.text)
        f.write('\n')
    for description in t_soup.findAll('p',{'class':'description'}):
        f.write(description.text)
        f.write('\n')
    str=''
    for normal in t_soup.findAll('p', {'class': 'Normal'}):
        str+=normal.text+'\n'

    str = str[:str.rfind('\n')]
    str = str[:str.rfind('\n')]
    str+='\n'
    f.write(str)
        #print('\n')
    print(i,'\n')


    #print(t_soup)
    #-----------
    '''driver.get(link)
    time.sleep(1)
    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/section[4]/div/div[2]/article')))
    str = driver.find_element(By.XPATH, '/html/body/section[4]/div/div[2]/article').text
    str = str[:str.rfind('\n')]
    str = str[:str.rfind('\n')]
    str = str[:str.rfind('\n')]
    str+='\n'
    f.write(str)
    print(i)
    #driver.execute_script("window.stop();")
    driver.refresh()'''
    #-------------

"""
f.close()









