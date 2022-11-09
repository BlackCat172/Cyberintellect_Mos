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

proxy_list=[]
for line in open("proxylist.txt","r"):
    proxy_list.append(line.split(":"))
proxy_check=[]

TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MzU4ZGExYTMyMzA4NDUzNDYwYjMwOTQiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MzU4ZGEzNDM5OGJmNTFkM2IyMjc5OTQifQ.8LBET_Bp0BK7W7nCafDQD1BV3nKkmKIXA7iltU0z0VA"

gl = GoLogin({
	"token": TOKEN,
    'tmpdir':"/tmp/",
    "local":True,
    "credentials_enable_service": False,
})

chrome_driver_path = "/Users/nguyenductai/Downloads/chromedriver"
debugger_address = gl.start()
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", debugger_address)
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)


"""
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
        'host': host,
        'port': port,
        'username': "prateep6793",
        'password': "Zing1234",
    }
});

"""

def creat_new_profile_id(gl, i):
    host=proxy_list[i][0]
    port=proxy_list[i][1]
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
            'host': host,
            'port': port,
            'username': "prateep6793",
            'password': "Zing1234",
        }
    });
    return profile_id

def clear_proxy_list(gl,driver):
    i=0
    while (i<len(proxy_list)):
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
            proxy_check[i]=True
        except:
            print("Error Proxy!")
            proxy_check[i]=False
        i+=1



# ----------------------------


'''
chrome_driver_path = "/Users/nguyenductai/Downloads/chromedriver2"
chrome_options = Options()
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
'''

start=time.time()
print("ok")
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
    tmp = "&tbs=cdr:1,cd_min:"+month_to+"/"+day_to+"/"+year_to+",cd_max:"+month_from+"/"+day_from+"/"+year_from
    #print(link+tmp)
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

    if (site=="cand.com.vn"):
        for title in t_soup.findAll('h1', {'class': 'box-title-detail entry-title'}):
            t_title = title.text
        for description in t_soup.findAll('div', {'class': 'box-des-detail this-one'}):
            t_description = description.text
        for contents in t_soup.findAll('div', {'class': 'detail-content-body'}):
            for content in contents.findAll('p'):
                t_contents += content.text + ". "

    if (site == "vtv.vn"):
        for title in t_soup.findAll('h1', {'class': 'title_detail'}):
            t_title = title.text
        for description in t_soup.findAll('h2', {'class': 'sapo'}):
            t_description = description.text
        for contents in t_soup.findAll('div', {'class': 'ta-justify'}):
            for content in contents.findAll('p'):
                t_contents += content.text + ". "
                tmp = len(content.text + ". ")

    if (site == "24h.com.vn"):
        for title in t_soup.findAll('h1', {'class': 'clrTit bld tuht_show'}):
            t_title = title.text
        for description in t_soup.findAll('h2', {'class': 'ctTp tuht_show'}):
            t_description = description.text
        for contents in t_soup.findAll('article', {'class': 'nwsHt nwsUpgrade'}):
            for content in contents.findAll('p'):
                t_contents += content.text + ". "

    if (site == "dantri.com.vn"):
        for title in t_soup.findAll('h1', {'class': 'title-page detail'}):
            t_title = title.text
        for description in t_soup.findAll('h2', {'class': 'singular-sapo'}):
            t_description = description.text
        for contents in t_soup.findAll('div', {'class': 'singular-content'}):
            for content in contents.findAll('p'):
                t_contents += content.text + ". "

    if (site == "baophapluat.vn"):
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

    if (site == "kenh14.vn"):
        for title in t_soup.findAll('h1', {'class': 'kbwc-title'}):
            t_title = title.text
        for description in t_soup.findAll('h2', {'class': 'knc-sapo'}):
            t_description = description.text
        for contents in t_soup.findAll('div', {'class': 'knc-content'}):
            for content in contents.findAll('p'):
                t_contents += content.text + ". "

    if (site == "laodong.vn"):
        for title in t_soup.findAll('h1', {'class': 'title'}):
            t_title = title.text
        for description in t_soup.findAll('div', {'class': 'chappeau'}):
            t_description = description.text
        for contents in t_soup.findAll('div', {'class': 'art-body'}):
            for content in contents.findAll('p'):
                t_contents += content.text + ". "

    if (site == "qdnd.vn"):
        for title in t_soup.findAll('h1', {'class': 'post-title'}):
            t_title = title.text
        for description in t_soup.findAll('div', {'class': 'post-summary'}):
            t_description = description.text
        for contents in t_soup.findAll('div', {'class': 'post-content'}):
            for content in contents.findAll('p'):
                t_contents += content.text + ". "

    if (site == "vtc.vn"):
        for title in t_soup.findAll('h1', {'class': 'font28 bold lh-1-3'}):
            t_title = title.text
        for description in t_soup.findAll('h2', {'class': 'font18 bold inline-nb'}):
            t_description = description.text
        for contents in t_soup.findAll('div', {'class': 'edittor-content box-cont mt15 clearfix '}):
            for content in contents.findAll('p'):
                t_contents += content.text + ". "

    if (site == "toquoc.vn"):
        for title in t_soup.findAll('h1', {'class': 'entry-title'}):
            t_title = title.text
        for description in t_soup.findAll('h2', {'class': 'sapo'}):
            t_description = description.text
        for contents in t_soup.findAll('div', {'data-role': 'content'}):
            for content in contents.findAll('p'):
                t_contents += content.text + ". "




    news = {'title': t_title, 'description': t_description, 'content': t_contents, 'category': "",'date':""}
    if t_title=="": return {}
    return news

#-----------------------
sites={'vnexpress.net','thanhnien.vn','tienphong.vn',
       'vov.vn','nhandan.vn','zingnews.vn',
       'tuoitre.vn','cand.com.vn','vtv.vn',
       '24h.com.vn','dantri.com.vn','baophapluat.vn',
       'kenh14.vn','laodong.vn','qdnd.vn','vtc.vn',
       'toquoc.vn'}

fi=open("baomoi_testing_crawling.txt","r")
fo=open("testing.txt",'w')
#--------------------------

clear_proxy_list()

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
        time.sleep(1)
        #print(check_link)
        if (driver.current_url.find("sorry")!=-1):
            print("Error!")
        else:
            print(driver.current_url)
        """
            try:
                i+=1
                driver.close()
                gl = GoLogin({
                    "token": TOKEN,
                    'profile_id': creat_new_profile_id(gl,i),
                })
                debugger_address = gl.start()
                chrome_options = Options()
                chrome_options.add_experimental_option("debuggerAddress", debugger_address)
                driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

                driver.get(check_link)
            except:
                pass

        #print("#---------------------"+"\n")
        '''
        while (driver.current_url!=check_link):
            driver.delete_all_cookies()
            driver.refresh()
            driver.get(check_link)
        '''
        """
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








