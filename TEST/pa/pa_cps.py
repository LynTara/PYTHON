from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class CPS(object):
    def cps(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")

