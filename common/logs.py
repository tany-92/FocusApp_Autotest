# coding=utf-8

import os
import time
import logging

"""
    使用相对路径+绝对路径
"""

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
log_path = PATH("D:\study\App-Test\log")
# log_path = PATH('/Users/xintudoutest/github/Appium/log/')


class Log:

    def __init__(self):

        """
            设置log文件名称和日志输出格式
        """

        filename = 'tanyang'+''.join(time.strftime('%Y%m%d'))+''.join('.log')
        self.logname = os.path.join(log_path, filename)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('[%(asctime)s] - [%(levelname)s] - %(message)s')

    def output(self, level, message):

        """
            打印log信息，level：日志等级，message：日志需要打印的信息
        """

        # send logging output to a disk file
        fh = logging.FileHandler(self.logname, 'a')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # send logging output to streams
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level =='debug':
            self.logger.debug(message)
        elif level =='warn':
            self.logger.warning(message)
        elif level =='error':
            self.logger.error(message)

        self.logger.removeHandler(fh)  # 防止重复打印
        self.logger.removeHandler(ch)

        fh.close()

    def info(self, message):
        self.output('info', message)

    def debug(self, message):
        self.output('debug', message)

    def warn(self, message):
        self.output('warn', message)

    def error(self, message):
        self.output('error', message)

