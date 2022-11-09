import sys
import time
# from sys import platform
#!/usr/bin/python

# -*- coding: utf8 -*-

from bs4 import BeautifulSoup
import requests
import time

start=time.time()

fi=open("linksthethao.txt","r")
fo=open("baothethao2.txt","w")

i=0

for line in fi.readlines():
    link=line.strip()
    url=requests.get(link)

    t_soup = BeautifulSoup(url.text, 'lxml')

    for headline in t_soup.findAll('h1', {'class': 'details__headline cms-title'}):
        fo.write(headline.text)
        fo.write('\n')
    for description in t_soup.findAll('div', {'class': 'sapo cms-desc'}):
        fo.write(description.text)
        fo.write('\n')
    str = ''
    for contents in t_soup.findAll('div', {'class': 'cms-body detail'}):
        for content in contents.findAll('p'):
            fo.write(content.text)
            fo.write('\n')

    i+=1
    print(i)
    if (i==50): break


fi.close()
fo.close()
print("--- %s seconds ---" % (time.time() - start))











