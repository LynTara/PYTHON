from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


class TestTesterHome(object):

    def setup_class(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        options=webdriver.ChromeOptions()
        # options.binary_location='chrome path'
        # self.driver=webdriver.Chrome(options=options)
        self.driver=webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)

        self.driver.implicitly_wait(10)
        self.driver.get("https://testerhome.com")

    def test_mtsc2020(self):
        self.driver.find_element_by_partial_link_text("MTSC2020").click()
        self.driver.find_element_by_xpath('//*[@data-toggle="dropdown"]').click()
        # self.driver.find_element_by_xpath('//*[text()[contains(.,"目录")]]').click()//目录按钮用text()定位
        # self.driver.find_element_by_css_selector('.toc-container .btn-default').click()//目录按钮css定位
        self.driver.find_element_by_partial_link_text("大会议题详情").click()


    # def test_basic(self):
    #     self.driver.maximize_window()
    #     self.driver.fullscreen_window()
    #
    # def test_execute_script(self):
    #     self.driver.execute('getxxx',params={'x':1,'y':2})
    #     # raw=self.driver.execute('JSON.stringify(window.performance.timing)')
    #     # print(raw)


    def tear_down(self):
        sleep(10)
        self.driver.quit()

    # def test_cookie(self):
    #     print(self.driver.get_cookies())

