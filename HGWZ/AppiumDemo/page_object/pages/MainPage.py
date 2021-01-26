from selenium.webdriver.common.by import By

from HGWZ.AppiumDemo import ProfilePage
from HGWZ.AppiumDemo import BasePage
from HGWZ.AppiumDemo import SearchPage
from HGWZ.AppiumDemo import SelectedPage


class MainPage(BasePage):


    def gotoselected(self):
        #点击进入行情页面
        hangqing=(By.XPATH,'//*[@resource-id="com.xueqiu.android:id/tab_icon"]/../../android.widget.RelativeLayout[2]')
        self.find(hangqing)
        self.find(hangqing).click()
        # self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/tab_icon"]/../../android.widget.RelativeLayout[2]')
        # self.driver.find_element(By.XPATH,'//*[@resource-id="com.xueqiu.android:id/tab_icon"]/../../android.widget.RelativeLayout[2]')
        # self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/tab_icon"]/../../android.widget.RelativeLayout[2]').click()
        return SelectedPage()

    def gotosearch(self):
        search_button = (By.ID,"home_search")
        self.find(search_button).click()
        return SearchPage()

    def gotoprofile(self):
        _profile_btn = (By.XPATH, '//*[@resource-id="com.xueqiu.android:id/tab_icon"]/../../android.widget.RelativeLayout[5]')
        self.find(_profile_btn).click()
        return ProfilePage()

