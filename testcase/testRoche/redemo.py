#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/3 21:33
# @Author  : name
# @File    : redemo.py


import re


# match = re.match('匹配','匹配到后,会返回一个Match对象,里面有个span方法,可以返回 匹配字符在 被匹配字符 的开始和结束索引')

# print(match)

# print(re.match('返回','匹配到后,会返回一个Match对象'))
# print(re.match('b','bcBAC'))

# string = '匹配到后,会返回一个Match对象,里面有个span方法,可以返回 匹配字符在 被匹配字符 的开始和结束索'
#
# match = re.search(r'会(.*)对象 ',string,re.M|re.S)
# print(match)
#
# line = 'Cats are smarter than dogs'
# matchObj = re.match(r'(.*)are (.*?) .*',line,re.M|re.I)
# if matchObj:
#     print('matchobj.group():',matchObj.group())
#     print('matchobj.group(1):',matchObj.group(1))
#     print('matchobj.group(2):',matchObj.group(2))
# else:
#     print('no match')
#
# searchObj = re.search(r'(.*) are (.*?) .*',line,re.M|re.I)
# if searchObj:
#     print('searchObj.group():',searchObj.group())
#     print('searchObj.group(1):',searchObj.group(1))
#     print('searchObj.group(2)',searchObj.group(2))
# else:
#     print('no search')
'''
match 和 search 方法的区别
使用search方法匹配下面文本中的 公司名,验证码,分钟数 三个匹配项,并打印出来
【果芽科技】您的验证码是8604，请于10分钟内使用，为保障您的账户安全，请勿将此验证短信转发给他人。
'''
# leng = '【果芽科技】您的验证码是8604，请于10分钟内使用，为保障您的账户安全，请勿将此验证短信转发给他人。'
# matchObj = re.match(r'【(.*)】.*是(.*)，请于(.*?)分钟内使用',leng,re.M|re.I)
# if matchObj:
#     print(matchObj.group())
#     print(matchObj.group(1))
#     print(matchObj.group(2))
#     print(matchObj.group(3))
# else:
#     print('no match')
#
# searchObj = re.search(r'【(.*)】.*是(.*)，请于(.*?)分钟内使用',leng,re.M|re.I)
# if searchObj:
#     print(searchObj.group())
#     print(searchObj.group(1))
#     print(searchObj.group(2))
#     print(searchObj.group(3))
# else:
#     print('nothing to do !!!')
phone = '2004-959-559 # 这是一个国外电话号码'
# 删除注释
numb = re.sub(r'#.*$','',phone)
# 移出非数字内容
numb1 = re.sub(r'\D','',phone)
# 替换原有字段
msg = '【果芽科技】您的验证码是8604，请于10分钟内使用，为保障您的账户安全，请勿将此验证短信转发给他人。'
msg1 = re.sub(r'【.*】','【二蛋】',msg)
msg2 = re.sub(r'是.*，','是10086',msg)
msg3 = re.sub(r'\d*分','30分',msg)

# 将 zhangsan@qq.com 中的qq 换为163
email = 'zhangsan@qq.com'
email1 = re.sub(r'@\w.','@163',email)
# compile 函数
pattern = re.compile(r'([a-z]+) ([a-z]+)',re.I)
m = pattern.match('Hello World wide Wed')


...

if __name__ == '__main__':
    print(m)
    print(m.group(1))
    print(m.span(0))
    print(m.groups())
    pass



