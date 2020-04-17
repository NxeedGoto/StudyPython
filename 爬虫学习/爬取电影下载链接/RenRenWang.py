from bs4 import BeautifulSoup
import requests
import re


class StructFileData(object):
    def __init__(self):
        self.film_name = ""
        self.film_data = ""
        self.film_status = ""
        self.film_download_name = []
        self.film_download_link = []


class RenRenWang(object):
    def __init__(self, filename):
        self.filename = filename
        self.url = "http://yyetss.com/Search/index/?s_keys=" + filename
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36"
                          " (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36"
        }
        self.list_film_date = []
        self.get_film_data()

    def get_html(self, url):
        try:
            r = requests.get(url, headers=self.headers, timeout=1)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.text
        except ConnectionError:
            print("超时")

    def parser_html(self, url):
        html = self.get_html(url)
        soup = BeautifulSoup(html, "html.parser")
        return soup

    def get_result(self, url):
        soup = self.parser_html(url)
        jumbortron = soup.find('div', class_='jumbotron')
        container = jumbortron.find('div', class_='container')
        result = container.find('p').string
        result = re.findall('共：(.*?)条结果', result)[0]
        return result

    def get_film_data(self):
        if self.get_result(self.url) == 0:
            print("没有查询到结果")
        else:
            soup = self.parser_html(self.url)
            film_dates = soup.find_all('div', class_="col-xs-3 col-sm-3 col-md-2 min-height-category")
            for film_date in film_dates:
                struct_film_temp = StructFileData()
                film_date_temp = film_date.find('div', class_="min-height:25px;display:block")
                film_link = film_date_temp.find('a')['href']
                self.get_download_link(film_link, struct_film_temp)
                struct_film_temp.film_link = film_link
                film_names = film_date_temp.find_all('p')
                col = 0
                for film_name in film_names:
                    if col == 0:
                        struct_film_temp.film_name = film_name.text
                    elif col == 1:
                        struct_film_temp.film_status = film_name.text
                    else:
                        struct_film_temp.film_data = film_name.text
                    col = col + 1
                self.list_film_date.append(struct_film_temp)

    def get_download_link(self, movie_link, struct_film_temp):
        soup = self.parser_html(movie_link)
        film_all_data = soup.find_all('div', class_="col-xs-12 col-sm-12 col-md-12")
        for film_data in film_all_data:
            film_data = film_data.find_all(class_="tab_set_info")
            if film_data is not None:
                for film_downloads in film_data:
                    film_downloads = film_downloads.find_all('li')
                    for film_download in film_downloads:
                        film_download_link = film_download.find('a')['href']
                        film_download_name = film_download.find('a').text
                        if re.match(re.compile(r'https'), film_download_link) or \
                                re.match(re.compile(r'magnet'), film_download_link) or \
                                re.match(re.compile(r'thunder'), film_download_link):
                            struct_film_temp.film_download_name.append(film_download_name)
                            struct_film_temp.film_download_link.append(film_download_link)


def main(movie_name):
    ren_ren = RenRenWang(movie_name)
    for film in ren_ren.list_film_date:
        print("")
        print('电影：   ' + film.__dict__['film_name'])
        print('出版时间：' + film.__dict__['film_data'])
        print('状态：   ' + film.__dict__['film_status'])
        print("------------------下载链接--------------------")
        for i in range(len(film.__dict__['film_download_name'])):
            print("名称： " + film.__dict__['film_download_name'][i])
            print("链接:  " + film.__dict__['film_download_link'][i])
        print("--------------------------------------------")


def input_movie():
    print('''
———————————————————————————————————————————————————
                目前版本1.0
        【影库】：阳光网 | 人人影视(TV)
———————————————————————————————————————————————————
''')
    movie_name = input('请输入电影名/美剧名：')
    return movie_name


if __name__ == '__main__':
    while True:
        main(str(input_movie()))





