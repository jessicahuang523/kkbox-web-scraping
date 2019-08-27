from utils.scraper import searchUrl, construct_Mongo
from dotenv import load_dotenv
import sys

if __name__ == "__main__":
    # load environment variables
    load_dotenv()

    homePage = "https://www.kkbox.com/hk/tc/column/index.html"
    collection = construct_Mongo()
    for numPage in range(1, 6):
        searchUrl(collection, homePage + "?p=" + str(numPage))

    print("done")


