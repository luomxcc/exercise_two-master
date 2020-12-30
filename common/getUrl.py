#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Author  :   {Mx}
@License :   (C) Copyright 2020-2021, {Nothing}
@Contact :   {YourEmail}
@Software:   PyCharm
@File    :   getUrl.py
@Time    :   2020/12/29 20:52
@Desc    :
'''
from common.apiinterface import *
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.parse import urlunparse
from posixpath import normpath

def myjoin(base,url):
    '''
    拼接URL链接
    :param base:
    :param url: URL
    :return:
    '''
    url1 = urljoin(base,url)
    arr = urlparse(url1)
    path = normpath(arr[2])
    return urlunparse((arr.scheme,arr.netloc,path,arr.params,arr.query,arr.fragment))





...

if __name__ == '__main__':

    pass
