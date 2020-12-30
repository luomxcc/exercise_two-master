#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Author  :   {Mx}
@License :   (C) Copyright 2020-2021, {Nothing}
@Contact :   {YourEmail}
@Software:   PyCharm
@File    :   testdemo1.py
@Time    :   2020/12/19 18:08
@Desc    :
'''

from common.requeststest import request
from common.apiinterface import *
from common.getUrl import myjoin
import unittest
'https://www.jianshu.com/users/recommended?seen_ids=&count=5&only_unfollowed=true'
'''
 https://www.jianshu.com/shakespeare/v2/notes/e9414cc7bf22/book
'''

url = 'https://www.jianshu.com'
data = 'seen_ids=&count=5&only_unfollowed=true'


def homepage():
    res = request.send_request("GET",myjoin(url,sodar) ,data)
    print(res.text)
def home2():
    res = request.send_request('get',myjoin(url,book))
    print(res.text)

...

if __name__ == '__main__':

    home2()
    pass
