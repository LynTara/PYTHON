from time import sleep

import pytest
from selenium import webdriver


class TestTesterHome(object):

    def setup_class(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)

    @classmethod
    def test_taogongscm_login(self):
        self.driver.get('https://www.w3school.com.cn/css/index.asp')
        # cls.driver.find_element_by_name('uname').send_keys('lint236')
        # cls.driver.find_element_by_name('password').send_keys('Dunan123')
        # cls.driver.find_elements_by_class_name('.btn.btn-success.uppercase').click()
        self.driver.sleep(10)

    def test_basic(self):
        self.driver.maximize_window()
        self.driver.fullscreen_window()

    def test_execute_script(self):
        raw=self.driver.execute('JSON.stringify(window.performance.timing)')
        print(raw)


    def tear_down(self):
        sleep(10)
        self.driver.quit()

