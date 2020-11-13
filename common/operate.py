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

    def back_home(self):

        """
            返回指定页面
        """

        self.baseoperate.backpage(u'订单')

if __name__ == '__main__':
    path = 'D:/study/App-Test/testyaml/login/01_EmailLogin.yaml'
    desired_caps = {}
    desired_caps['deviceName'] = '66J5T18A24032566'
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '10'
    desired_caps['appPackage'] = 'com.sohu.focus.live'
    desired_caps['appActivity'] = '.main.MainActivity'
    desired_caps['automationName'] = 'uiautomator2'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # desired_caps['noReset'] = True
    driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)

    operate = Operate(path,driver)
    operate.check_operate_type()



