from time import sleep

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from page_object.page.MainPage import MainPage


class TestXueqiu(object):
        def setup(self):
            #driver初始化
            self.driver=webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)
            self.driver.implicitly_wait(10)
            self.driver.get("https://xueqiu.com/")
            self.main=MainPage(self.driver)


        def test_search(self):
            self.main.search("alibaba").follow("9988")
            #todo: add assertion


        def teardown(self):
            sleep(60)
            self.driver.quit()
