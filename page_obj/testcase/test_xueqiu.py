from page_obj.page.Mainpage import Mainpage
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import logging

from page_obj.page.Profilepage import Profilepage


class Testxueqiu(object):
    # logging.basicConfig()
    log=logging.getLogger("test_xueqiu")
    log.setLevel(logging.DEBUG)

    def setup(self):
        self.driver=webdriver.Chrome()
        self.drvier=webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)
        self.driver.get("https://xueqiu.com/")
        self.driver.implicitly_wait(10)
        #这一步想不到，不知道怎么关联起来(初始化)
        self.main= Mainpage(self.driver)

    def test_search(self):
        #为什么这里search（）函数和follow()函数自动加载不出来，
        self.main.search('alibaba').follow('09988')

    def test_profile(self):
        profile=Profilepage(self.driver)
        profile.login()
        selected=profile.gotoselected()
        selected.select("alibaba","1688")

    def test_log(self):
        self.log.warning("warning demo")
        self.log.debug("debug demo")

    def teardown(self):
        self.drvier.quit()


