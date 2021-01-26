import json

from requests import options
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
# import pytest
import time


class Testxueqiu(object):
    @classmethod
    def setup_class(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver=webdriver.Chrome(options=options)
        self.driver=webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)
        self.driver.implicitly_wait(5)
        self.driver.get("https://xueqiu.com/")

    def test_xueqiu(self):
        self.driver.find_element_by_name("q").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath('//*[@class="iconfont_iconfont_9UW  search"]').click()
        self.driver.find_element_by_xpath("//*[@id='app']/div[2]/div/div[3]/div[1]/table/tr[2]/td[6]/a").click()
        self.driver.implicitly_wait(10)

        self.driver.find_element_by_name("username").send_keys("15168228946")
        self.driver.find_element_by_name("password").send_keys("123456")
        self.driver.find_element_by_class_name("modal__login__btn").click()

    def test_basic(self):
        self.driver.maximize_window()
        self.driver.fullscreen_window()

    def test_execute_script(self):
        raw= self.driver.execute_script("return JSON.stringify(window.performance.timing)")
        # print(raw)
        print(json.dumps(json.loads(raw),indent=4))

    def tear_down(self):
        time.sleep(10)
        self.driver.quit()

