#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Author  :   {Mx}
@License :   (C) Copyright 2020-2021, {Nothing}
@Contact :   {YourEmail}
@Software:   PyCharm
@File    :   requeststest.py
@Time    :   2020/12/19 17:04
@Desc    :
'''

import json
import requests


class HttpReuqest(object):
    '''简单封装http请求方法'''

    def __init__(self):
        self.session = requests.Session()

    def send_request(self, method, url, params_type='form', data=None, **kwargs):

        method = method.upper()
        params_type = params_type.upper()
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except Exception:
                data = eval(data)
        if 'GET' == method:
            response = self.session.request(method=method, url=url, params=data, **kwargs)
        elif 'POST' == method:
            if params_type == 'FORM':  # 发送表单数据，使用data传参
                response = self.session.request(method=method, url=url, data=data, **kwargs)
            elif params_type == 'JSON':  # 如果接口支持application/json类型，则使用json参数传递
                response = self.session.request(method=method, url=url, json=data, **kwargs)
            else:  # 如果接口需要传递其他类型的数据比如 上传文件，调用下面的请求方法
                response = self.session.request(method=method, url=url, **kwargs)
            # 如果请求方式非 get 和post 会报错，当然你也可以继续添加其他的请求方法
        else:
            raise ValueError('request method"{}" error!please check'.format(method))
        return response

    def __call__(self, method, url, params_tpye='form', data=None, **kwargs):
        return self.send_request(method=method, url=url, params_tpye=params_tpye, data=data, **kwargs)

    def close_session(self):
        self.session.close()
        try:
            del self.session.cookies['JSESSIONID']
        except:
            pass


request = HttpReuqest()

# request = requests.get('https://www.cnblogs.com/linuxchao/ajax/signature.aspx?blogId=438209')
# print(request.text)

...

if __name__ == '__main__':
    pass
