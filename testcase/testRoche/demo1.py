#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/11 21:51
# @Author  : Mx.
# @File    : demo1.py
import os


def fun1():
    try:
        a = 1/0
    except:
        print('错误的运算.')
def fun2():
    try:
        num = 5/2
    except:
        print('test')
    else:
        print('test_demo')
def fun3():
    try:
        num = 5/2
    except:
        print('cuo wu')
    else:
        print('错误了,就走这里')
    finally:
        print('管你错不错,都来.')
def fun4():
    try:
        a = int(input('请输入您想的数字:\t'))
        b = int(input('请输入您想的一个数字:\t'))
        c = a/b
        print('您输入的两个数相除的结果是%s'%c)
    except ValueError:
        print('这里出现了,值的异常')
    except ArithmeticError:
        print('这里出现运算错误')
    except :
        print('未知错误')
    print('程序正常服务,未发生异常')

def fun5():
    try:
        1/5
    except Exception as e:
        # 访问异常的错误编号和详细信息
        print(e.args)
        print(str(e))
        print(repr(e))

def fun6():
    a = input('请输入2-5位数字:\t')
    if len(a)<2:
        raise ValueError('输入小于2位数')
    elif len(a) >5:
        raise ValueError ('输入大于5位数字')
    else:
        print('输入成功')


...

...
if __name__ == '__main__':
    fun6()
    pass