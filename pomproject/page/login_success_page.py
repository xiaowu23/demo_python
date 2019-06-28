# -*- coding:utf-8 -*-
from common.base import BasePage
from page.login_page import LoginPage,login_url
from selenium import webdriver

success_url = ""

class LoginSuccessPage(BasePage):
    welcome_loc = ()

    def get_welcome_text(self):
        text = self.get_text(self.welcome_loc)
        return text

if __name__ == "__main__":
    driver = webdriver.Firefox()
    login_driver = LoginPage(driver)
    login_driver.open(login_url)
    login_driver.login()
    result = LoginSuccessPage(driver).get_welcome_text()
    print(result)

