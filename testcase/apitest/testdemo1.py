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
data = 'class=Order&method=iGetSingleMeetingOrderDetailV2&params=%7B%22start_day%22%3A%22%22%2C%22sid%22%3A%22aaego8unatvj7i6kue6lk29b26%22%2C%22jobId%22%3A%1c619b37-d9b3-4242-8aef-baa233b6a7ba%22%7D'
headers = {
    'Content-Type':'application/json; charset=UTF-8',
    'Cookie':'_ga=GA1.2.1497790954.1607785740; __yadk_uid=syluTiylrdpa77flakttDkvd30QkrQ60; read_mode=day; default_font=font2; locale=zh-CN; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1609939600,1609939820,1609939863,1609939872; remember_user_token=W1syNTYwMDY0Ml0sIiQyYSQxMSR2MTRjeDh4ejE1UkpvVTVTMWMxMy91IiwiMTYwOTk0MDE1NS43MTc1NTMiXQ%3D%3D--d1d44a51de6541d887e402c742b878bb53798688; web_login_version=MTYwOTk0MDE1NQ%3D%3D--9cb2451c349cd403ce905eaa073116158c90c57e; _m7e_session_core=114d772b11774969d5608b1aa4eed849; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22176577f77c322c-02946a94e6c0e1-163a6153-1296000-176577f77c4ecb%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D%2C%22%24device_id%22%3A%22176577f77c322c-02946a94e6c0e1-163a6153-1296000-176577f77c4ecb%22%7D; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1609940233'
}
datas = {
	"id": "82217307",
	"autosave_control": 10,
	"title": "随笔",
	"content": "<p>这是一篇简单的随笔。</p>"
}


def apirequest_get1():
    res = request.send_request("GET",myjoin(url,sodar) ,data)
    print(res.text)

def apirequest_get2():
    res = request.send_request('get',myjoin(url,book))
    print(res.text)

def apirequest_post():
    res = request.send_request('POST',myjoin(url,diary),headers,data)
    print(res.text)
    pass


def apirequest_post2():
    url = "https://gateway.smarteventcloud.cn/api/foundation/bpm/foundation/workflow/v2/Task/PagingTMISTasks"
    payload = "{\n    \"pageIndex\": 1,\n    \"pageSize\": 10,\n    \"filters\": {\n        \"datasourceids\": \"14c6b6b9-9254-4cc0-88ff-cd84cf2ca191\",\n        \"col7\": 0,\n        \"flowCode\": \"TMIS-Lilly\",\n        \"col9\": \"小型区域会\"\n    },\n    \"sorts\": {\n        \"col2\": 1,\n        \"ts\": 1\n    }\n}"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': ' Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImZmNDI4MDRlNzQxMTY5ODJkODE0NmRmYzEzYjczMTg0IiwidHlwIjoiSldUIn0.eyJuYmYiOjE2MDk5NDEyNDQsImV4cCI6MTY0MTA0NTI0NCwiaXNzIjoiaHR0cDovL3Bhc3Nwb3J0LnNtYXJ0eGNsb3VkLmNuIiwiYXVkIjpbImh0dHA6Ly9wYXNzcG9ydC5zbWFydHhjbG91ZC5jbi9yZXNvdXJjZXMiLCJBcGlzLkFkbWluIiwiQXBpcy5DaGVja0FjY291bnQiLCJBcGlzLkNvbmZpZ3VyYXRpb24iLCJBcGlzLkV2ZW50IiwiQXBpcy5GaWxlIiwiQXBpcy5GbG93IiwiQXBpcy5Gb3VuZGF0aW9uIiwiQXBpcy5JZGVudGl0eSIsIkFwaXMuSW52b2ljZSIsIkFwaXMuTWVhbCIsIkFwaXMuTWVzc2FnZSIsIkFwaXMuTXlQcm9maWxlIiwiQXBpcy5TaG9wS2VlcGVyIiwiQXBpcy5TbWFydEFsaXBheSIsIkFwaXMuU21hcnRFdmVudCIsIkFwaXMuU21hcnRKb2IuRmluIiwiQXBpcy5WZW51ZSIsImVjLm9yZGVyIiwicGFzc3BvcnQiLCJyZXMudmVudWUiLCJzbWFydHhhcHAiLCJ3b3JrZmxvdyJdLCJjbGllbnRfaWQiOiJhcHAtMjQiLCJzdWIiOiI5YjRkY2UwMy1mMmIzLTExZTgtOGVjNy0wMjQyYWMxMjA2MDIiLCJhdXRoX3RpbWUiOjE2MDk5NDEyNDQsImlkcCI6ImxvY2FsIiwiaWQiOiI5YjRkY2UwMy1mMmIzLTExZTgtOGVjNy0wMjQyYWMxMjA2MDIiLCJuYW1lIjoibHRlc3QwMSIsIm5pY2tuYW1lIjoi6ZmI5rW35rabIiwicm9sZV9jb2RlcyI6IldPLlVTRVIsVHQtTGlsbHktQ29uZmVyZW5jZUxlYWRlcixUdC1MaWxseS1lUDJQLUNvbmZlcmVuY2VMZWFkZXIsVHQtTGlsbHktU01SZXBvcnQsU21hcnRYLlZlbnVlLk9QLFR0LUxpbGx5LUZvdW5kZXIsVHQtTGlsbHktQWRtaW4sVHQtTGlsbHktUmVwb3J0LEVYLkFsaXBheSxUdC1MaWxseS1GaW5hbmNlLEF0dGVuZGVyLFR0LUxpbGx5LU1lZGl1bU1pY2VDb25mZXJlbmNlTGVhZGVyLFR0LUxpbGx5LUJ1c2luZXNzLUNvbmZlcmVuY2VMZWFkZXIsVHQtTGlsbHktUk1ULFR0LUxpbGx5LVJlc01nciIsInRlbmFudF9pZCI6ImYwNGI0NWE5LWU3ZjgtMTFlOC1hZDJhLTAyNDJhYzE0MTkwNyIsInRlbmFudF9jb2RlIjoibGlsbHkiLCJ2ZXJzaW9uIjoiNjgiLCJzY29wZSI6WyJBcGlzLkFkbWluIiwiQXBpcy5DaGVja0FjY291bnQiLCJBcGlzLkNvbmZpZ3VyYXRpb24iLCJBcGlzLkV2ZW50IiwiQXBpcy5GaWxlIiwiQXBpcy5GbG93IiwiQXBpcy5Gb3VuZGF0aW9uIiwiQXBpcy5JZGVudGl0eSIsIkFwaXMuSW52b2ljZSIsIkFwaXMuTWVhbCIsIkFwaXMuTWVzc2FnZSIsIkFwaXMuTXlQcm9maWxlIiwiQXBpcy5TaG9wS2VlcGVyIiwiQXBpcy5TbWFydEFsaXBheSIsIkFwaXMuU21hcnRFdmVudCIsIkFwaXMuU21hcnRKb2IuRmluIiwiQXBpcy5WZW51ZSIsImVjLm9yZGVyIiwicGFzc3BvcnQiLCJyZXMudmVudWUiLCJzbWFydHhhcHAiLCJ3b3JrZmxvdyIsIm9mZmxpbmVfYWNjZXNzIl0sImFtciI6WyJjdXN0b20iXX0.gu11HZwkaEoDzrvofrzCKP0nIiYvAkFpymscE7FZzsyh2CP45j9lRUJrzON0bEE_Z7YLfrx2M8-9PtonEtj7afBx0RiuDCf5Q6hQZDt8dpwm1kkmFrMqrvjbdmB7uaxRyA8ZTmLCsFl2-xMq5MV7-0PXISQ8XUnS76tOmpsD8URddpq4NNtZbTB1VPqqwICXCWi7-Etz7SObiJKzkVIQeizJC5sDDxbq-cISPweutZi2AIyQvCUGUI1hRqcUsHyZNdn1-3eZDMLHuMM1pij3z0UsCdCt16EjG7S7nzTQpTYKsJ0U2yy_ribU4io47ZmvFXrmdqDAUA4tKGk3e55Hug'
    }
    res = request.send_request('post',url,headers,payload)
    print(res.text)


...

if __name__ == '__main__':

    apirequest_post2()
    pass
