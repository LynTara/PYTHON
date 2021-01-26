from selenium.webdriver.common.by import By

from HGWZ.AppiumDemo import BasePage


class SelectedPage(BasePage):
    def addDefault(self):
        return self

    def gotoHS(self):
        self.findByText("沪深").click()
        return self

    def getPriceByName(self,name):
        #根据name获取股价
        # price = self.driver.find_element_by_xpath(f"//*[contains(@resource-id,'stockName') and @text = '{name}'] /../../../..//*[contains(@resource-id,'currentPrice')]").text
        priceLocator = (By.XPATH,f"//*[contains(@resource-id,'stockName') and @text = '{name}'] /../../../..//*[@resource-id='com.xueqiu.android:id/row_recycler']/android.widget.FrameLayout[1]//*[@resource-id='com.xueqiu.android:id/item_layout']")
        price = self.find(priceLocator).text
        print(price)
        return float(price)