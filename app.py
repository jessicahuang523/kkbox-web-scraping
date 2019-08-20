from utils.scraper import writeMongo, scrapePage, setup_Mongo
from dotenv import load_dotenv
import sys

if __name__ == "__main__":
    # load environment variables
    load_dotenv()
    client = setup_Mongo()

    # initiate variables
    data = {}
    data['音樂頭條'] = []

    homePage = "https://www.kkbox.com/hk/tc/column/index.html"
    for numPage in range(1, 4):
        d = scrapePage(homePage + "?p=" + str(numPage))
        data['音樂頭條'].append(d)

    #write to database
    writeMongo(client, data)


