import sys
import time
# from sys import platform
#!/usr/bin/python

# -*- coding: utf8 -*-

from bs4 import BeautifulSoup
import requests
import time
import json

start=time.time()

fi=open("links2.txt","r")
fo=open("","a")

news={}
#news[len(news)] = {'title': title, 'link': link, 'content': title + ' ' + description, 'category': category, 'page':page}

i=0

start=time.time()

for line in fi.readlines():
    i+=1
    if (i<69878): continue
    link=line.strip()
    try:
        url=requests.get(link)
        if url.history: continue
        t_soup = BeautifulSoup(url.text, 'lxml')
        t_content=""
        for title in t_soup.findAll('h1', {'class': 'bm_J'}):
            t_title=title.text
        for description in t_soup.findAll('h3', {'class': 'bm_Ak bm_J'}):
            t_description = description.text
        for date in t_soup.findAll('time'):
            if date.has_attr('datetime'):
                t_date=date['datetime']
        for category in t_soup.findAll('a', {'class': 'bm_y'}):
            t_category=category.text
        for content in t_soup.findAll('p', {'class': 'bm_Y'}):
            t_content+=content.text+" "
        for content in t_soup.findAll('p', {'class': 'bm_Y bm_FP'}):
            t_content+=content.text+" "
        news = {'title': t_title, 'description': t_description, 'content': t_content, 'category': t_category, 'date': t_date}
        fo.write(json.dumps(news, ensure_ascii=False))
        fo.write('\n')
        print(i)
    except:
        print("Error!")

fi.close()
fo.close()

print("--- %s seconds ---" % (time.time() - start))








