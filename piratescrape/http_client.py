import requests

class HTTPClient(object):
    def __init__(self, default="https://thepiratebay.org"):
        self.session = requests.Session()
        self.default = default

    def get(self, page):
        self.session.get(self.default)
        resp = self.session.get(page)
        if resp.status_code != 200:
            raise Exception("Invalid Response")
        return resp.text
