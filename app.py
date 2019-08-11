from utils.scraper import writeJson, scrapePage

if __name__ == "__main__":
    data = {}
    data['音樂頭條'] = []

    homePage = "https://www.kkbox.com/hk/tc/column/index.html"
    for numPage in range(1, 4):
        d = scrapePage(homePage + "?p=" + str(numPage))
        data['音樂頭條'].append(d)

    writeJson(data)