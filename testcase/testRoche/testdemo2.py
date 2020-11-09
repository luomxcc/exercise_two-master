#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/19 21:25
# @Author  : name
# @File    : testdemo2.py
from functools import partial # 导入partial包

# 原始方案
def filter1(l):
    return list(filter(lambda x: x%2==0,l)) # 定义一个过滤出列表中偶数的方法
# print(filter1([1,2,3,4,56,7,8]))
# filter2 =partial(filter,lambda x: x%2==0)
# print(list(filter2([1,2,3,4,5,6,7,8])))

def info(name,age):
    print('姓名:{},年龄:{},外号叫狗剩'.format(name,age))



'''
练习课件中的代码
现有原函数:
def f1(a,b,c):
    return a+b-c
要求为f1 写一个偏函数,固定传入参数c 为10
'''
def f1(a,b,c):
    return a+b-c

def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent
    return exponent_of # 返回值是 exponent_of 函数
'''
   square = nth_power(2) # 计算一个数的平方
    cube = nth_power(3) # 计算一个数的立方
    print(square(2)) # 计算2 的平方
    print(cube(3)) # 计算3 的立方
    print(square.__closure__)
    print(square.__closure__[0].cell_contents)
'''
'''
练习课件中的代码
使用闭包函数写一个装饰器,要求:使用该装饰器的方法会循环执行5次,并且打印出循环次数
'''

def fun_a(func):
    print('原方法返回值:',func)
    return 'hello'

@fun_a
def fun_b():
    return '124'

def fun_s(funq):
    def function():
        fun1 = funq()
        for i in range(funq):
            print('循环次数:',funq,i+1)
            return funq
        return function
@fun_s
def fun_c():
    print('函数fun_c执行的次数:',(2))

def fun_2(fun1):
    def function(arg_b):
        print('函数执行前的操作:')
        res = fun1(arg_b)
        print('函数执行后的操作:')
        return res
    return function
@fun_2
def fun_3(arg_b):
    print(arg_b)



...

if __name__ == '__main__':
    fun_c()
    fun_3('二狗')
    print(fun_3)
    print(fun_c)
    pass



