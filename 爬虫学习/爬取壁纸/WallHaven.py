from bs4 import BeautifulSoup
import requests
import random
import 爬虫学习.工具目录.common_headers as my_headers
import 爬虫学习.工具目录.IP_Address_Pool as my_proxies


class WallPaperSpider(object):
    def __init__(self, website):
        self.url = website
        self.wallpaper_num = 0
        self.wallpaper_page = 1

    def get_html(self, url):
        b_overtime = True
        while b_overtime:
            try:
                my_header = my_headers.return_one_header()
                my_proxy = my_proxies.return_one_ip()
                soup = requests.get(url, headers=my_header, proxies=my_proxy, timeout=10)
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
    wallpaper_url = 'https://wallhaven.cc/search?categories=110&purity=100' \
                    '&resolutions=1920x1080&topRange=1M&sorting=toplist&order=desc&page='
    new_spider = WallPaperSpider(wallpaper_url)
    new_spider.download_wallpaper()














    




