#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/3 16:54
# @Author  : Mx.
# @File    : testexcel.py
import xdrlib,xlwt,xlrd,sys,os



class Redact_excel(object):
    def __init__(self):
        pass
    def open_excel(self,files=None):
        try:
            self.data = xlrd.open_workbook(files)
            return self.data
        except Exception as e:
            print(str(e))

    def excel_table_byname(self,file=None,colnameindex=0,by_name=u'sheet1'):
        '''
        根据名称获取Excel表格中的数据, 数据;file
        :param file:Excel表格路径,
        :param colnameindex:表头名称
        :param by_name:sheet页
        :return:
        '''
        # 打开Excel文件
        self.data = self.open_excel(file)
        # 根据sheet名字来获取Excel中的sheet
        self.table = self.data.sheet_by_name(by_name)
        # 行数
        self.nrows = self.table.nrows
        # 某一行数据
        self.colnames = self.table.row_values(colnameindex)
        # 读取结果的序列
        list = []
        # 遍历每一行内容
        for rownum in range(0,self.nrows):
            # 根据行号获取行
            self.row = self.table.row_values(rownum)
            # 如果行存在
            if self.row:
                app = [] # 行的内容
                for i in range(len(self.colnames)):
                    app.append(self.row[i])
                list.append(app)
        return list







...

...
if __name__ == '__main__':
    redact = Redact_excel()
    redact.open_excel()
    pass