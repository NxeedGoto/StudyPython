from bs4 import BeautifulSoup
import requests
from tkinter import *


def getHTML(url):
    # 用try，except来捕获异常，是程序正常运行
    try:
        # 不论网站有无反趴机制，都要设置headers
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/77.0.3865.120 Safari/537.36'
        }
        r = requests.get(url, headers=headers)
        # 如果状态不是200，产生HTTPError异常
        r.raise_for_status()
        # 获取网页编码，并且编码格式设置为解析格式
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "error"


def parserHTML(html, text):
    soup = BeautifulSoup(html, "lxml")
    # 找到所有的<ol>
    ols = soup.find_all('ol')
    for ol in ols:
        # 在ol中找到li标签，因为每一个li标签里面存储着一部电影的信息
        lis = ol.find_all('li')
        for li in lis:
            # 找到电影的排名
            index = li.find_all('em')[0]
            # 找到电影的名称
            title = li.find_all('span', class_='title')[0]
            # 找到电影的评分
            rate_num = li.find_all('span', class_='rating_num')[0]
            # LstBox.insert()
            # ListTitle.append([])
            text.insert(END, "{0:^10}\t{1:{3}^10}\t{2:^10}"
                        .format(index.string, title.string, rate_num.string, chr(12288))+'\n')

            """
            # 打印出一部电影的信息
            print("{0:^10}\t{1:{3}^10}\t{2:^10}".format(index.string, title.string, rate_num.string, chr(12288)))
            # open (name, mode, encoding)
            # name是包含包含文件名称的字符串
            # mode决定打开文件的模式('r': 只读，'w': 只写，果不存在在文件的后面追加，'a'：附加在问文件的末尾）
            # #encoding表示我们要输入的编码方式
            with open('douban250.text', 'a', encoding='utf--8') as f:
                # 把爬取到的排名，名称，评分写入文件。
                f.write("{0:^10}\t{1:{3}^10}\t{2:^10}\n".format(index.string, title.string, rate_num.string, chr(12288)))
                # 保证数据及时从缓存存入本地。
                f.flush()
            """


def main(start, text):
    url = "https://movie.douban.com/top250?start="+str(start)
    html = getHTML(url)
    parserHTML(html, text)


if __name__ == '__main__':
    root = Tk()
    root.title('豆瓣Top250电影')
    root.geometry('320x240')
    text = Text(root)
    text.pack()
    text.insert(END, "{0:^10}\t{1:{3}^10}\t{2:^10}"
                .format('排名', '电影名', '评分', chr(12288))+'\n')
    for i in range(10):
        main(i * 25, text)
    root.mainloop()

