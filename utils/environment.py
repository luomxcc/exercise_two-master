#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Author  :   {MX}
@Contact :   {381493362}
@Software:   PyCharm
@File    :   environment.py
@Time    :   2020/7/10 21:35
@Desc    :
'''


class EnvWrapper:
    def __init__(self):
        self._module_path = None
        self._log_console = False

    def init_env(self):
        # 环境
        pass

    def get_module_path(self):
        return self._module_path

    def get_log_enable(self):
        return self._log_console


...

if __name__ == '__main__':
    pass
