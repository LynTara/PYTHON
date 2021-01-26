import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver


class Testxueqiu_swipe(object):
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
        self.driver = Testxueqiu_swipe.driver
        # el2 = self.driver.find_element_by_id("com.gongbangbang.www:id/loginRegister")
        # el2.click()

    def test_swipe_loop(self):
        self.driver.find_element_by_xpath("//*[contains(@resource-id,'title')]//*[@text='热门']")
        action = TouchAction(self.driver)
        rect = self.driver.get_window_rect()
        #怎么确认是否滑动到最后一个页面，没想到处理方案就把数据先写死了
        for i in range(3):
            # self.driver.swipe(1000,1000,200,200)
            action.press(x=rect["width"]*0.9,y=rect["height"]*0.8).move_to(x=rect["width"]*0.1,y=rect["height"]*0.8).release().perform()
            time.sleep(2)
            for j in range(5):
                action.press(x=rect["width"]*0.1,y=rect["height"]*0.9).move_to(x=rect["width"]*0.1,y=rect["height"]*0.1).release().perform()


    def teardown_method(self):
        # 不加也没关系，如果不quit,启动appium会自动quit之前的session
        self.driver.quit()

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

        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(10)
        return driver
