# -*- condig:utf-8 -*-

from common.base import BasePage
from selenium import webdriver
import time

#百度糯米
login_url = "https://www.nuomi.com/pclogin/main/loginpage"

class LoginPage(BasePage):
    #登录账号
    user_loc = ("id","TANGRAM__PSP_4__userName")
    #登录密码
    pwd_loc = ("id","TANGRAM__PSP_4__password")
    #登录按钮
    button_loc = ("id","TANGRAM__PSP_4__submit")
    #获取错误提示信息
    tip_loc = ("id","TANGRAM__PSP_4__error")
    #登录遇到问题
    forget_pwd_loc = ("id","pass-fgtpwd")
    #下次自动登录
    low_login_loc = ("id","TANGRAM__PSP_4__memberPassLabel")

    #输入QQ号
    def input_username(self, text):
        self.send_keys(self.user_loc, text)

    #输入密码
    def input_pwd(self, text):
        self.send_keys(self.pwd_loc, text)

    #点击登录按钮
    def click_login_button(self,):
        self.click(self.button_loc)

    #获取错误提示信息
    def get_tip(self):
        text = self.get_text(self.tip_loc)
        return text

    #点击忘了密码
    def click_forget_user(self):
        self.click(self.forget_pwd_loc)

    #点击下次自动登录
    def click_forget_psw(self):
        self.click(self.low_login_loc)

    #封装登录功能
    def login(self, user=u"13246798759", pwd=u"xiaowu@251314"):
        self.input_username(user)
        self.input_pwd(pwd)
        self.click_login_button()

if __name__ == "__main__":
    driver = webdriver.Firefox()
    login_driver = LoginPage(driver)
    login_driver.open(login_url)
    login_driver.input_username("xxxx")
    login_driver.input_pwd("xxxx")
    login_driver.click_login_button()
    t = login_driver.get_tip()
    print(t)
    driver.quit()