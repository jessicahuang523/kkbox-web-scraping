class News():
    def __init__(self, title, author, date, keyword, content, album, meta):
        self.title = title
        self.author = author
        self.date = date
        self.keyword = keyword
        self.content = content
        self.album = album
        self.meta = meta
    
    def writeData(self):
        newData = {}
        newData['標題'] = self.title
        newData['作者'] = self.author
        newData['日期'] = self.date
        newData['關鍵字'] = self.keyword
        newData['內容'] = self.content
        newData['推薦專輯'] = self.album
        newData['meta'] = self.meta
        return newData

    