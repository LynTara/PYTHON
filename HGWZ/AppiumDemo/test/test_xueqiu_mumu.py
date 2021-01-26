import time


from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Testxueqiu_mumu(object):
    driver = WebDriver
    @classmethod
    def setup_class(cls):
        cls.driver = cls.install_app()
        print("setup class")
        # el1 = cls.driver.find_element_by_id("com.gongbangbang.www:id/navigation_mine")
        # el1.click()

    def setup_method(self):
        print("setup method")
        # 获取启动的appium的driver实例，用于后续每个case的driver
        self.driver = Testxueqiu_mumu.driver
        self.driver.find_element_by_xpath("//*[@text='交易']")

    def test_webview_mumu(self):
        self.driver.find_element_by_accessibility_id("A股开户").click()
        self.driver.find_element_by_accessibility_id("立即开户")
        #显示等待
        WebDriverWait(self.driver,30).until(EC.presence_of_element_located(MobileBy.ACCESSIBILITY_ID,"立即开户"))



    def teardown_method(self):
        # 不加也没关系，如果不quit,启动appium会自动quit之前的session
        self.driver.back()

    @classmethod
    def install_app(cls) -> WebDriver:
        caps = {}
        # 如果有必要，进行第一次安装
        caps["platformName"] = "android"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        # 解决首次启动问题（权限问题）
        caps["autoGrantPermissions"] = "true"
        # 为了更快的启动，并保留之前的数据，从而可以保存上一个case执行后的状态
        caps["noReset"] = "true"
        caps["uuid"] = "127.0.0.1:7555"

        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(10)
        return driver
