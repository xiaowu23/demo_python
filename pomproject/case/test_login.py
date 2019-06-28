# -*- coding:utf-8 -*-
from selenium import webdriver
from page.login_page import LoginPage,login_url
import unittest
import time

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.login_driver = LoginPage(self.driver)
        self.login_driver.open(login_url)

    #登录模块用例
    def test_01(self):
        # 第1步：输入用户名
        self.login_driver.input_username("xxxx")
        # 第2步：输入密码
        self.login_driver.input_psw("xxxx")
        # 第3步：点击登录按钮
        self.login_driver.click_login_button()
        time.sleep(3)
        # 第4步：获取返回结果
        t = self.login_driver.get_tip()
        print(t)
        # 第5步：判断结果跟预期是否一致
        self.assertIn(u"请输入验证码",t)

    def tearDown(self):
        self.driver.quit()
