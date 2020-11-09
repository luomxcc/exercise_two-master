#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/18 23:53
# @Author  : name
# @File    : kinddemo.py
import os
class Car():
    def __init__(self,name,no,speed):
        self.name = name
        self.no = no
        self.speed = speed
    def show(self):
        print(self.name,self.speed,self.no)
    def start(self):
        if self.speed ==100:
            print(self.name+'启动了')
        else:
            print(self.name+'停在这里')
    def run(self):
        print(self.name + '行驶中,车速是:'+self.speed)

    def stop(self):
        if self.speed == 0:
            print(self.name+'当前行使速度为'+self.speed)
        else:
            print('急刹')

class Human(object):
    # __init__ : 类的初始化方法
    # self : 代表类的本身 ,name,age,sex 初始化的时候 要用到的参数
    def __init__(self,name,age,sex):
        # self.name = name : 把方法中的参数 绑定给 类的属性
        self.name = name
        self.age = age
        self.sex = sex

    # 类中的方法 必须包含self 参数
    def eat(self):
        print(self.name+'在吃饭 ')

    def sleep(self):
        print(self.name+'在睡觉')

    # 类中的方法,可以调用其他方法,可以调用属性,除了init 方法
    def info(self):
        print('这个人叫%s,今年%s岁,性别: %s'%(self.name,self.age,self.sex))
        self.eat()

class People:
    name = ''
    age = 0
    __weigth = 0
    def __init__(self,a,n,w):
        self.name = n
        self.age = a
        self.__weigth = w
    def speak(self):
        print('%s说:我%s岁,'%(self.name,self.age))
        print(f'__weith:{self.__weigth}')
    def __info(self):
        print('调用私有方法')

class Tester(Human):
    def __init__(self,name,age,sex,job):
        super().__init__(name,age,sex)
        self.job = job
    def do_test(self):
        print(self.name +'在测试出代码')
        self.sleep()
class Dev:
    def __init__(self,name,language):
        self.name = name
        self.language = language
    def do_dev(self):
        print(f'{self.name}开发游戏,擅长使用{self.language}语言编写游戏代码')
class SDET(Tester,Dev):
    def __init__(self,name,age,sex,job,language):
        Tester.__init__(self,name,age,sex,job)
        Dev.__init__(self,name,language)

    def do_work(self):
        print(f'{self.name}都是用{self.language}语言写接口')
    def do_test(self):
        print('{}擅长使用自动化测试'.format(self.name))
    def do_dev(self):
        print('%s做的工作是,使用%s脚本语言编写代码'% (self.name,self.language) )



def do_t(obj):
    obj.dest()
# 原始方案
def filter1(l):
    return list(filter(lambda x: x%2==0,l)) # 定义一个过滤出列表中偶数的方法



...

if __name__ == '__main__':
    test = Tester('黄蜂', '22','食屎啦','铲屎的')
    s = SDET('小明','22','不男不女','小小开发','php')
    super(SDET,s).do_test()
    do_t(test)

    pass



