# coding=utf-8

import unittest
from page.page_login.page_PhoneLogin import EmailLogin
from page.page_live.page_start_live import StartLive
from page.page_live.page_close_live import CloseLive
from common.getDriver import driver
import time
from common.sendEmail import Email


class LoginTest(unittest.TestCase):


    def test_01(self):
        """手机账号登录"""
        em = EmailLogin(driver)
        em.operatepe()


    def test_02(self):
        """发起直播"""
        st = StartLive(driver)
        st.operatepe()



    def test_03(self):
        "直播20s后，关闭直播并返回到直播列表页"
        time.sleep(20)
        cl = CloseLive(driver)
        cl.operatepe()


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(LoginTest('test_01'))
    suite.addTest(LoginTest('test_02'))
    suite.addTest(LoginTest('test_03'))
    unittest.TextTestRunner(verbosity=1).run(suite)
    Email.send_mail()
