from requests import options
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
import time


class TestZJS(object):
    @classmethod
    def setup_class(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        # self.driver=webdriver.Chrome(options=options)
        self.driver=webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)
        self.driver.get("https://tgtest.taogongscm.com/console/?ctl=passport")

    def test_zjs(self):
        #后台登录
        self.driver.find_element_by_name("uname").send_keys("lint236")
        self.driver.find_element_by_name("password").send_keys("Dunan123")
        self.driver.find_element_by_xpath("//*[@class='btn btn-success uppercase']").click()
        self.driver.fullscreen_window()
        time.sleep(2)
        #通过会员列表进入前台会员中心
        self.driver.find_element_by_partial_link_text("会员").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_partial_link_text("会员列表").click()
        self.driver.find_element_by_xpath("//*[@href='index.php?app=b2c&ctl=admin_member_gofront&act=redirect&p[0]=1978548&singlepage=1']").click()
        # self.driver.implicitly_wait(5)
        #跳转至会员前台页面
        self.driver.fullscreen_window()
        time.sleep(2)
        #查找商品
        self.driver.find_element_by_xpath("//*[@id='input_keyword']").send_keys("151752")
        self.driver.find_element_by_link_text("搜索").click()
        self.driver.find_element_by_partial_link_text("搜索").click()
        self.driver.find_element_by_xpath("//*[@href='/item-1495.html']").click()
        #跳转商品详情页

    @classmethod
    def teardown_class(self):
        self.driver.quit()



