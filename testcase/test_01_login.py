# coding=utf-8

import unittest
from page.page_login.page_PhoneLogin import PhoneLogin
from page.page_login.page_PasswordError import PasswordError
from page.page_login.page_UnLogin import UnLogin
from page.page_login.page_Back import Back
from page.page_login.page_PhoneUnexist import PhoneUnexist

from common.getDriver import driver


class LoginTest(unittest.TestCase):
    """登录"""

    #@unittest.skip
    def test_01(self):
        """账号密码登录"""
        lo = PhoneLogin(driver)
        lo.operatepe()

    def test_02(self):
        "退出登录"
        un = UnLogin(driver)
        un.operatepe()

    def test_03(self):
        "账号密码登录时密码错误 "
        pa = PasswordError(driver)
        pa.operatepe()

    def test_04(self):
        "返回到“手机号验证码登录”页面"
        ba = Back(driver)
        ba.operatepe()

    def test_05(self):
        "返回到“我的”页面"
        ba = Back(driver)
        ba.operatepe()

    def test_06(self):
        "账号密码登录时账号不存在"
        ph = PhoneUnexist(driver)
        ph.operatepe()




if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(LoginTest('test_01'))
    suite.addTest(LoginTest('test_02'))
    suite.addTest(LoginTest('test_03'))
    suite.addTest(LoginTest('test_04'))
    suite.addTest(LoginTest('test_05'))
    suite.addTest(LoginTest('test_06'))
    unittest.TextTestRunner(verbosity=1).run(suite)
