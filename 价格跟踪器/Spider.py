from bs4 import BeautifulSoup
import requests
from tkinter import *
import re


def get_html(url):
    # 用try，except来捕获异常，是程序正常运行
    try:
        # 不论网站有无反趴机制，都要设置headers
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                          ' (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
        }
        r = requests.get(url, headers=headers, timeout=1)
        # 如果状态不是200，产生HTTPError异常
        r.raise_for_status()
        # 获取网页编码，并且编码格式设置为解析格式
        r.encoding = r.apparent_encoding
        return r.text
    except ConnectionError:
        Message("超时")


def parserHTML(html):
    soup = BeautifulSoup(html, "lxml")
    Price = soup.find_all('span')[1]
    LowPrice = Price.find_all('font', class_='bigwordprice')[0].get_text().strip()
    NowPrice = Price.find_all(string=re.compile('当前价'))[0].strip()
    NowPrice = re.findall(r'\d+.\d+', NowPrice)[0].strip()
    return LowPrice, NowPrice


def main(HTMLURL):
    url = "http://p.zwjhl.com/price.aspx?url="+str(HTMLURL)
    html = getHTML(url)
    return parserHTML(html)





