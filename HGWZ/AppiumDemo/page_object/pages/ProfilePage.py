from selenium.webdriver.common.by import By

from HGWZ.AppiumDemo.page_object.pages import BasePage
from HGWZ.AppiumDemo.page_object.pages import LoginPage


class ProfilePage(BasePage):
    def gotologin(self):
        login_btn = (By.ID,"com.xueqiu.android:id/rl_login")
        self.find(login_btn).click()
        return LoginPage()
