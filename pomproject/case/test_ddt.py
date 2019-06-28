# -*- coding:utf-8 -*-
import ddt
import unittest

#测试数据
data = [{"user":"xxx","pwd":"xxx","excpet":True},
        {"user": "xxx","pwd": "xxx","excpet": False}]

@ddt.ddt
class Test(unittest.TestCase):
    @ddt.data(*data)
    def test_01(self, data):
        print(data)
        print(data["user"])
        print(data["pwd"])
        print(data["excpet"])

if __name__ == "__main__":
    unittest.main()