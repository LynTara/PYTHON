import logging
import requests
import json

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

##首先，先写类，然后set_up方法，driver初始化
##chrome定位元素  $x('xpath表达式')  $('css表达式')

class TesterHome(object):
    logging.basicConfig(level=logging.INFO)
    # url='https://testerhome.com/'
    def setup(self):
        # self.driver=webdriver.Chrome()
        self.driver=webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)
        self.driver.implicitly_wait(10)
        self.driver.get('https://testerhome.com/')

    # def test_basic(self):
    #   self.driver.maximize_window()
    #


    def test_TesterHome(self):
        # r=requests.get(self.url)
        # logging.info(r)
        self.driver.maximize_window()
        self.driver.find_element_by_partial_link_text('MTSC2019').click()
        # self.driver.find_element_by_xpath('//*[@data-toggle="dropdown" and @class="btn btn-default"]').click()
        self.driver.find_element_by_css_selector('.toc-container .btn.btn-default').click()
        self.driver.find_element_by_partial_link_text('工程效率专场').click()
        self.driver.find_element_by_partial_link_text('陆金所造数服务').click()


    def test_execute_script(self):
        # 不要漏掉return，这个方法比requests更详细，可以获取requests无得到的一些内部指标
        raw=self.driver.execute_script("return JSON.stringify(window.performance.timing)")
        print(raw)
        print(json.dumps(json.loads(raw),indent=4))

    def tear_down(self):
        # self.sleep(10)
        self.driver.quit()

    def test_cookie(self):
        print(self.driver.get_cookies())




