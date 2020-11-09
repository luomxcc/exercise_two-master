#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/28 18:03
# @Author  : name
# @File    : demo0s.py
import os,time



'''
print(os.sep)
# 读取系统分隔符 widows \ linux /
print(os.name)
# 查看系统名字 widows nt linux posix
print(os.getenv('path'))
# 读取环境变量
print(os.getcwd())
# 返回当前路径
print(os.listdir())
print(os.listdir('/file'))
# 返回指定目录下的 所有文件名和目录,默认返回当前目录的内容
# 创建目录
os.mkdir('testosdemo')
# 删除一个目录,若目录不存在则无法删除
os.rmdir('testosdemo')
# 生成多层空目录,若目录全部存在,则失败
os.makedirs('./test/te')
# 删除多层空目录,若目录中有文件则删除失败
os.removedirs('test/te')
# 改变当前工作目录
os.chdir('../')
os.mkdir('demoos')

# 重命名文件或目录, test->旧名字, test1->新名字
os.renames('demo0s','demoos')

# 判断目录或文件是否存在
os.path.exists('目录名/文件名')
# 判断是否是文件
os.path.isfile('路径/文件名')
# 判断是否是目录
os.path.isdir('路径/路径名')
# 判断目录或文件是否存在
os.path.exists('目录名/文件名')
# 判断是否是文件
os.path.isfile('路径/文件名')
# 判断是否是目录
os.path.isdir('路径/路径名')

## 返回文件名
path = '/Users/beazley/Data/data.csv'
os.path.basename(path)

## 返回 data.csv
## 返回文件路径
os.path.dirname(path)

## 返回 /Users/beazley/Data/
## 返回文件大小(单位是字节),如果是目录 返回 目录中的所有文件大小的和
getsize = os.path.getsize('../pro')
print(getsize)
## 返回绝对路径
os.path.abspath('../')

## 返回上级目录的绝对路径
## 分隔路径和文件
os.path.split('/root/gy.txt')

## 返回 ('/root', 'gy.txt')
## 连接目录与与文件或者目录,合成一个目录
a = 'dev'
b = 'conf'
c = 'nginx.conf'
join_path = os.path.join(a, b, c)
print(join_path)
# 输出
# dev\conf\nginx.conf
def open_demo():
    # testfile 相对路径 testcase\testRoche\test.text
    file = 'testcase\testRoche\testdemo.text'
    # 'w+' 读写
    a = open('test.text','w+')
    a.write('open and file 用法1')
    print(type(a))
    # 注意在对file类型对象操作结束后,需要调用close方法,关闭文件
    a.close()

def open_demo2():
    # 相对路径 test.text
    # a+ 代表读写模式,写入时不会覆盖 原文档内容,相当于追加内容
    test = open('test.text','a+')
    test.write('open and file 用法2')
    test.close()
'''

'''
使用w+模式打开一个新文件a.log,并写入: 学习使我快乐。然后关闭file对象
再使用a+模式打开a.log,换行并写入：我每天都很快乐
open中 a+ 和 w+ 模式的区别
'''

def open_demo1():
    #a = 'test.text'
    file = open('test.text','w+',encoding='utf-8')
    file.write('学习使我快乐,')
    file.close()
def open_demo3():
    test1 = open('test.text','a+',encoding='utf-8')
    test1.write('\n我每天都很快乐')
    test1.close()
def open_dem04():
    # r 只读模式,不可写入
    test = open('test.text','r',encoding='utf-8')
    # 读取第一行
    readline = test.readline()
    print(readline)
    # 读取第二行
    readline2 = test.readline()
    print(readline2)

def open_demo5():
    test = open('test.text','r',encoding='utf-8')
    readlines = test.readlines()
    print(readlines)
    print(readlines[1])
def open_demo6():
    test = open('test.text','rb')
    readline = test.readline()
    print(readline)

...

if __name__ == '__main__':
    open_demo6()
    pass



