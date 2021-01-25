#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Author  :   {Mx}
@License :   (C) Copyright 2020-2021, {Nothing}
@Contact :   {YourEmail}
@Software:   PyCharm
@File    :   httprequests.py
@Time    :   2021/1/10 20:16
@Desc    :
'''

import requests
from common.testFile.loggers.loggs import logger
class HttpRequest:
    #
    # def __init__(self):
    #     pass

    def http_request(self,url,data,method,cookie=None):
        '''
        请求方法简单封装。
        :param url: http:ip:port/path
        :param data:
        :param method:
        :param cookie:
        :return:
        '''
        try:
            if method == 'get':
                response = requests.get(url,data=None,cookie=None)
            else:
                response = requests.post(url,data,cookie)
            return response
        except:
            print('参数有误，或请求方法不对')
...

if __name__ == '__main__':
    url = 'https://www.runoob.com/python/python-exceptions.html'
    req = HttpRequest()
    resp = req.http_request(url,'get')
    print(resp.text)
    pass
