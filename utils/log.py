#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Author  :   {MX}
@Contact :   {381493362}
@Software:   PyCharm
@File    :   log.py
@Time    :   2020/7/11 23:08
@Desc    :
'''
import logging,os,time
cur_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(os.path.dirname(cur_path),'Logs')

if not os.path.exists(log_path):os.makedirs(log_path)
print(log_path)

class Logger(object):
    def __init__(self):
        # 文件名
        self.logname = os.path.join(log_path,'%s.log'%time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s] - [%(filename)s] - %(levelname)s:%(message)s')

    def __console(self,level,message):
        # 创建一个fileHangder 用于写入本地文件
        fh = logging.FileHandler(self.logname,'a',encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)
        # 创建一个streamHandler 用于输出控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

        # 过滤重复日志
        self.logger.removeHandler(fh)
        self.logger.removeHandler(ch)
        fh.close()
    def debug(self,message):
        self.__console('debug',message)
    def info(self,message):
        self.__console('info',message)
    def warning(self,message):
        self.__console('warning',message)
    def error(self,message):
        self.__console('error',message)

log = Logger()


if __name__ == '__main__':
    log.error('pei')
    log.info('hello')
    log.debug('ddddd')
    log.warning('警告')

    pass