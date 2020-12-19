# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/7 20:45
# @Author  : name
# @File    : operationexcel.py


import xlrd
import os
import xlutils.copy
import copy


# 金融基础-作业参考.xlsx
# 查找当前电脑文件
class Operation:
    def __init__(self, path, filename):
        self.path = path
        self.filename = filename

    def search(self):
        '''本地电脑查找文件'''
        path_file = []
        for root, dirs, files in os.walk(self.path):  # path为根目录
            if self.filename in dirs or self.filename in files:
                root = str(root)
                re_path = os.path.join(root, self.filename)
                path_file.append(re_path)  # 返回路径包含文件名
        return path_file

    # 读取exelc表格数据
    def read_execl(self):
        # 打开execl文件
        sheet_list = xlrd.open_workbook(self.search()[0])
        print(self.search()[0])
        # 读取execl sheet列表
        sheet_name = sheet_list.sheet_names()
        print('数据表格名:%s' % sheet_name)

        sheet1 = sheet_list.sheets()[0]  # 获取1张sheet表数据
        sheet1_name = sheet1.name  # 获取名称
        sheet1_cols = sheet1.ncols  # 获取列数
        sheet1_nrows = sheet1.nrows  # 获取行数
        # print("sheet_name:{},sheet_cols:{},sheet_nrows:{}".format(sheet_name,sheet1_cols,sheet1_nrows))
        # 会哦部分表格内容


# 再指定位置查找指定文件
def findfile(start, name):
    for relpath, dirs, files in os.walk(start):
        if name in files:
            full_path = os.path.join(start, relpath, name)
            file_path = os.path.normpath(os.path.abspath(full_path))

    return print(file_path)


#
# # 获取文件当前位置
# curPath = os.path.abspath(os.path.dirname(__file__))
# # print(curPath)
# # 获取项目路径
# rootPath = os.path.abspath(os.path.dirname(curPath))
# # 获取文件路径testcase\apitest\test_w.xlsx
# file_Path = r'D:\Cache\04Python_code_apicase\exercise_two-master\testcase\apitest\test_w.xlsx'
# file_path = r'D:\Cache\WeChat\WeChat Files\q381493362\FileStorage\File\\2020-12\\计算机应用基础-作业参考.xlsx'
# filePath = os.path.join(rootPath,file_Path)
# # 打开工作表
# data = xlrd.open_workbook(file_path,encoding_override='utf-8')
# # 获取第一张表
# table = data.sheets()[0]
# # 创建一个data_list 来存放数据e
# data_list = []
# # 讲第一行的数据读取出存放再data_list中
# data_list.extend(table.row_values(0))
# # 打印出第一行的数据
# print(data_list)
# for item in data_list:
#     print(item)
# ...

if __name__ == '__main__':
    # fand = findfile('D:\Softwork','金融基础-作业参考.xlsx')
    read = Operation('D:\Softwork', '金融基础-作业参考.xlsx')
    re = read.read_execl()
    print(re)
    # req = read_execl(re)
    # print(req)

    pass
