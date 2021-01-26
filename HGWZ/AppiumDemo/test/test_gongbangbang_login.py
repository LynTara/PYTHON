import time

from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class Testgongbb(object):
    driver = WebDriver
    @classmethod
    def setup_class(cls):
        cls.driver = cls.install_app()
        print("setup class")
        el1 = cls.driver.find_element_by_id("com.gongbangbang.www:id/navigation_mine")
        el1.click()

    def setup_method(self):
        print("setup method")
        # 获取启动的appium的driver实例，用于后续每个case的driver
        self.driver = Testgongbb.driver
        el2 = self.driver.find_element_by_id("com.gongbangbang.www:id/loginRegister")
        el2.click()

    def test_swipe_screenshot(self):
        for i in range(3):
            self.driver.swipe(1000,1000,200,200)
            time.sleep(2)

    def test_gongbb_phone(self):
        el3 = self.driver.find_element_by_id("com.gongbangbang.www:id/codeLogin")
        el3.click()

    def test_gongbb_password(self):
        phone = self.driver.find_element_by_id("com.gongbangbang.www:id/phone").send_keys("15168228946")
        psword = self.driver.find_element_by_id("com.gongbangbang.www:id/password").send_keys("lin123456")
        login_btn = self.driver.find_element_by_id("com.gongbangbang.www:id/login").click()
        time.sleep(2)
        assert self.driver.find_element_by_xpath("//*[@text='专 心 服 务 工 业 用 品 经 销 商']")
        print("login success")

    # def test_password_foget(self):
    #     el4 = self.driver.find_element_by_id("com.gongbangbang.www:id/forgetPassword")
    #     el4.click()

    def test_gongbb_wechat(self):
        pass

    def teardown_method(self):
        # 不加也没关系，如果不quit,启动appium会自动quit之前的session
        self.driver.back()

    @classmethod
    def install_app(cls) -> WebDriver:
        caps={}
        caps["platformName"] = "android"
        caps["appPackage"] = "com.gongbangbang.www"
        caps["automationName"] = "UiAutomator2"
        caps["appActivity"] = "com.gongbangbang.www.business.app.MainActivity"
        # 为了更快的启动，并保留之前的数据，从而可以保存上一个case执行后的状态
        # caps["noReset"] = "true"
        caps["autoGrantPermissions"] = "true"

        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(10)
        return driver
