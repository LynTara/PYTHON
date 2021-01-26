#安装app
#启动app
#使用一个全局变量
from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class AndroidClient(object):
    driver: WebDriver
    @classmethod
    def install_app(cls) -> WebDriver:
        caps = {}
        # 如果有必要，进行第一次安装
        caps["platformName"] = "android"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        # 解决首次启动问题（权限问题）
        caps["autoGrantPermissions"] = True
        # 为了更快的启动，并保留之前的数据，从而可以保存上一个case执行后的状态
        caps["noReset"] = "true"


        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)
        return cls.driver

    @classmethod
    def restart_app(cls) -> WebDriver:
        caps = {}

        caps["platformName"] = "android"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        # 为了更快的启动，并保留之前的数据，从而可以保存上一个case执行后的状态
        caps["noReset"] = "true"
        # caps["autoGrantPermissions"] = "true"
        caps['unicodeKeyboard'] = False
        caps['resetKeyboard'] = False

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)
        return cls.driver