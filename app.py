from utils.setup import setup_Mongo
from utils.scraper import scrapePage, writeSetting
from utils.text_seg import ngram
from dotenv import load_dotenv
import sys

if __name__ == "__main__":
    # load environment variables
    load_dotenv()

    homePage = "https://www.kkbox.com/hk/tc/column/index.html"
    client = setup_Mongo()
    headline_collection = client.kkbox.headlines
    setting_collection = client.setting.last_update
    
    #for numPage in range(1, 2):
        #scrapePage(headline_collection, setting_collection, homePage + "?p=" + str(numPage))
    #writeSetting(setting_collection)
    ngram(2, headline_collection)
    print("done")


