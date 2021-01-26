from selenium.webdriver.remote.webdriver import WebDriver


class Basepage(object):
    def __init__(self,driver):
        self.driver:WebDriver= driver