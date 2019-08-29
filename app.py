from utils.scraper import scrapePage, setup_Mongo
from dotenv import load_dotenv
import sys

if __name__ == "__main__":
    # load environment variables
    load_dotenv()

    homePage = "https://www.kkbox.com/hk/tc/column/index.html"
    collection = setup_Mongo()
    for numPage in range(2, 3):
        scrapePage(collection, homePage + "?p=" + str(numPage))

    print("done")


