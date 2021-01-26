import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver


class Testxueqiu(object):
   driver = WebDriver

   @classmethod

   #当前类下的所有用例执行之前只执行一次
   def setup_class(cls):
      cls.driver = cls.install_app()#cls.driver实际未被调用
      print("setup class")


   # 当在每个测试用例执行之前执行一次
   def setup_method(self):
      print("setup method")
      #获取启动的appium的driver实例，用于后续每个case的driver
      self.driver = Testxueqiu.driver


   def test_login_page(self):
      # 进入我的界面
      action = TouchAction(self.driver)
      self.driver.pre
      el2 = self.driver.find_element_by_id("tv_login_phone")
      el2.click()

   def test_login_password_error(self):
       # el1 = Testxueqiu.driver.
       # el1.click()
       el2 = self.driver.find_element_by_id("tv_login_phone")
       el2.click()



   def teardown_method(self):
      #不加也没关系，如果不quit,启动appium会自动quit之前的session
      self.driver.quit()



   @classmethod
   def install_app(cls) -> WebDriver:
      caps = {}
      #如果有必要，进行第一次安装
      caps["platformName"] = "android"
      caps["appPackage"] = "com.gongbangbang.www"
      # caps["appActivity"] = ".view.WelcomeActivityAlias"
      #解决首次启动问题（权限问题）
      caps["autoGrantPermissions"] = "true"
      #为了更快的启动，并保留之前的数据，从而可以保存上一个case执行后的状态
      # caps["noReset"] = "true"

      driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
      driver.implicitly_wait(10)
      return driver
