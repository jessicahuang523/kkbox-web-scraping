from utils.setup import setup_Mongo
from utils.scraper import scrapePage, writeSetting
from dotenv import load_dotenv
import sys

if __name__ == "__main__":
    # load environment variables
    load_dotenv()

    homePage = "https://www.kkbox.com/hk/tc/column/index.html"
    client = setup_Mongo()
    headline_collection = client.kkbox.headlines
    setting_collection = client.setting.last_update
    
    for numPage in range(1, 6):
        scrapePage(headline_collection, setting_collection, homePage + "?p=" + str(numPage))
    writeSetting(setting_collection)

    print("done")


