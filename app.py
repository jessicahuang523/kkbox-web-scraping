from utils.scraper import scrapePage
from dotenv import load_dotenv
import sys

if __name__ == "__main__":
    # load environment variables
    load_dotenv()

    homePage = "https://www.kkbox.com/hk/tc/column/index.html"
    for numPage in range(1, 4):
        scrapePage(homePage + "?p=" + str(numPage))

    print("done")


