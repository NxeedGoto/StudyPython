# 代理IP的数据模型
class Proxy(object):
    def __init__(self, ip, port):
        # 代理IP的地址
        self.ip = ip
        # 代理IP的端口
        self.port = port

    def __str__(self):
        # 返回数据字符串
        return str(self.__dict__)

