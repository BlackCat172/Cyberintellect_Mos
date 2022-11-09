from underthesea import ner
from underthesea import pos_tag
from underthesea import word_tokenize
import json
from bs4 import BeautifulSoup
import requests


fi=open("baomoi_testing_crawling.txt","r")

i=0

for line in fi.readlines():
    a=json.loads(line)
    t_str=ner(a["title"])
    #---
    t_date=a["date"]
    year=t_date[0:4]
    month=t_date[5:7]
    day=t_date[8:10]
    #---
    print(t_str)
    searching_key= ''
    for words in t_str:
        if (words[1]=="N") or (words[1]=="Np"):
            searching_key+= '"' + words[0] + '"' + "%2B"
    searching_key=searching_key.replace(" ", "+")
    searching_key= searching_key[0:len(searching_key) - 3]
    '''
    print(searching_key)
    print(year,' ',month,' ',day)
    print(i)
    '''
    i+=1
    if (i==2): break
