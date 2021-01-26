from selenium.webdriver.common.by import By

from HGWZ.AppiumDemo import BasePage


class SearchPage(BasePage):
    _editLocator = (By.ID, "com.xueqiu.android:id/search_input_text")

    def search(self, key):
        self.find(self._editLocator).send_keys(key)
        self.find(self._editLocator).click()
        return self #可以保持链式调用

    def addToSelected(self,key):
        follow_btn = (By.XPATH,
                      f"//*[contains(@resource-id,'stockCode') and contains(@text,'{key}')]/../../..//*[contains(@resource-id,'follow_btn')]")
        self.find(follow_btn).click()
        return self

    def removeFromSelected(self, key):
        followed_btn = (By.XPATH,
                      f"//*[contains(@resource-id,'stockCode') and contains(@text,'{key}')]/../../..//*[contains(@resource-id,'followed_btn')]")
        self.find(followed_btn).click()
        return self

    def select_tab(self,key):
        select_tab = (By.XPATH, f"//*[@resource-id='com.xueqiu.android:id/code' and contains(@text,'{key}')]/../..")
        self.find(select_tab).click()

    def isInSelected(self,key):
        follow_btn = (By.XPATH,f"//*[contains(@resource-id,'stockCode') and contains(@text,'{key}')]/../../..//*[contains(@resource-id,'follow')]")
        id=self.find(follow_btn).get_attribute("resourceId")
        print(id)
        return "followed_btn" in id

    def searchByUser(self,key):
        self.find(self._editLocator).send_keys(key)
        #点击输入栏显示搜索栏结果下拉栏
        self.find(self._editLocator).click()
        user_btn = (By.XPATH,"//*[@resource-id='com.xueqiu.android:id/title_container' ]/..//*[@text='用户']")
        user_tab = (By.XPATH,f"//*[@resource-id='com.xueqiu.android:id/name' and contains(@text,'{key}')]/../..")
        self.find(user_tab).click()
        self.find(user_btn).click()


        return self

    def isfollowed(self,key):
        follow_btn = (By.XPATH,
                      f"//*[@resource-id='com.xueqiu.android:id/user_name' and contains(@text,'{key}')]/../../..//*[ contains(@text,'关注') and contains(@resource-id,'follow')]")
        id = self.find(follow_btn).get_attribute("resourceId")
        print(id)
        return "followed_btn" in id

    def cancel(self):
        self.findByText("取消").click()






