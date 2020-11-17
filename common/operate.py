# coding=utf-8

from common.readYaml import Readyaml
from common.baseOperate import BaseOperate
from appium import webdriver


class Operate:

    def __init__(self, path, driver):
        self.path = path
        self.driver = driver
        self.yaml = Readyaml(self.path)
        self.baseoperate = BaseOperate(driver)

    def check_operate_type(self):

        """
            # 读取yaml的信息并执行
            # element_info：定位元素的信息
            # find_type：定位元素的类型 id、xpath、text、ids
            # operate_type: 要执行的操作 click、send_keys、back、swipe_up、swipe_down、assert
            # send_content：执行send_keys时，要输入的内容
            # index：ids时用到，元素组的第几位
            # times: swipe和back的次数
        """

        for i in range(self.yaml.caselen()):

            if self.yaml.get_operate_type(i) == 'click':
                self.driver.implicitly_wait(3)
                if self.yaml.get_findtype(i) == 'text':
                    self.baseoperate.get_text(self.yaml.get_elementinfo(i)).click()

                #if self.yaml.get_findtype(i) == 'text':
                #   self.baseoperate.get_name(self.yaml.get_elementinfo(i)).click()
                elif self.yaml.get_findtype(i) == 'id':
                    self.baseoperate.get_id(self.yaml.get_elementinfo(i)).click()
                elif self.yaml.get_findtype(i) == 'xpath':
                    self.baseoperate.get_xpath(self.yaml.get_elementinfo(i)).click()
                elif self.yaml.get_findtype(i) == 'ids':
                    self.baseoperate.get_ids(self.yaml.get_elementinfo(i))[self.yaml.get_index(i)].click()
                elif self.yaml.get_findtype(i) == 'class':
                    self.baseoperate.get_class(self.yaml.get_elementinfo(i))[self.yaml.get_index(i)].click()


            elif self.yaml.get_operate_type(i) == 'send_keys':
                self.driver.implicitly_wait(3)
                if self.yaml.get_findtype(i) == 'text':
                    self.baseoperate.get_text(self.yaml.get_elementinfo(i)).send_keys(self.yaml.get_send_content(i))
                #if self.yaml.get_findtype(i) == 'text':
                 #   self.baseoperate.get_name(self.yaml.get_elementinfo(i)).send_keys(self.yaml.get_send_content(i))
                elif self.yaml.get_findtype(i) == 'id':
                    self.baseoperate.get_id(self.yaml.get_elementinfo(i)).send_keys(self.yaml.get_send_content(i))
                elif self.yaml.get_findtype(i) == 'xpath':
                    self.baseoperate.get_xpath(self.yaml.get_elementinfo(i)).send_keys(self.yaml.get_send_content(i))
                elif self.yaml.get_findtype(i) == 'ids':
                    self.baseoperate.get_ids(self.yaml.get_elementinfo(i))[self.yaml.get_index(i)].send_keys(self.yaml.get_send_content(i))



            elif self.yaml.get_operate_type(i) == 'assert':

                if self.yaml.get_findtype(i) == 'text':
                    self.baseoperate.get_text(self.yaml.get_elementinfo(i))
                #if self.yaml.get_findtype(i) == 'text':
                 #   self.baseoperate.get_name(self.yaml.get_elementinfo(i))
                elif self.yaml.get_findtype(i) == 'toast':
                    self.baseoperate.get_toast(self.yaml.get_elementinfo(i))

            elif self.yaml.get_operate_type(i) == 'back':
                for n in range(self.yaml.get_backtimes(i)):
                    self.baseoperate.back()

            elif self.yaml.get_operate_type(i) == 'swipe_up':
                for n in range(self.yaml.get_backtimes(i)):
                    self.baseoperate.swipe_up()

            elif self.yaml.get_operate_type(i) == 'swipe_down':
                for n in range(self.yaml.get_backtimes(i)):
                    self.baseoperate.swipe_down()
            elif self.yaml.get_operate_type(i) == 'swipe_left':
                for n in range(self.yaml.get_backtimes(i)):
                    self.baseoperate.swipe_left()
            elif self.yaml.get_operate_type(i) == 'swipe_right':
                for n in range(self.yaml.get_backtimes(i)):
                    self.baseoperate.swipe_right()
            #判断是否是键盘键入
            #elif self.yaml.get_operate_type(i) == 'keyevent':
             #   self.baseoperate.get_keyevent(self.yaml.get_send_content(i))


    def back_home(self):

        """
            返回指定页面
        """

        self.baseoperate.backpage(u'订单')

