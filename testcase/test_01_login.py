# coding=utf-8

import unittest
from page.page_login.page_EmailLogin import EmailLogin

from common.getDriver import driver


class LoginTest(unittest.TestCase):
    """登录"""

    def test_01(self):
        """手机账号登录"""
        em = EmailLogin(driver)
        em.operatepe()


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(LoginTest('test_01'))
    unittest.TextTestRunner(verbosity=1).run(suite)
