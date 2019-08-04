from urllib.request import urlopen
from bs4 import BeautifulSoup

def getLink(url):
    html = urlopen(url)
    bs = BeautifulSoup(html)
    return bs

def scrapePage(link):
    page = getLink(link)
    articles = page.findAll("a", {"class": "cover"})
    for article in articles:
        news = getLink("http://www.kkbox.com"+article.attrs['href'])
        title = news.find("h1")
        contents = news.find("div", {"class": "column-article"}).findAll("p")
        keywords = news.findAll("li", {"class": "keyword"})
        print(">>>title<<<")
        print(title.get_text())
        print(">>>keyword<<<")
        for keyword in keywords:
            print(keyword.get_text())
        print(">>>content<<<")
        for content in contents:
            print(content.get_text())
        print("------------------------")

home = "https://www.kkbox.com/hk/tc/column/index.html"
scrapePage(home)
for noPage in range(2, 4):
    scrapePage(home + "?p=" + str(noPage))