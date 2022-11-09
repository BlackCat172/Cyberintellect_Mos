import sys
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

gl = GoLogin({
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MzJjMjliMjJlMjIxZjVlMjc5Yzc4ZTQiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MzJjMmI3OTlmYjIxNDI0YTFmNTQzZTUifQ.GR4iJFqUVRuI3XO_Ns3cfiII2m8CactTGU9jhNaSf-k",
    "profile_id": "632c5184cef566f424ef2e3c",
    # "port": random_port
})
chrome_driver_path = "/Users/nguyenductai/Downloads/chromedriver"
debugger_address = gl.start()
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", debugger_address)
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
# ----------------------------


'''
chrome_driver_path = "/Users/nguyenductai/Downloads/chromedriver2"
chrome_options = Options()
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
'''

start=time.time()

# ----------some def------------------
def find_first_link():
    for tmp in driver.find_elements(By.TAG_NAME,'a'):
        extracted_link=tmp.get_attribute("href")
        if (extracted_link!=None):
            if (extracted_link.find("https://"+site+"/")==0):
                print(extracted_link)

def create_link(site):
    link = 'https://www.google.com/search?q=' + searching_key + '+site%3A' + site + '&sxsrf=ALiCzsbBtWjs-pcdgMW06QAzFmDQAIJemg%3A1663745112460&source=lnt&tbs=cdr%3A1%2Ccd_'
    date_from=date-timedelta(days=1)
    date_to=date+timedelta(days=1)
    year_from=date_from.strftime("%Y")
    year_to=date_to.strftime("%Y")
    month_from=date_from.strftime("%m")
    month_to=date_to.strftime("%m")
    day_from=date_from.strftime("%d")
    day_to=date_to.strftime("%d")
    tmp = 'min%3A'+month_from+'%2F'+day_from+'%2F'+year_from+'%2Ccd_max%3A'+month_to+ '%2F'+ day_to+  '%2F'+ year_to+  '&tbm='
    return link+tmp

def crawl(link,site):

    news = {}
    t_title = ""
    t_description = ""
    t_contents = ''
    url = requests.get(link)
    t_soup = BeautifulSoup(url.text, 'lxml')

    if (site=="thanhnien.vn"):
        for title in t_soup.findAll('h1', {'class': 'details__headline cms-title'}):
            t_title=title.text
        for description in t_soup.findAll('div', {'class': 'sapo cms-desc'}):
            t_description=description.text
        for contents in t_soup.findAll('div', {'class': 'cms-body detail'}):
            for content in contents.findAll('p'):
                t_contents+=content.text+". "
        for contents in t_soup.findAll('div', {'class': 'cms-body'}):
            for content in contents.findAll('p'):
                t_contents+=content.text+". "
    
    if (site=="vnexpress.net"):
        for title in t_soup.findAll('h1', {'class': 'title-detail'}):
            t_title=title.text
        for description in t_soup.findAll('p', {'class': 'description'}):
            t_description=description.text
        for contents in t_soup.findAll('p', {'class': 'Normal'}):
            t_contents+=contents.text+". "

    if (site=="tienphong.vn"):
        for title in t_soup.findAll('h1', {'class': 'article__title cms-title'}):
            t_title=title.text
        for description in t_soup.findAll('div', {'class': 'article__sapo cms-desc'}):
            t_description=description.text
        for contents in t_soup.findAll('div', {'class': 'article__body cms-body'}):
            for content in contents.findAll('p'):
                t_contents+=content.text+". "
        for contents in t_soup.findAll('td', {'class': 'caption'}):
            for content in contents.findAll('p'):
                t_contents+=content.text+". "

    if (site=="vov.vn"):
        for title in t_soup.findAll('div', {'class': 'row article-title'}):
            t_title=title.text
        for description in t_soup.findAll('div', {'class': 'row article-summary'}):
            t_description=description.text
        for contents in t_soup.findAll('div', {'class': 'row article-content'}):
            for content in contents.findAll('p'):
                t_contents+=content.text+". "
        for contents in t_soup.findAll('td'):
            for content in contents.findAll('p'):
                t_contents+=content.text+". "

    if (site=="nhandan.vn"):
        for title in t_soup.findAll('h1', {'class': 'article__title cms-title'}):
            t_title = title.text
        for description in t_soup.findAll('div', {'class': 'article__sapo cms-desc'}):
            t_description = description.text
        for contents in t_soup.findAll('div', {'class': 'article__body cms-body'}):
            for content in contents.findAll('p'):
                t_contents += content.text + ". "
        for contents in t_soup.findAll('td', {'class': 'caption'}):
            for content in contents.findAll('p'):
                t_contents += content.text + ". "

    if (site=="zingnews.vn"):
        for title in t_soup.findAll('h1', {'class': 'the-article-title'}):
            t_title = title.text
        for description in t_soup.findAll('p', {'class': 'the-article-summary'}):
            t_description = description.text
        for contents in t_soup.findAll('div', {'class': 'the-article-body'}):
            for content in contents.findAll('p'):
                t_contents += content.text + ". "

    if (site=="tuoitre.vn"):

        for title in t_soup.findAll('h1', {'class': 'article-title'}):
            t_title = title.text
        for description in t_soup.findAll('h2', {'class': 'sapo'}):
            t_description = description.text
        for contents in t_soup.findAll('div', {'class': 'content fck'}):
            for content in contents.findAll('p'):
                t_contents += content.text + ". "


    news = {'title': t_title, 'description': t_description, 'content': t_contents, 'category': "",'date':""}
    if t_title=="": return {}
    return news

#-----------------------
sites={'vnexpress.net','thanhnien.vn','tienphong.vn','vov.vn','nhandan.vn','zingnews.vn','tuoitre.vn'}

fi=open("baomoi_testing_crawling.txt","r")
fo=open("testing.txt",'w')
i=0
#--------------------------
for line in fi.readlines():
    a=json.loads(line)
    t_str=ner(a["title"])
    #---
    t_date=a["date"]
    year=int(t_date[0:4])
    month=int(t_date[5:7])
    day=int(t_date[8:10])
    date=datetime(year,month,day)
    #---
    searching_key= ''
    for words in t_str:
        if (words[1]=="N") or (words[1]=="Np"):
            searching_key+= '"' + words[0] + '"' + "%2B"
    searching_key=searching_key.replace(" ", "+")
    searching_key= searching_key[0:len(searching_key) - 3]
    source = [line]
    for site in sites:
        #print(create_link(site))
        check_link=create_link(site)
        driver.get(check_link)
        time.sleep(0.5)
        #print(check_link)
        #print(driver.current_url)
        while (driver.current_url.find("https://www.google.com/search")==-1):
            driver.delete_all_cookies()
            driver.refresh()
            driver.get(check_link)
            time.sleep(0.5)
        #print("#---------------------"+"\n")
        '''
        while (driver.current_url!=check_link):
            driver.delete_all_cookies()
            driver.refresh()
            driver.get(check_link)
        '''
        #driver.execute_script("window.open("+"'"+create_link(site)+"'"+");")
        for tmp in driver.find_elements(By.TAG_NAME, 'a'):
            extracted_link = tmp.get_attribute("href")
            if (extracted_link != None):
                if (extracted_link.find("https://" + site + "/") == 0):
                    #print(extracted_link)
                    print(extracted_link)
                    news = crawl(extracted_link,site)
                    if news!={}:
                        source.append(news)
                    break
        #time.sleep(2)
        #crawling(create_link(site))
        # print(source)

    fo.write(json.dumps(source, ensure_ascii=False))
    fo.write('\n')


print("--- %s seconds ---" % (time.time() - start))








