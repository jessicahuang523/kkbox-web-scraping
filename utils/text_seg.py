import pymongo
import re
from operator import itemgetter
from collection import Counter


def form_all_chi_para(title, content):
    r = '[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~「」『』、：，。／　〉|〈（）｜ ]+'
    para = title + content
    para = re.sub(r, '', para)
    para = re.sub('\n', '', para)
    return para

def ngram_tf(n, para):
        freq = {}
        for i in range(0, len(para)-(n-1)):
            word = para[i:i+n]
            if word not in freq:
                freq[word] = 1
            else:
                freq[word] += 1
        total = sum(freq.values())
        for j in freq:
            freq[j] = freq[j]/total
        print("---------------------------")
        #freqArray = sorted(freq.items(), key=itemgetter(1), reverse=True)
        return freq

def idf():