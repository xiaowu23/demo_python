# -*- coding:utf-8 -*-
from selenium import webdriver
from page.login_page import LoginPage,login_url
from page.login_success_page import LoginSuccessPage
import unittest
import time

#第一组数据，登录成功
data1 = {"user":"xxx","pwd":"xxx","excpet":True}

#第二组数据，登录失败
data2 = {"user": "xxx","pwd": "xxx","excpet": False}

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.login_driver = LoginPage(self.driver)
        self.login_driver.open(login_url)
        self.success_driver = LoginSuccessPage(self.driver)

    #登录成功的判断方法
    def is_login_success(self, username):
        try:
           result = self.success_driver.get_welcome_text()
           print("登录成功，获取返回结果：%s"%result)
           if username in result:
               return True
           else:
               return False
        except:
            print("登录失败，返回结果为空")
            return False

    def login_case(self, username, pwd, exp):
        # 第1步：调用登录
        self.login_driver.login(user=username, pwd=pwd)
        # 第2步：获取登录成功页欢迎语
        text = self.is_login_success(username)
        print(text)
        return text
        # 第3步：断言
        self.assertEqual(text, exp)

    #登录成功的用例
    def test_01(self):
        self.login_case(data1["user"], data1["pwd"], data1["excpet"])

    #登录失败的用例
    def test_02(self):
        self.login_case(data2["user"], data2["pwd"], data2["excpet"])

    def tearDown(self):
        self.driver.quit()
