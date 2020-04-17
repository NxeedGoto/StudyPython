from bs4 import BeautifulSoup
import requests


class WallPaperSpider(object):
    def __init__(self):
        self.url = ''
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36"
                          " (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36"
        }

    def get_html(self, url):
        try:
            soup = requests.get(url=self.url, headers=self.headers, timeout=1)
            soup.raise_for_status()
            soup.encoding = soup.apparent_encoding
            return soup.text
        except RuntimeError and ConnectionError:
            print("超时")
        except Exception as e:
            print(e)

    def parser_html(self, url):
        soup = self.get_html(url)
        soup = BeautifulSoup(soup, "html.parser")
        return soup

    




