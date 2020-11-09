#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Author  :   {MX}
@Contact :   {381493362}
@Software:   PyCharm
@File    :   bad_log.py
@Time    :   2020/7/9 22:42
@Desc    :
'''
import os,logging,datetime
import glob
import platform
from logging.handlers import TimedRotatingFileHandler
from utils.findpath import BASE_PASH


class Logger:
    def __init__(self,logger_name='framework'):
        self.log_path =os.path.join(BASE_PASH,'Logs')
        if not os.path.exists(self.log_path):os.makedirs(self.log_path)
        self.logger =logging.getLogger(logger_name)
        logging.root.setLevel(logging.INFO)
        if platform.system() == 'Windows':
            # win 日志路径
            self.log_path = os.path.join(os.path.dirname(os.path.dirname(__file__),),'Logs')
        else:
            # 服务器日志
            self.log_path = 'home/Logs'
        self.log_path_name = 'test.log'
        self.backup_count = 5 # 保留日志数量
        # 日志级别
        self.console_output_level = 'INFO'
        self.file_output_level = 'INFO'
        # 日志格式pattern
        pattern = '%(asctime)s - %(filename)s - [Lien:%(lineno)d] - %(levelname)s - %(message)s'
        self.formatter = logging.Formatter(pattern)

    def get_logger(self):
        '''在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回
        我们这里添加两个句柄，一个输出日志到控制台，另一个输出到日志文件。
        两个句柄的日志级别不同，在配置文件中可设置。'''
        if not logging.logThreads: # 过滤重复日志
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)

            file_handler = TimedRotatingFileHandler(filename=os.path.join(self.log_path,self.log_path_name),
                                                    when='D',
                                                    interval=1,
                                                    backupCount=self.backup_count,
                                                    encoding='utf-8')
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
        return self.logger



log = Logger().get_logger()




if __name__ == '__main__':
    log.info('put')
    pass