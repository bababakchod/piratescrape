class Torrent:
    def __init__(self, name="", url="", magnet_url="", seeders=0, leechers=0, uploaded_by="", uploaded_at=""):
        self.name = name
        self.url = url
        self.magnet_url = magnet_url
        self.seeders = seeders
        self.leechers = leechers
        self.uploaded_by = uploaded_by
        self.uploaded_at = uploaded_at
    
    def jsonify(self):
        json = ''
        json += '{'
        json += '"name": ' + '"' + self.name + '"' + ','
        json += '"url": ' + '"' + self.url + '"' + ','
        json += '"magnet_url": ' + '"' + self.magnet_url + '"' + ','
        json += '"seeders": ' + '"' + str(self.seeders) + '"' + ','
        json += '"leechers": ' + '"' + str(self.leechers) + '"' + ','
        json += '"uploaded_by": ' + '"' + self.uploaded_by + '"' + ','
        json += '"uploaded_at": ' + '"' + self.uploaded_at + '"'
        json += '}'
        return json

if __name__=='__main__':
    t = Torrent()
    t.name = "Monty Python"
    t.url = "someshadyurl.com/file.torrent"
    t.magnet_url = "maqwrgnet:?blablabla"
    t.seeders = 123
    t.leechers = 50
    t.uploaded_by = "YIFY"
    t.uploaded_at = "20/10/2009"
    print(t.jsonify())

