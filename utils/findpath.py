#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Author  :   {MX}
@Contact :   {381493362}
@Software:   PyCharm
@File    :   findpath.py
@Time    :   2020/7/9 22:11
@Desc    :
'''
import os
# 获取根目录地址
BASE_PASH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]

def dir_path(file=None,filename=None,pathName=None):
    '''
    查询文件路径
    :param file:根目录文件名
    :param filename:文件夹名
    :param pathName:文件名称
    :return:文件绝对路径
    '''
    if filename:
        path = os.path.join(BASE_PASH,file,filename,pathName)
    else:
        path = os.path.join(BASE_PASH,file,pathName)
    return path


...

if __name__ == '__main__':
    a = dir_path(file='utils', pathName='bad_log.py')
    print(a)
    #print(dir_path('testcase','testRoche','login.json'))
    #print(dir_path(file="common",pathName='MySQL'))

    pass