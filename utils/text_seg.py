import pymongo
from operator import itemgetter

def ngram(n, col):
    title = col.distinct("標題")
    content = col.distinct("內容")
    numOfArticle = col.count()
    for i in range(0, numOfArticle):
        article = title[i] + content[i]
        bifreq = {}
        for i in range(0, len(article)-1):
            bi = article[i:i+2]
            if bi not in bifreq:
                bifreq[bi] = 1
            else:
                bifreq[bi] += 1
        bifreq = sorted(bifreq.items(), key=itemgetter(1), reverse=True)
        print(bifreq)
        print("---------------------------")
