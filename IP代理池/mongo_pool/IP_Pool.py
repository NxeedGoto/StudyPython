import sys
import pymongo
from IP代理池.IP_Model.IP_Model import Proxy
import logging


class MongoPool(object):
    def __init__(self):
        # 连接数据库
        self.client = pymongo.MongoClient(host='localhost', port='27017')
        # 获取操作的字典集，形如以下
        '''
        # 如果存在名为'proxy_pool'的数据库，则获取
        db = self.client['proxy_pool']
        # 如果存在名为'proxies'的数据表，则获取
        col = db['proxies']
        '''
        self.proxies = self.client['proxy_pool']['proxies']

    def __del__(self):
        self.client.close()

    def insert(self, proxy):
        # 代理IP插入方法
        count = self.proxies.count_documents({'_id': proxy.ip})
        if count == 0:
            # Proxy对象转化为字典
            proxy_dict = proxy.__dict__
            proxy_dict['_id'] = proxy.ip
            self.proxies.insert_one(proxy_dict)
            logging.info('插入新的代理: {}'.format(proxy))
        else:
            # 存在
            logging.warning('已存在代理{}'.format(proxy))

    def update(self, proxy):
        self.proxies.update_one({'_id': proxy.ip}, {'$set': proxy.__dict__})
        logging.info('更新代理IP: {}'.format(proxy))

    def find_all(self):
        # 查询数据库中所有的代理IP
        cursor = self.proxies.find()
        for Item in cursor:
            # 删除
            Item.pop('_id')
            proxy = Proxy(**Item)
            yield proxy

    def limit_find(self, conditions={}, count=0):
        # 根据条件查询
        cursor = self.proxies.find(conditions, count).sort([('score', pymongo.DESCENDING), ('speed', pymongo.ASCENDING)])
        # 接收查询所得的代理IP
        proxy_list = []
        for Item in cursor:
            Item.pop('_id')
            proxy = Proxy(**Item)
            proxy_list.append(proxy)
        return proxy_list

    def get_proxies(self, protocol=None, domain=None, nick_type=0, count=0):
        # 根据协议的类型和要访问网站的域名，获取代理IP列表











if __name__ == "__main__":
    Mongo = MongoPool()


