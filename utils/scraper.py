from urllib.request import urlopen
from bs4 import BeautifulSoup
from model.News import News
import re
import json
import pymongo

def getLink(url):
    html = urlopen(url)
    bs = BeautifulSoup(html, features="html.parser")
    return bs

def writeMongo(data):
    client = pymongo.MongoClient('localhost', 27017)
    db = client.kkbox
    collection = db.musicHeadlines
    result = db.collection.insert_one(data)
    print(result)

def scrapePage(link):
    curlPage = getLink(link)
    articles = curlPage.findAll("a", {"class": "cover"})
    for article in articles:
        news = getLink("http://www.kkbox.com"+article.attrs['href'])
        title = news.find("h1").get_text()
        author = news.find("div", {"class": "media-heading"}).find("span").get_text()
        contents = news.find("div", {"class": "column-article"}).findAll("p")
        contentArray = []
        for content in contents:
            if content.find("img") or content.find("iframe") or content.find("a"):
                continue
            contentArray.append(content.get_text())
        newContent = ''.join(contentArray)
        keywords = news.findAll("li", {"class": "keyword"})
        keywordArray = []
        for keyword in keywords:
            if keyword.find("a"):
                continue
            keywordArray.append(keyword.get_text())
        metaDict = {}
        metaTags = news.findAll("meta", {"property": re.compile("^(og:)")})
        for metaTag in metaTags:
            metaDict[metaTag.attrs['property']] = metaTag.attrs['content']
        newData = News(title, author, keywordArray, newContent, metaDict)
        return newData.writeData()

