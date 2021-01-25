#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Author  :   {Mingxing}
@License :   (C) Copyright 2020-2021, {Everything }
@Contact :   381493362@qq.com
@Software:   PyCharm
@File    :   loggs.py
@Time    :   2021/1/17 20:15
@Desc    :
'''

import logging
from logging import config
import logging.config

# class Mylog(object):
#
#     def __init__(self):
#         config.fileConfig('logger.ini')
#         self.logger = logging.getLogger('example01')
#
#     @property
#     def my_logger(self):
#
#         return self.logger
logging.config.fileConfig('logger.ini')  # 加载配置
logger = logging.getLogger('test')  # 创建logger


...

if __name__ == '__main__':
    # log = Mylog()
    # log.my_logger.info('it is my test log message info')
    logger.info('普通消息')
    logger.debug('调试消息')
    logger.warning('警告消息')
    logger.error('错误消息')
    pass
