from urllib.request import urlopen
from bs4 import BeautifulSoup
from model.News import News
import re
import json
import pymongo

first = True

def compare(news, settingCol, headlineCol):
    d1 = news.find("div", {"class": "column-author-date"}).get_text()
    d2 = settingCol.find_one({'標題': "上次更新"})['日期']
    if d1>d2:
        return 1
    elif d1<d2:
        return -1
    else:
        title = news.find("h1").get_text()
        inDB = headlineCol.find_one({'標題': title})
        if inDB:
            return -1
        else:
            return 0

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
        first = False

def writeSetting(settingCol):
    global latest
    settingCol.update({'標題': "上次更新"}, {'$set': {'日期': latest}}, upsert=True)
