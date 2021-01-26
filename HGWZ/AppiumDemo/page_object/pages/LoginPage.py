from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from HGWZ.AppiumDemo.page_object.pages import BasePage


class LoginPage(BasePage):
    _close_locator = (By.ID,"com.xueqiu.android:id/iv_action_back")
    _usrpwd_locator = (By.ID,"com.xueqiu.android:id/login_without_password")
    _button_next = (By.ID,"com.xueqiu.android:id/button_next")
    _login_account = (By.ID,"com.xueqiu.android:id/login_account")
    _login_password = (By.ID,"com.xueqiu.android:id/login_password")
    _forget_password = (By.ID,"com.xueqiu.android:id/tv_forget_password")
    _error_msg = (By.ID,"com.xueqiu.android:id/md_content")
    def loginByWX(self):
        return self

    def loginByMSG(self, phone, code):
        return self

    def loginbypassword(self, var1= 1, var2 = 2):
        #load by yaml
        self.loadSteps("../data/LoginPage.yaml", "loginByPassword", user = var1, password = var2)
        pass

    def loginByPassword(self, account, password):
        self.find(self._login_account).send_keys(account)
        self.find(self._login_password).send_keys(password)
        self.find(self._button_next).click()
        return self

    def loginSuccessByPassword(self, account, password):
        from page_obj.page.Mainpage import Mainpage
        return Mainpage()

    def back(self):
        WebDriverWait(self.driver,2).until(expected_conditions.presence_of_element_located(self._close_locator))
        from HGWZ.AppiumDemo import ProfilePage
        return ProfilePage()

    def getErrorMsg(self):
        msg = self.find(self._error_msg).text
        self.findByText("确定").click()
        return msg