from urllib.request import urlopen
from bs4 import BeautifulSoup
from model.News import News
import re
import json
import pymongo
import os


def getLink(url):
    html = urlopen(url)
    bs = BeautifulSoup(html, features="html.parser")
    return bs

def setup_Mongo():
    if os.getenv("MongoDB"):
        connection_string="mongodb+srv://" + os.getenv("Mongo_UserName") +':'+ os.getenv("Mongo_Password")+'@'+os.getenv("MongoDB")
        client = pymongo.MongoClient(connection_string)
    else:
        client = pymongo.MongoClient('localhost', 27017)
    db = client.kkbox
    collection = db.musicHeadlines
    return collection

def scrapePage(collection, link):
    curlPage = getLink(link)
    articles = curlPage.findAll("a", {"class": "cover"})
    for article in articles:
        news = getLink("http://www.kkbox.com"+article.attrs['href'])
        date = news.find("div", {"class": "column-author-date"}).get_text()
        title = news.find("h1").get_text()
        author = news.find(
            "div", {"class": "media-heading"}).find("span").get_text()
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
        newData = News(title, author, date, keywordArray, newContent, metaDict)
        collection.insert_one(newData.writeData())
