from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.kkbox.com/tw/tc/column/index.html?fbclid=IwAR0IHVM8a7TArfW7PWnZctF12DWln6n3iQ92uCWuflf9SvC9IEY55RQpc3k")
bs = BeautifulSoup(html)
title = bs.findAll("a", {"class": "cover"})[1]
print(title.attrs['title'])
link = "http://www.kkbox.com"+title.attrs['href']
html = urlopen(link)
bs = BeautifulSoup(html)
for string in bs.findAll("p"):
    print(string.get_text())
