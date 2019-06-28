# -*- coding:utf-8 -*-
from config import read_config
import unittest

test_dir = r"E:\Demo\demo_python\pomproject\case"

#可以通过测试套件加载测试用例
#test_suit = unittest.TestSuite()
#自动去匹配加载所有test*.py的用例，会比TestSuite更简单
discover = unittest.defaultTestLoader.discover(test_dir, "test*.py")
#print(discover)

#测试用例的集合
#test_suit.addTests(discover)

#调用unittest的TextTestRunner类，运行所有的用例
runner = unittest.TextTestRunner()
#runner.run(test_suit)
runner.run(discover)


"""
smtp_server = read_config.smtp_server
port = read_config.port
sender = read_config.sender
pwd = read_config.pwd
receiver = read_config.receiver
#print(smtp_server, port, sender, pwd, receiver)
#print(type(port))

#send_mail(smtp_server, port, sender, pwd, receiver)
"""