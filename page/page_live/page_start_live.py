# coding=utf-8

import os
from common.operate import Operate
from common.getDriver import driver

PATH = lambda p: os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )
yamlpath = PATH("D:\\study\\FocusApp_Autotest\\testyaml\\live\\01_StartLive.yaml")


class StartLive:

    def __init__(self, driver):
        self.path = yamlpath
        self.driver = driver
        self.operate = Operate(self.path, self.driver)

    def operatepe(self):
        self.operate.check_operate_type()