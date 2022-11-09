import time
import re
# from sys import platform
#!/usr/bin/python

# -*- coding: utf8 -*-

from bs4 import BeautifulSoup
from bs4 import element

import bs4
import requests

start=time.time()



news={}
#news[0]={'title':'','link':'','content':''}


def scraping_soup(link, category, page):
    url = requests.get(link)
    if (page=="vnexpress"):
        soup = BeautifulSoup(url.content, 'lxml')
    else:
        soup = BeautifulSoup(url.content, 'html.parser')
    items = soup.findAll('item')
    i=0
    for item in items:

        title = item.title.text
        link = item.guid.text
        description = item.description.text
        print(title)
        #--------


        news[len(news)] = {'title': title, 'link': link, 'content': title + ' ' + description, 'category': category, 'page':page}
        i+=1
        if i==30: break


#def Suggest_news_thethao():
    #scraping_soup('https://vnexpress.net/rss/the-thao.rss','thethao', 'vnexpress')


def Suggest_news_thoisu_chinhtri():
    scraping_soup('https://vnexpress.net/rss/thoi-su.rss', 'thoisu', 'vnexpress')
    #scraping_soup('https://vtv.vn/trong-nuoc/chinh-tri.rss', 'thoisu')
    scraping_soup('https://toquoc.vn/rss/thoi-su-1.rss', 'thoisu','toquoc')
    #scraping_soup('https://baotintuc.vn/thoi-su.rss', 'thoisu', 'baotintuc')
    #scraping_soup('https://vietnamnet.vn/rss/thoi-su.rss', 'thoisu', 'vietnamnet')
   # scraping_soup('https://laodong.vn/rss/thoi-su.rss', 'thoisu', 'laodong')


#def Suggest_news_vanhoa():
    #scraping_soup('https://toquoc.vn/rss/van-hoa-10.rss', 'vanhoa', 'toquoc')
    #scraping_soup('https://baotintuc.vn/van-hoa.rss', 'vanhoa', 'baotintuc')
    #scraping_soup('https://laodong.vn/rss/van-hoa-giai-tri.rss', 'vanhoa', 'laodong')



#Suggest_news_thethao()
Suggest_news_thoisu_chinhtri()
#Suggest_news_vanhoa()

print(news)










