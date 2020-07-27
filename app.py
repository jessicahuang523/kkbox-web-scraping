from utils.setup import setup_Mongo
from utils.scraper import scrapePage, writeSetting
from utils.text_seg import ngram_tf, form_all_chi_para
from dotenv import load_dotenv
import sys

if __name__ == "__main__":
    # load environment variables
    load_dotenv()

    homePage = "https://www.kkbox.com/hk/tc/column/index.html"
    client = setup_Mongo()
    headline_collection = client.kkbox.headlines
    setting_collection = client.setting.last_update
    
    #for numPage in range(1, 4):
        #scrapePage(headline_collection, setting_collection, homePage + "?p=" + str(numPage))
    #writeSetting(setting_collection)

    #title = headline_collection.distinct("標題")
    #content = headline_collection.distinct("內容")
    title = ["我愛的人不是你愛的人喔", "但是我不愛的人是你喔"]
    content = ["你愛的人不是我愛的人喔", "但是我不恨的人是你喔"]
    tfidf_array = []

    for i in range(0, headline_collection.count()):
        paragragh = form_all_chi_para(title[i], content[i])
        tfidf_array.append(ngram_tf(2, paragragh))

    print("done")
    #tf done, testing idf


