headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
import requests,openpyxl
import re
from bs4 import BeautifulSoup
from urllib.request import quote
import time

URL4 = 'https://www.xinxs.la/3_3051/'

try:
    res4 = requests.get(URL4, headers=headers, verify=False, timeout=100)
    res4.encoding = 'utf-8'
    # 如果状态不是200，产生HTTPError异常
    res4.raise_for_status()
except TimeoutError and ConnectionError:
    print("超时")
except:
    print("Error")
html4 = res4.text
soup4 = BeautifulSoup(html4,'html.parser')
list = soup4.find('div', id='list')
dl = list.find('dl')
IsStart = False
for child in list.dl.contents:
    time.sleep(10)
    if child != '\n':
        if IsStart is True:
            lineS = ['VIP卷']
            pattern = re.compile(r'VIP卷')
            TextA = child.text
            if pattern.findall(TextA) != pattern.findall(lineS[0]):
                href = child.find('a')['href']
                #print(child.text + '\t' + "https://www.xinxs.la" + href)
                URL2 = "https://www.xinxs.la"+href
                res2 = requests.get(URL2, headers=headers, verify=False)
                res2.encoding = 'utf-8'
                html2 = res2.text
                soup2 = BeautifulSoup(html2, 'html.parser')
                Book_Names = soup2.find('div', class_="bookname")
                Book_Name = Book_Names.find('h1')
                Book_Name1 = Book_Name.text
                AA = '\n'
                AB = '\n'
                AC = '\n'
                AD = '\n'
                AE = '\n'
                Newfile = open('小说.txt', 'a', encoding='utf-8')
                Newfile.write(Book_Name1)
                Newfile.write(AA)
                Newfile.write(AB)
                Newfile.close()
                # print(Book_Name.text)
                List_All1 = soup2.find('div', id="content")
                for x in List_All1:
                    if x.string != None:
                        Newfile = open('小说.txt', 'a', encoding='utf-8')
                        Newfile.write(x)
                        Newfile.write(AC)
                        Newfile.close()
                Newfile = open('小说.txt', 'a', encoding='utf-8')
                Newfile.write(AD)
                Newfile.write(AE)
                Newfile.close()
        if re.match(re.compile(r'《遮天》正文'), child.text):
            IsStart = True