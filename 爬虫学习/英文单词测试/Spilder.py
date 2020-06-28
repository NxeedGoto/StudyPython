import requests, re
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
HotFilmList = []
# 列表是拿来装热门电影的链接
SearchfilmList = []


# 列表是拿来装搜索电影的链接

def YesorNot(url):  # 检测链接类型
    a = 'magnet'
    b = 'ed2k'
    c = 'pan.baidu.com'
    A = ['magnet']
    B = ['ed2k']
    C = ['pan.baidu.com']
    patternA = re.compile(a)
    patternB = re.compile(b)
    patternC = re.compile(c)
    if patternA.findall(url) == A:
        print('这是个磁力链接')
    elif patternB.findall(url) == B:
        print('这是个种子链接')
    elif patternC.findall(url) == C:
        print('这是个百度网盘链接')
        BaiduYun(url)


def BaiduYun(url):  # 检测百度云网盘链接是否还生效
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    try:
        NotfoundError = soup.find('div', id="share_nofound_des")
        print(NotfoundError.text.strip())
    except AttributeError:
        print('此链接有效')


def RenRenFilm(FilmName):
    pattern = '<a.*?href="(.+)".*?>(.*?)style'
    url = 'http://yyetss.com/Detail/moviesearch?s_keys_movies=' + FilmName
    res = requests.get(url, headers=headers)
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    HotFilm = soup.find_all('div', class_="col-xs-4 col-sm-4 col-md-2 index-new-list")
    for A in HotFilm:
        HotFilm_Name = A.find('p')
        HotFilm_Ram1 = A.find_all('p')
        for AA in HotFilm_Ram1:
            try:
                HotFilm_Link = AA.find('a')['href']
            except TypeError:
                pass
            HotFilm_Ram2 = AA.find('a')
            if HotFilm_Ram2 != None:
                HotFilm_Ram = HotFilm_Ram2.text
        # print('''电影名：%s\n链接：%s\n大小：%s'''%(HotFilm_Name.text,HotFilm_Link,HotFilm_Ram))
        HotFilmList.append([HotFilm_Name.text, HotFilm_Link, HotFilm_Ram])
        pattern = re.compile(FilmName)
        if pattern.findall(FilmName) == pattern.findall(HotFilm_Name.text):
            print('推荐里有你搜索的内容哦~')
            print('''\33[1;33m电影名：\33[0m%s\n\33[1;33m链接：\33[0m%s\n\33[1;33m大小：\33[0m%s''' % (
            HotFilm_Name.text, HotFilm_Link, HotFilm_Ram))

    # 修改部分--------------------
    SearchFilm1 = soup.find('tbody')
    SearchFilm2 = SearchFilm1.find_all('tr')
    for BS in SearchFilm2:
        SearchFilm = BS.find_all('td')
        a = 0
        for C in SearchFilm:
            if C.text != None or C.text != '':
                # print(C.text.strip())
                if a == 0:
                    SearchFilm_Name = C.text.strip()
                    SearchfilmList.append({'电影名': SearchFilm_Name})
                    print('\33[1;33m电影名：\33[0m' + SearchFilm_Name)
                elif a == 1:
                    links = C.find_all('a')
                    for link in links:
                        film_link = link['href']
                        print('\33[1;33m链接：\33[0m' + film_link)
                elif a == 2:
                    SearchFilm_Ram = C.text.strip()
                    SearchfilmList.append({'内存大小': SearchFilm_Ram})
                    print('\33[1;33m内存大小：\33[0m' + SearchFilm_Ram)
                elif a == 3:
                    SearchFilm_resolution = C.text.strip()
                    SearchfilmList.append({'分辨率': SearchFilm_resolution})
                    print('\33[1;33m分辨率：\33[0m' + SearchFilm_resolution)
                elif a == 4:
                    SearchFilm_Subtilte = C.text.strip()
                    SearchfilmList.append({'字幕': SearchFilm_Subtilte})
                    print('\33[1;33m字幕：\33[0m' + SearchFilm_Subtilte)
                # print(C.text.strip())
            else:
                pass
            a += 1
            if a == 5:
                a = 0

FilmName = input('请输入电影名')
RenRenFilm(FilmName)

