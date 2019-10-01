import pymongo
import re
from operator import itemgetter

r = '[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~「」『』、：，。／　〉|〈（）｜ ]+'

def ngram(n, col):
    title = col.distinct("標題")
    content = col.distinct("內容")
    numOfArticle = col.count()
    for i in range(0, numOfArticle):
        article = title[i] + content[i]
        article = re.sub(r, '', article)
        article = re.sub('\n', '', article)
        freq = {}
        for i in range(0, len(article)-(n-1)):
            word = article[i:i+n]
            if word not in freq:
                freq[word] = 1
            else:
                freq[word] += 1
        freq = sorted(freq.items(), key=itemgetter(1), reverse=True)
        print(freq)
        print("---------------------------")