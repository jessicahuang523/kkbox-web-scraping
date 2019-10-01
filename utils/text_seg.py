import pymongo
import re
from operator import itemgetter


def ngram_tfidf(n, col):
    r = '[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~「」『』、：，。／　〉|〈（）｜ ]+'
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
        total = sum(freq.values())
        for j in freq:
            freq[j] = freq[j]/total
        freqArray = sorted(freq.items(), key=itemgetter(1), reverse=True)
        print(freqArray)
        print("---------------------------")