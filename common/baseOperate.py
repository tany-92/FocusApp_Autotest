# coding=utf-8

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.logs import Log
import os
import time
from appium import webdriver
from common.readYaml import Readyaml

log = Log()


class BaseOperate:

    """
        基础操作：返回、上下左右滑动屏幕、截图、获取element信息
    """

    def __init__(self, driver):
        self.driver = driver

    def back(self):

        """
            Android 点击物理返回键
        """
        os.popen("adb shell input keyevent 4")

    def get_window_size(self):

        """
            获取屏幕大小
        """

        global windowSize
        windowSize = WebDriverWait(self.driver, 10).until(lambda x: x.get_window_size())
        self.driver.implicitly_wait(2)
        return windowSize

    def swipe_up(self):

        """
            向上滑动屏幕
        """

        windowsSize = self.get_window_size()
        width = windowsSize.get("width")
        height = windowsSize.get("height")
        self.driver.swipe(width/2, height*3/4, width/2, height/4, 1000)

    def swipe_down(self):

        """
            向下滑动屏幕
        """

        windowsSize = self.get_window_size()
        width = windowsSize.get("width")
        height = windowsSize.get("height")
        self.driver.swipe(width/2, height/4, width/2, height*3/4, 1000)

    def swipe_left(self):

        """
            向左滑动屏幕
        """

        windowsSize = self.get_window_size()
        width = windowsSize.get("width")
        height = windowsSize.get("height")
        self.driver.swipe(width*3/4, height/2, width/20, height/2, 1000)

    def swipe_right(self):

        """
            向右滑动屏幕
        """

        windowsSize = self.get_window_size()
        width = windowsSize.get("width")
        height = windowsSize.get("height")
        self.driver.swipe(width/20, height/2, width*3/4, height/2, 1000)

    def screenshot(self):

        """
            截图，并将图片保存到指定目录下，用时间命名
        """

        now = time.strftime("%Y%m%d.%H.%M.%S")
        self.driver.get_screenshot_as_file('D:\\study\\App-Test\\screenshot' + now + '.png')
        # self.driver.get_screenshot_as_file('/Users/xintudoutest/github/Appium/screenshot/' + now + '.png')
        print('screenshot:', now, '.png')

    def get_name(self, name):

        """
            定位页面text元素，param：name
        """

        findname = "//*[@text='%s']"%(name)
        try:
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath(findname).is_displayed())
            element = self.driver.find_element_by_xpath(findname)
            # element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(findname))
            # self.driver.implicitly_wait(2)
            return element
        except:
            log.error('未定位到元素：'+'%s'%(name))
            self.screenshot()

    def get_id(self, id):

        """
            定位页面resouce id元素，param：id
        """

        try:
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_id(id).is_displayed())
            element = self.driver.find_element_by_id(id)
            # element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id(id))
            # self.driver.implicitly_wait(2)
            return element
        except:
            log.error('未定位到元素：'+'%s'%(id))
            self.screenshot()

    def get_xpath(self, xpath):

        """
            定位页面xpath元素，param：xpath
        """

        try:
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_xpath(xpath).is_displayed())
            element = self.driver.find_element_by_xpath(xpath)
            # element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(xpath))
            # self.driver.implicitly_wait(2)
            return element
        except:
            log.error('未定位到元素：'+'%s'%(xpath))
            self.screenshot()

    def get_ids(self, id):

        """
            定位页面resouce id元素组，param：id，return：元素列表
        """

        try:
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_elements_by_id(id).is_displayed())
            elements = self.driver.find_elements_by_id(id)
            # elements = WebDriverWait(self.driver, 10).until(lambda x: x.find_elements_by_id(id))
            # self.driver.implicitly_wait(2)
            return elements
        except:
            log.error('未定位到元素：'+'%s'%(id))
            self.screenshot()

    def get_toast(self, toast):

        """
            查找页面toast元素，param：toast
        """

        try:
            message = '//*[contains(@text,\'{}\')]'.format(toast)
            element = WebDriverWait(self.driver, 5, 0.5).until(
                EC.presence_of_element_located((By.XPATH, message)))
            log.info('查找到toast：'+'%s'%(element.text))
        except:
            log.error('未查找到toast：'+'%s'%(toast))
            self.screenshot()

    def get_class(self, name):

        """
            查找页面class元素，param：name
        """

        try:
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_elements_by_class_name(name).is_displayed())
            elements = self.driver.find_elements_by_class_name(name)
            return elements
        except:
            log.error('未定位到class元素：'+'%s' % (name))
            self.screenshot()



    def backpage(self, name):

        """
            返回到指定页面，不兼容Android7.0系统
        """

        i = 0
        while i < 10:
            i = i + 1
            try:
                findname = "//*[@text='%s']" % (name)
                self.driver.find_element_by_xpath(findname)
                self.driver.implicitly_wait(2)
                break
            except:
                os.popen("adb shell input keyevent 4")
                try:
                    findname = "//*[@text='订单']"
                    self.driver.find_element_by_xpath(findname).click()
                    self.driver.implicitly_wait(2)
                except:
                    os.popen("adb shell input keyevent 4")


    def get_text(self, text):
        """
            查找页面text元素，param：text
        """
        try:
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_element_by_android_uiautomator('new UiSelector().text("%s")' % text).is_displayed())
            elements = self.driver.find_element_by_android_uiautomator('new UiSelector().text("%s")' % text)
            return elements
        except:
            log.error('未定位到text元素：' + '%s' % (text))
            self.screenshot()

