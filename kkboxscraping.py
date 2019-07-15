from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.kkbox.com/tw/tc/column/index.html?fbclid=IwAR0IHVM8a7TArfW7PWnZctF12DWln6n3iQ92uCWuflf9SvC9IEY55RQpc3k")
bs = BeautifulSoup(html)
for title in bs.findAll("a", {"class": "cover"}):
    print(title.attrs['title'])