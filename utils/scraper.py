from urllib.request import urlopen
from bs4 import BeautifulSoup
from model.News import News
from utils.scheduling import compare
import re
import pymongo

# only the date of the first article matters since the articles are sorted from new to old
first = True

def getBS(url):
    html = urlopen(url)
    bs = BeautifulSoup(html, features="html.parser")
    return bs

def scrapePage(headlineCol, settingCol, url):
    curPage = getBS(url)
    articles = curPage.findAll("a", {"class": "cover"})
    for article in articles:
        news = getBS("http://www.kkbox.com"+article.attrs['href'])
        if settingCol.count()!=0 and compare(news, settingCol, headlineCol)==-1:
            # all new articles are scraped
            return
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
        headlineCol.insert_one(newData.writeData())
        global first
        if first:
            global latest
            latest = date
            # record the date of the first article
        first = False
        # only do this once each time this program runs

def writeSetting(settingCol):
    global latest
    settingCol.update({'標題': "上次更新"}, {'$set': {'日期': latest}}, upsert=True)
