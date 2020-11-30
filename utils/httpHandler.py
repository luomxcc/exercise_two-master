# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/30 22:50
# @Author  : name
# @File    : httpHandler.py
import requests

'''
HTTP请求封装
'''


class ReuquestHandler:
    def get(self, url, **kwargs):
        """封装get方法"""
        # 获取请求参数
        params = kwargs.get("params")
        headers = kwargs.get("headers")
        try:
            reqult = requests.get(url, params=params, headers=headers)
            return
        except Exception as e:
            print("get请求错误: %s" % e)

    def post(self, url, **kwargs):
        '''封装post请求方法'''
        # 获取请求参数
        params = kwargs.get("params")
        data = kwargs.get("data")
        json = kwargs.get("json")
        try:
            reqult = requests.post(url, data=data, params=params, json=json)
            return reqult
        except Exception as e:
            print("post请求错误:%s" % e)

    def run_man(self, method, **kwargs):
        '''
        判断请求类型
        :param method:请求接口类型
        :param kwargs:选填参数
        :return:接口返回内容
        '''
        if method == "get":
            reqult = self.get(**kwargs)
            return reqult
        elif method == "post":
            reqult = self.post(**kwargs)
            return reqult
        else:
            print("接口请求类型错误,请检查请求方式.")


class RequestHandlers:
    def __init__(self):
        """session管理器"""
        self.session = requests.session()

    def visit(self, methon, url, params=None, data=None, json=None, headers=None, **kwargs):
        return self.session.request(methon, url, params=params, data=data, json=json, headers=headers, **kwargs)

    def close_session(self):
        '''关闭 session'''
        self.session.close()


...

if __name__ == '__main__':
    pass
