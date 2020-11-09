#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/23 19:13
# @Author  : name
# @File    : demo3.py
import time, functools,copy




class Test(object):
    def __init__(self,func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        print('这是一个装饰器:')
        print(args[0])
        print(args[1])
        self.__func(*args,**kwargs)
@Test
def logs(a,b):
    print('你好丫')

class Test1:
    def __init__(self,a,b,c):
        print('___装饰器初始化___')
        self.a = a
        self.b = b
        self.c = c

    def __call__(self,fun):
        print('装饰函数:',self.a,self.b,self.c)
        def info(*args,**kwargs):
            fun(*args,**kwargs)
        return info
@Test1('参数a','参数b','参数c')
def show(name,age,sex):
    print('性别:' + sex + '的' + age + '岁的' + name)
# 将下面闭包函数的装饰器 使用类装饰器 实现一下:
def fun_d(minNum=0,maxNum=100): # arg_a接收装饰器传递过来的参数
    def swap(func):
        def function(*args,**kwargs):
            for i in args:
                if not isinstance(i,int) or i<minNum or i>maxNum:
                    return f'参数:{i},不符合要求'
            res = func(*args,**kwargs)
            return res
        return function
    return swap

@fun_d(minNum=10,maxNum=20)
def fun1(a,b):
    return a+b

@fun_d(minNum=10,maxNum=20)
def fun2(a,b,c):
    return a+b-c


#print(fun1(15,21))
#print(fun1(15,20))

def warp(obj):
    obj.name = '猴子'
    return obj
@warp
class Bar(object):
    def __init__(self):
        pass


def f1(func):
    def fun(*args,**kwargs):
        print('装饰器实现功能')
        print(args)
        return func(*args,**kwargs)
    return fun
@f1
class Hero(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('初始化属性.')

    def moev(self):
        print(f'{self.name}正在快速移动')

a = {1:[1,2,3]}
# b = a
# c = a.copy()
# c[2]='1'
# a[1].append(5)
# d = copy.deepcopy(a)
#
# ...

import copy
d = copy.deepcopy(a)
d[2]='1'
print(a)
print(d)
print('-----')
a[1].append(4)
print(a)
print(d)

if __name__ == '__main__':

    pass



