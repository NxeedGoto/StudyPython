from bs4 import BeautifulSoup
import requests
import 爬虫学习.工具目录.common_headers as my_headers
import random
import urllib.request


def get_html_text(url):
    b_overtime = True
    while b_overtime:
        try:
            my_header = {
                "User-Agent": random.choice(my_headers.common_headers)
            }
            request = requests.get(url, headers=my_header, timeout=10)
            request.raise_for_status()
            request.encoding = request.apparent_encoding
            b_overtime = False
            return request.text
        except ConnectionError and RuntimeError:
            print('timeout. waiting retry....')
        except Exception as e:
            print(e)


def get_ip_list(url):
    web_data = get_html_text(url)
    soup = BeautifulSoup(web_data, 'html.parser')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)
    # 检测ip可用性，移除不可用ip：（这里其实总会出问题，你移除的ip可能只是暂时不能用，剩下的ip使用一次后可能之后也未必能用）
    for ip in ip_list:
        try:
            proxy_host = "https://" + ip
            proxy_temp = {"https": proxy_host}
            res = urllib.request.urlopen(url, proxies=proxy_temp, timeout=10).read()
        except Exception as e:
            ip_list.remove(ip)
            continue
    return ip_list


def return_one_ip():
    web_url = 'http://www.xicidaili.com/nn/'
    ip_list_usable = get_ip_list(web_url)
    proxy_list = []
    for ip in ip_list_usable:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies


if __name__ == '__main__':
    print(return_one_ip())




















