#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/31 15:11
# @Author  : name
# @File    : tiemdemo.py
import time
import calendar
import datetime

# times = time.time()
# print('当前时间:',times)
# localtime = time.localtime(time.time())
# print(localtime.tm_yday)
# print(localtime.tm_mday)
# atime = time.asctime(localtime)
# print(atime)
'''
tm_year: 4位数年份
tm_mon: 1 到 12 (月份)
tm_mday: 1 到 31 (日期)
tm_hour: 0 到 23 (小时)
tm_min: 0 到 59 (分钟)
tm_sec: 0 到 61 (60或61 是闰秒)
tm_wday: 0到6 (0是周一)
tm_yday: 一年中的第几天，1 到 366
tm_isdst: 是否为夏令时，值有：1(夏令时)、0(不是夏令时)、-1(未知)，默认 -1
'''
'''练习课件中的代码
获取当前时间,并转换成 2016/12/21 格式的字符串
将时间 2016/12/21 10:22:56 转换成 时间类型对象
'''
# str_time = time.strftime('%Y-%m-%d %H:%M:%S')
# print(str_time)
# timestring = '2016-12-21 10:22:56'
# btime = time.strptime(timestring, '%Y-%m-%d %H:%M:%S')
# print(btime)
# print(time.mktime(btime))
# #time.strptime() 可以将字符串转换成 时间类型对象,第一个参数为字符串,第二个是字符串的格式模版
# #time.mktime() 可以将时间对象转换为 时间戳
#
#
#
#
# cal = calendar.month(2020,1)
# print('输出2020年1月的日历')
# print(cal)
# # 判断是否闰年 isleap() False \True
# print(calendar.isleap(1897))
# 当前时间
now = datetime.datetime.now()
# 三天前
three_days_ago = now + datetime.timedelta(days= -3)
# 三周以前
three_weeks_ago = now + datetime.timedelta(weeks= -3)
# print(three_days_ago)
# print(three_weeks_ago)
# print(now)
# 三小时以后
three_hour_later = now + datetime.timedelta(hours=3)
# 三天以后
three_days_later = now + datetime.timedelta(days=3)
# print(three_hour_later)
# print(three_days_later)
dd = '2019-03-17 11:00:00'
# dd = time.strftime('%Y-%m-%d %H:%M:%S')
dd = datetime.datetime.strptime(dd,'%Y-%m-%d %H:%M:%S')

# 计算时间差;使用 datetime.datetime.strptime() 转换字符串时间 为 datetime 对象,然后进行相减运算,即可获得 时间差
ff = time.strftime('%Y-%m-%d %H:%M:%S')
ff = datetime.datetime.strptime(ff,'%Y-%m-%d %H:%M:%S')
dev = ff - dd
# print(dev)
'''
计算当前时间五周后的日期
计算当前时间五天前的日期
计算2题和3题 时间相差的天数
'''
five_days_ago = now + datetime.timedelta(days= -5)
five_days_later = now + datetime.timedelta(days=5)

days = five_days_later - five_days_ago

print((five_days_later-five_days_ago).days)
print(days)


...

if __name__ == '__main__':

    pass



