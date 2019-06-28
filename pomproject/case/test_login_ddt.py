# -*- coding:utf-8 -*-
from selenium import webdriver
from page.login_page import LoginPage,login_url
from page.login_success_page import LoginSuccessPage
import unittest
import ddt
from common.excel_util import ExcelUtil

#测试数据，登录成功
"""
data = [{"user":"xxx","pwd":"xxx","excpet":True},
        {"user": "xxx","pwd": "xxx","excpet": False}]
"""

#使用读取excel方法获取测试数据
filePath = r"E:\Demo\demo_python\pomproject\common\testdata.xlsx"
sheetName = "登录"
data = ExcelUtil(filePath, sheetName)
data = data.dict_data()
#print (data)

@ddt.ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.login_driver = LoginPage(cls.driver)
        cls.success_driver = LoginSuccessPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        #输入地址
        self.login_driver.open(login_url)

    def tearDown(self):
        #清空所有的cookie
        self.driver.delete_all_cookies()
        #刷新
        self.driver.refresh()

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
        if exp == "True":
            exp = True
        elif exp == "False":
            exp = False
        # 第3步：断言
        self.assertEqual(text, exp)

    #登录成功的用例
    @ddt.data(*data)
    def test_01(self,data1):
        print(data1)
        self.login_case(data1["user"], data1["pwd"], data1["excpet"])

if __file__ == "__main__":
    unittest.main()