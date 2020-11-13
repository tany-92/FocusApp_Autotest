# coding=utf-8

import time
from appium import webdriver
from selenium.common.exceptions import WebDriverException
from common.readConfig import Readconfig
from common.getDevices import Devices
from common.logs import Log


log = Log()
conf = Readconfig()
cmd = Devices()


deviceName = cmd.get_device_name()
platformVersion = cmd.get_platform_version()
platformName = conf.getAppValue('platformName')
appPackage = conf.getAppValue('appPackage')
appActivity = conf.getAppValue('appActivity')


desired_caps = {}
desired_caps['deviceName'] = '%s' % deviceName
desired_caps['platformName'] = '%s' % platformName
desired_caps['platformVersion'] = '%s' % platformVersion
desired_caps['appPackage'] = '%s' % appPackage
desired_caps['appActivity'] = '%s' % appActivity
desired_caps['automationName'] = 'uiautomator2'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
# desired_caps['noReset'] = True  #注释之后，每次启动都会自动清除数据

try:
    driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)
    time.sleep(5)
    log.info('获取driver成功')
except WebDriverException:
    log.warn('获取driver失败')



