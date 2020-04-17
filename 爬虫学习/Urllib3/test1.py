# 1. 导入urllib3模块
import urllib3
import json

# 2. 创建PoolManage实例来发出请求。该对象处理连接池和线程安全性的所有详细信息
http = urllib3.PoolManager()

"""
# 3. 要发出请求
r = http.request('GET', 'http://httpbin.org/robots.txt')
print(r.data)

r = http.request('POST', \
                 'http://httpbin.org/post', \
                 fields={'hello': 'world'})

r = http.request('GET', 'http://httpbin.org/ip')
print(r.status)
print(r.data)
print(r.headers)
"""

r = http.request('GET', 'http://httpbin.org/ip')
print(json.loads(r.data.decode('utf-8')))

r = http.request('GET',\
                 'http://httpbin.org/headers',\
                 headers={'X-Something': 'value'})
print(json.loads(r.data.decode('utf-8'))['headers'])