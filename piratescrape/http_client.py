import requests

class HTTPClient:
    def __init__(self):
        self.session = requests.Session()

    def get_tpb(self, page):
        self.session.get("https://thepiratebay.org")
        resp = self.session.get(page)
        #if resp.status_code != "200":
        #    raise Exception("Invalid Response")
        return self.session.get(page).text

if __name__=='__main__':
    # test the tpb getter
    client = HTTPClient()
    resp = client.get_tpb("https://thepiratebay.org/search/python/0/99/0")
    ok = str("magnet" in resp)
    print(ok)
    
