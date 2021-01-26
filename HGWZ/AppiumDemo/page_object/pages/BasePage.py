# from appium.webdriver import WebElement
import yaml
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from HGWZ.AppiumDemo import AndroidClient


class BasePage(object):
    # driver:WebDriver
    def __init__(self):
        # self.driver = AndroidClient.driver
        self.driver = self.getDriver()

    @classmethod
    def getDriver(cls):
        cls.driver = AndroidClient.driver
        return cls.driver

    @classmethod
    def getClient(cls):
        return AndroidClient

    def find(self,kv) -> WebElement:
        #todo:处理弹窗
        return self.driver.find_element(*kv)

    def findByText(self,text):
        return self.driver.find_element(By.XPATH,f"//*[@text='{text}']")

    def loadSteps(self, po_path, key, **kwargs):
        file = open(po_path,'r')
        po_data = yaml.load(file)
        po_method = po_data[key]
        for step in po_method:
            element:WebElement = self.driver.find_element(by=step['by'], value=step['locator'])
            action = str(step['action']).lower()

            #todo:定位失败，多数是因为弹窗，try catch后进入一个弹窗处理
            if str(step['action']).lower() == 'click':
                element.click()
            elif str(step['action']).lower() == 'sendkeys':
                element.send_keys(step['text'])
            else:
                print(f"UNKOWN COMMAND {step}")
