from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import json

def getLink(url):
    html = urlopen(url)
    bs = BeautifulSoup(html)
    return bs

def writeJson(data):
    with open("output.json", "w") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
        file.close

def scrapePage(link):
    page = getLink(link)
    articles = page.findAll("a", {"class": "cover"})
    for article in articles:
        news = getLink("http://www.kkbox.com"+article.attrs['href'])
        title = news.find("h1")
        author = news.find("div", {"class": "media-heading"}).find("span")
        contents = news.find("div", {"class": "column-article"}).findAll("p")
        keywords = news.findAll("li", {"class": "keyword"})
        newData = {}
        newData['標題'] = title.get_text()
        newData['作者'] = author.get_text()
        contentArray = []
        for content in contents:
            if content.find("img") or content.find("iframe") or content.find("a"):
                continue
            contentArray.append(content.get_text())
        newContent = ''.join(contentArray)
        newData['內容'] = newContent
        newData['關鍵字'] = []
        for keyword in keywords:
            if keyword.find("a"):
                continue
            newData['關鍵字'].append(keyword.get_text())
        newData['meta'] = {}
        metaTags = news.findAll("meta", {"property": re.compile("^(og:)")})
        for metaTag in metaTags:
            newData['meta'][metaTag.attrs['property']] = metaTag.attrs['content']
        data['音樂頭條'].append(newData)
data = {}
data['音樂頭條'] = []

home = "https://www.kkbox.com/hk/tc/column/index.html"
for noPage in range(1, 4):
    scrapePage(home + "?p=" + str(noPage))

writeJson(data)