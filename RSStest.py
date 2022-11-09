from bs4 import BeautifulSoup
import requests
import time
start=time.time()

def crawl():
    f = open("testingrss.txt", "w")

    url = requests.get('https://vnexpress.net/rss/the-thao.rss')

    soup = BeautifulSoup(url.content, 'xml')
    items = soup.find_all('item')

    for item in items:
        title = item.title.text
        print(title + '\n')
    # -------------------------------------------
    url = requests.get('https://vnexpress.net/rss/thoi-su.rss')

    soup = BeautifulSoup(url.content, 'xml')
    items = soup.find_all('item')

    for item in items:
        title = item.title.text
        print(title + '\n')
    # -------------------------------------------
    url = requests.get('https://vnexpress.net/rss/giao-duc.rss')

    soup = BeautifulSoup(url.content, 'xml')
    items = soup.find_all('item')

    for item in items:
        title = item.title.text
        print(title + '\n')
    # ------------------
    f.close()

crawl()
print("--- %s seconds ---" % (time.time() - start))