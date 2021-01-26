import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver


class Testxueqiu(object):


   @classmethod
   #当前类下的所有用例执行之前只执行一次
   def setup_class(cls):
      cls.driver = cls.install_app()#cls.driver实际未被调用
      print("setup class")


   # 当在每个测试用例执行之前执行一次
   def setup_method(self):
      print("setup method")
      #获取启动的appium的driver实例，用于后续每个case的driver
      self.driver = self.restart_app()


   # def test_login(self):
   #    # el1 = Testxueqiu.driver.
   #    # el1.click()
   #    el2 = self.driver.find_element_by_id("tv_login_phone")
   #    el2.click()

   def test_hot(self):
      #首次进入app的同意弹窗，没找到合适的位置存放，放在第一个case内，调试可以通过
      agree = self.driver.find_element_by_id("com.xueqiu.android:id/tv_agree")
      agree.click()
      el = self.driver.find_element_by_xpath("//*[contains(@resource-id,'title')]//*[@text='热门']")
      el.click()
      # Testxueqiu.driver.find_element_by_xpath("//*[contains(@resource-id,'indicator')]//*[@text='基金']")


   def test_swipe(self):
      self.driver.find_element_by_xpath("//*[contains(@resource-id,'title')]//*[@text='热门']")
      for i in range(5):
         self.driver.swipe(1000, 1000, 200, 200)
         time.sleep(2)
         self.driver.get_screenshot_as_file(str(i)+'.png')

   # 根据页面具体坐标进行滑动
   def test_action(self):
      self.driver.find_element_by_xpath("//*[contains(@resource-id,'title')]//*[@text='热门']")
      action = TouchAction(self.driver)
      for i in range(5):
         # action.tap_and_hold(x=1000,y=1000).move_to(x=200,y=200).perform()  #报错无tap_and_hold这个方法
         action.press(x=500,y=500).move_to(x=200,y=200).release().perform()
         time.sleep(2)

   # 根据页面下相对百分比进行滑动
   def test_action_p(self):
      rect = self.driver.get_window_rect()
      self.driver.find_element_by_xpath("//*[contains(@resource-id,'title')]//*[@text='热门']")
      action = TouchAction(self.driver)
      for i in range(5):
         # action.tap_and_hold(x=1000,y=1000).move_to(x=200,y=200).perform()  #报错无tap_and_hold这个方法
         action.press(x=rect['width']*0.3,y=rect['height']*0.3).move_to(x=rect['width']*0.3,y=rect['height']*0.8).release().perform()
         time.sleep(2)

   #获取屏幕大小
   def test_window_size(self):
      print(self.driver.get_window_rect())

   def teardown_method(self):
      #不加也没关系，如果不quit,启动appium会自动quit之前的session
      self.driver.quit()



   @classmethod
   def install_app(cls) -> WebDriver:
      caps = {}
      #如果有必要，进行第一次安装
      caps["platformName"] = "android"
      caps["appPackage"] = "com.xueqiu.android"
      caps["appActivity"] = ".view.WelcomeActivityAlias"
      #解决首次启动问题（权限问题）
      caps["autoGrantPermissions"] = "true"
      #为了更快的启动，并保留之前的数据，从而可以保存上一个case执行后的状态
      caps["noReset"] = "true"

      driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
      driver.implicitly_wait(10)
      return driver

   @classmethod
   def restart_app(cls) -> WebDriver:
      caps = {}

      caps["platformName"] = "android"
      caps["appPackage"] = "com.xueqiu.android"
      caps["appActivity"] = ".view.WelcomeActivityAlias"
      # 为了更快的启动，并保留之前的数据，从而可以保存上一个case执行后的状态
      caps["noReset"] = "true"
      # caps["autoGrantPermissions"] = "true"

      driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
      driver.implicitly_wait(10)
      return driver
