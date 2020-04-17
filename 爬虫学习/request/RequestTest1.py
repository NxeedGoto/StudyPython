# 导入模块
import requests
import json

"""
# 尝试获取一个网页 - 初始化了一个Response的对象r
r = requests.get('https://api.github.com/events')

# HTTP POST 请求方式
r = requests.post('https://hhtpbin.org/post', data = {'key': 'value'})

r = requests.put('https://httpbin.org/put', data = {'key':'value'})
r = requests.delete('https://httpbin.org/delete')
r = requests.head('https://httpbin.org/get')
r = requests.options('https://httpbin.org/get')
"""

"""
# 在网址中传递参数
payload = {'key1' : 'value1', 'key2' : 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.url)
"""

"""
# 响应内容
r = requests.get('https://www.baidu.com')
print(r.text)           # 文本编码响应内容
print(r.encoding)
print(r.content)        # 二进制响应内容
# print(r.json())         # json响应内容  解码失败则会引发异常

print('\n', r.raw)            # 原始响应内容
print('\n', r.raw.read(10))
"""

"""
# 自定义页眉
url = "http://www.baidu.com"
header = {'user-agent' : 'my-app/0.01'}
r = requests.get(url, headers=header)

payload_tuples = [('key1', 'value1'), ('key1', 'value2')]
r1 = requests.post('https://httpbin.org/post', data=payload_tuples)
payload_dict = {'key1': ['value1', 'value2']}
r2 = requests.post('https://httpbin.org/post', data=payload_dict)
print(r1.text)
"""
"""
# 响应状态码
r = requests.get('http://www.baidu.con')
r.status_code                               # 响应状态代码
r.status_code == requests.codes.ok
"""

"""
# 错误请求（4xx客户端错误或5xx服务器错误响应）
bad_r = requests.get('https://httpbin.org/status/404')
print(bad_r.status_code)
bad_r.raise_for_status()
"""

"""
# 响应头
r = requests.get('http://www.baidu.com')
print(r.headers)
print('\n ', r.headers['content-type'])
print('\n ', r.headers.get('content-type'))
"""

"""
# Cookie
url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)
print(r.cookies)
"""

