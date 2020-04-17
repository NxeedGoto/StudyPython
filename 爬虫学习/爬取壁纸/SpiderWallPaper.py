from bs4 import BeautifulSoup
import requests
import random
from urllib.request import urlretrieve


proxy_list = [
    '183.95.80.102:8080',
    '123.160.31.71:8080',
    '115.231.128.79:8080',
    '166.111.77.32:80',
    '43.240.138.31:8080',
    '218.201.98.196:3128'
]

# 收集到的常用Header
my_headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko)"
    " Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14"
    " (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko)"
    " Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
]

# 随机从列表中选择IP、Header
random_proxy = random.choice(proxy_list)
random_header = {
    "User-Agent": random.choice(my_headers)
}


class WallPaperSpider(object):
    def __init__(self, website):
        self.url = website
        self.headers = random_header
        self.wallpaper_num = 0
        self.wallpaper_page = 1

    def get_html(self, url):
        b_overtime = True
        while b_overtime:
            try:
                soup = requests.get(url, headers=self.headers, timeout=10)
                soup.raise_for_status()
                soup.encoding = soup.apparent_encoding
                b_overtime = False
                return soup.text
            except RuntimeError and ConnectionError:
                print("超时,继续")
                b_overtime = True
            except Exception as e:
                print(e)

    def parser_html(self, url):
        soup = self.get_html(url)
        soup = BeautifulSoup(soup, "html.parser")
        return soup

    def download_wallpaper(self):
        url = self.url
        url += str(self.wallpaper_page)
        self.wallpaper_page += 1
        soup = self.parser_html(url)
        section = soup.find('section', class_='thumb-listing-page')
        lis = section.find_all('li')
        if len(lis) is 0:
            print('下载结束')
            exit(0)
        for li in lis:
            image_preview = li.find('a', class_='preview')['href']
            self.get_wallpaper_link(image_preview)
        self.download_wallpaper()

    def get_wallpaper_link(self, url):
        soup = self.parser_html(url)
        download_link = soup.find('img', id='wallpaper')['src']
        self.save_image(download_link)

    def save_image(self, url):
        b_overtime = True
        while b_overtime:
            try:
                wallpaper = requests.get(url, timeout=5)
                b_overtime = False
            except RuntimeError and ConnectionError:
                print("超时,继续")
                b_overtime = True
            except Exception as e:
                print(e)
        file_name = '图片' + str(self.wallpaper_num) + '.jpg'
        self.wallpaper_num += 1
        print('下载' + file_name)
        file_path = '.\\存放壁纸\\' + file_name
        with open(file_path, 'wb') as fp:
            fp.write(wallpaper.content)


if __name__ == '__main__':
    wallpaper_url = 'https://wallhaven.cc/search?categories=001&purity=110&' \
                    'resolutions=1920x1080&topRange=1M&sorting=toplist&order=desc&page='
    new_spider = WallPaperSpider(wallpaper_url)
    new_spider.download_wallpaper()














    




