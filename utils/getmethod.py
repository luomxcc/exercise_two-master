#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Author  :   {MX}
@Contact :   {381493362}
@Software:   PyCharm
@File    :   getmethod.py
@Time    :   2020/7/14 22:14
@Desc    :
'''
import requests
import json

from utils.log import Logger


class HttpRrqurests(object):
    '''封装请求方法'''

    def get_method(self, url, data=None, header=None):
        '''
        封装get请求方法
        :param url:请求地址
        :param data:参数
        :param hander:请求头
        :return:
        '''
        if header is not None:
            response = requests.get(url, params=data, headers=header)
        else:
            response = requests.get(url, params=None)

        return response.json()

    def post_method(self, url, data=None, header=None):
        '''
        封装post请求方法
        :param url:
        :param data:
        :param hander:
        :return:
        '''
        if header is not None:
            response = requests.post(url, json=data, headers=header)
        else:
            response = requests.post(url, json=data)
        if str(response) == '<Response [200]>':
            return response.json()
        else:
            return response.text

    def put_method(self, url, data=None, header=None):
        '''
        封装put请求方法
        :param url:
        :param data:
        :param hander:
        :return:
        '''
        if header is not None:
            response = requests.put(url, json=data, headers=header)
        else:
            response = requests.put(url, json=data)
        return response.json()

    def delete_method(self, url, data=None, header=None):
        '''
        封装delete请求方法
        :param url:
        :param data:
        :param hander:
        :return:
        '''
        if header is not None:
            response = requests.delete(url, json=data, headers=header)
        else:
            response = requests.delete(url, json=data)
        return response.json()

    def run_method(self, method, url, data=None, header=None):
        if method == 'get' or method == 'GET':
            response = self.get_method(url, data, header)
        elif method == 'post' or method == 'POST':
            response = self.post_method(url, data, header)
        elif method == 'put' or method == 'PUT':
            response = self.put_method(url, data, header)
        elif method == 'delete' or method == 'DELETE':
            response = self.delete_method(url, data, header)
        else:
            print('请求方法不正确,请换个姿势再来一次!')
            response = '这个请求的姿势不对>>>>>>'
        # return json.dumps(response,ensure_ascii=False,indent=4,sort_keys=True,separators=(''))

        return json.dumps(response, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ':'))


...

if __name__ == '__main__':
    resq = HttpRrqurests()
    # url = "https://gateway-dev-k8s.smarteventcloud.cn/identity/login"
    # data = 'client_id=app-24&client_secret=smartx&grant_type=password&userName=ltest01&password=1&version=68'
    # header = {'Content-Type': 'application/x-www-form-urlencoded'}
    # res = resq.post_method(url,data,header)
    url = "https://gateway-dev-k8s.smarteventcloud.cn/api/mshop/shop/Shops?pageindex=1&pageSize=10&CityName={{gs_val}}&NL=31.24733&EL=121.446218&Keyword=妙手湘&Filters="
    hesder = {
        'Content-Type': 'application/json',
    }
    res = resq.run_method(url, hesder)
    print(res)

    pass
