from bs4 import BeautifulSoup
import requests
import 爬虫学习.工具目录.common_headers as my_headers
import 爬虫学习.工具目录.IP_Address_Pool as my_proxies
import 爬虫学习.工具目录.ExcelOperation as my_excel


row_numb = 2


def get_html_text(url):
    b_overtime = True
    while b_overtime:
        try:
            my_header = my_headers.return_one_header()
            my_proxy = my_proxies.return_one_ip()
            request = requests.get(url, headers=my_header, proxies=my_proxy, timeout=10)
            request.raise_for_status()
            request.encoding = request.apparent_encoding
            b_overtime = False
            return request.text
        except ConnectionError and RuntimeError:
            print('timeout, retry...')
        except Exception as e:
            print(e)


def parser_html(url):
    web_text = get_html_text(url)
    soup = BeautifulSoup(web_text, 'html.parser')
    return soup


def skin_kinds(url, excel_operation):
    soup = parser_html(url)
    skin_item_kinds = soup.find_all('div', class_='items')
    for skin_item_kind in skin_item_kinds:
        skin_item_kind_name = skin_item_kind.find('div', class_='detailsCa')
        if skin_item_kind_name is not None:  # 过滤掉所有
            skin_item_type_name = skin_item_kind.find('div', class_='type')
            skin_item_type_name = skin_item_type_name.find('a')
            skin_item_type_name = skin_item_type_name.text.strip()      # strip()： 去除字符串中的空格和换行
            # print('  枪械种类: ' + skin_item_type_name)    # 输出枪的类型名 （手枪、冲锋枪、...)
            # print('=====================================================')
            skin_item_kind_list = skin_item_kind_name.find('div', class_=list)
            skin_item_kind_name_list = skin_item_kind_list.find_all('a', class_='single')
            for skin_item_name in skin_item_kind_name_list:
                skin_item_link = skin_item_name['href']
                skin_item_name = skin_item_name.text.strip()
                # print('  枪械类别: ' + skin_item_name)
                # print('---------------------------------------------------')
                skin_item_link = 'https://www.igxe.cn' + skin_item_link + '&page_no='
                skin_name_wear_price(skin_item_link, 1, excel_operation)     # 从第一页开始
                # print('---------------------------------------------------')
            # print('=====================================================')


def skin_name_wear_price(url, page_num, excel_operation):
    global row_numb
    page_url = url + str(page_num)
    soup = parser_html(page_url)
    data_list = soup.find('div', class_='dataList')
    data_all = data_list.find_all('a', class_='single csgo')
    if len(data_all) != 0:      # 当前页有数据
        for data in data_all:
            skin_wear = data.find('div', class_='label')
            skin_wear = skin_wear.text.strip()
            # print('  磨损级别: ' + skin_wear)  # 磨损级别
            excel_operation.write_in_cell(row_numb, 2, str(skin_wear))
            skin_name = data.find('div', class_='name')
            skin_name = skin_name.text.strip()
            # print('  皮肤名称: ' + skin_name)  # 皮肤名称
            excel_operation.write_in_cell(row_numb, 1, skin_name)
            skin_low_price_data = data.find('div', class_='price fl')
            skin_low_price = ''
            for skin_low_price_constitute in skin_low_price_data.contents:
                if skin_low_price_constitute != '\n':
                    skin_low_price += str(skin_low_price_constitute.text.strip())
            # print('  现最低价: ' + skin_low_price)  # 当前最低价
            # print('')
            excel_operation.write_in_cell(row_numb, 3, str(skin_low_price))
            row_numb += 1
        # 读取下一页数据
        skin_name_wear_price(url, page_num + 1, str(excel_operation))
        print('next')


if __name__ == '__main__':
    web_url = 'https://www.igxe.cn/csgo/730?sort=3'
    excel = my_excel.ExcelOperation('IGXE.xlsx')
    skin_kinds(web_url, excel)
    del excel



