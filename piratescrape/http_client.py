import requests

class HTTPClient:
	def __init__(self):
		self.session = requests.Session()
	
	def get_tpb(self, page):
		self.session.get("https://thepiratebay.org")
		resp = self.session.get(page)
		if resp.status_code != "200":
			raise "Invalid Response"
		return self.session.get(page).text

