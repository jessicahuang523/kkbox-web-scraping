def compare(news, settingCol, headlineCol):
    d1 = news.find("div", {"class": "column-author-date"}).get_text()
    d2 = settingCol.find_one({'標題': "上次更新"})['日期']
    if d1>d2:
        return 1
    elif d1<d2:
        return -1
    else:
        title = news.find("h1").get_text()
        inDB = headlineCol.find_one({'標題': title})
        if inDB:
            return -1
        else:
            return 0