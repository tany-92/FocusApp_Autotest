'''import os
from common.readConfig import Readconfig
from common.logs import Log
conf = Readconfig()

values = os.popen('adb shell getprop ro.build.version.release').read()
print(values)
platformName = conf.getAppValue('platformName')
print(platformName)
appPackage = conf.getAppValue('appPackage')
print(appPackage)
appActivity = conf.getAppValue('appActivity')
print(appActivity)'''

# coding=utf-8

from appium import webdriver
import time

from common.baseOperate import BaseOperate, log

desired_caps = {}
desired_caps['deviceName'] = 'ea29b52f'
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['appPackage'] = 'com.sohu.focus.live'
desired_caps['appActivity'] = '.main.MainActivity'
desired_caps['automationName'] = 'uiautomator2'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
# desired_caps['noReset'] = True
driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)
time.sleep(2)

driver.find_element_by_id('com.android.permissioncontroller:id/permission_allow_button').click()
time.sleep(5)
driver.find_element_by_id('com.sohu.focus.live:id/privacy_negative').click()
time.sleep(2)
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.TabWidget/android.widget.RelativeLayout[4]/android.widget.RelativeLayout/android.widget.ImageView').click()
time.sleep(2)
driver.find_element_by_id('com.sohu.focus.live:id/personal_information_layout').click()
time.sleep(2)
driver.find_element_by_id('com.sohu.focus.live:id/login_to_account_auth').click()
time.sleep(2)
driver.find_element_by_id('com.sohu.focus.live:id/login_account_phone_num').send_keys('13001232861')
time.sleep(5)
txt = '密码'
#driver.find_element_by_android_uiautomator('new UiSelector().text("%s")' % txt).send_keys('442182')
BaseOperate(driver).get_txt(txt).send_keys('442182')
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.CheckBox').click()
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TextView[2]').click()
time.sleep(5)

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.logs import Log
import os
import time





driver.quit()







