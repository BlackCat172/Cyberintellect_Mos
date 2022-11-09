import time
# from sys import platform
#!/usr/bin/python

# -*- coding: utf8 -*-

from bs4 import BeautifulSoup
import bs4
import requests
from urllib.parse import urljoin
import time

base = 'https://baomoi.com/'

#start=time.time()

f=open("links2.txt","w")



def scraping_link(link):
    url = requests.get(link)
    soup = BeautifulSoup(url.content, 'lxml')
    for links in soup.findAll('div',{'class':'bm_O'}):
        for a in links.findAll('a', href=True):
            f.write(urljoin(base,a['href']))
            f.write('\n')



for i in range(1,168):
    start = time.time()
    print(i)
    #scraping_link("https://baomoi.com/tin-moi/trang+"+str(i)+".epi")
    scraping_link("https://baomoi.com/the-gioi/trang+"+str(i)+".epi")
    #----
    scraping_link("https://baomoi.com/thoi-su/trang+"+str(i)+".epi")
    scraping_link("https://baomoi.com/giao-thong/trang+"+str(i)+".epi")
    scraping_link("https://baomoi.com/moi-truong-khi-hau/trang+"+str(i)+".epi")
    #----
    scraping_link("https://baomoi.com/nghe-thuat/trang+"+str(i)+".epi")
    scraping_link("https://baomoi.com/am-thuc/trang+"+str(i)+".epi")
    scraping_link("https://baomoi.com/du-lich/trang+"+str(i)+".epi")
    #----
    scraping_link("https://baomoi.com/lao-dong-viec-lam/trang+"+str(i)+".epi")
    scraping_link("https://baomoi.com/tai-chinh/trang+"+str(i)+".epi")
    scraping_link("https://baomoi.com/chung-khoan/trang+"+str(i)+".epi")
    scraping_link("https://baomoi.com/kinh-doanh/trang+"+str(i)+".epi")
    #-----
    scraping_link("https://baomoi.com/hoc-bong-du-hoc/trang+" + str(i) + ".epi")
    scraping_link("https://baomoi.com/dao-tao-thi-cu/trang+" + str(i) + ".epi")
    #-----
    scraping_link("https://baomoi.com/bong-da-quoc-te/trang+" + str(i) + ".epi")
    scraping_link("https://baomoi.com/bong-da-viet-nam/trang+" + str(i) + ".epi")
    scraping_link("https://baomoi.com/quan-vot/trang+" + str(i) + ".epi")
    #---
    scraping_link("https://baomoi.com/am-nhac/trang+" + str(i) + ".epi")
    scraping_link("https://baomoi.com/thoi-trang/trang+" + str(i) + ".epi")
    scraping_link("https://baomoi.com/dien-anh-truyen-hinh/trang+" + str(i) + ".epi")
    #---
    scraping_link("https://baomoi.com/an-ninh-trat-tu/trang+" + str(i) + ".epi")
    scraping_link("https://baomoi.com/hinh-su-dan-su/trang+" + str(i) + ".epi")
    # ---
    scraping_link("https://baomoi.com/cntt-vien-thong/trang+" + str(i) + ".epi")
    scraping_link("https://baomoi.com/thiet-bi-phan-cung/trang+" + str(i) + ".epi")
    # ---
    scraping_link("https://baomoi.com/khoa-hoc/trang+" + str(i) + ".epi")
    # ---
    scraping_link("https://baomoi.com/dinh-duong-lam-dep/trang+" + str(i) + ".epi")
    scraping_link("https://baomoi.com/tinh-yeu-hon-nhan/trang+" + str(i) + ".epi")
    scraping_link("https://baomoi.com/suc-khoe-y-te/trang+" + str(i) + ".epi")
    # ---
    scraping_link("https://baomoi.com/xe-co/trang+" + str(i) + ".epi")
    # ---
    scraping_link("https://baomoi.com/quan-ly-quy-hoach/trang+" + str(i) + ".epi")
    scraping_link("https://baomoi.com/khong-gian-kien-truc/trang+" + str(i) + ".epi")
    print("--- %s seconds ---" % (time.time() - start))
f.close()












