from page_object.page.BasePage import BasePage
from page_object.page.SearchPage import SearchPage


class MainPage(BasePage):
    def search(self, keyword):
        self.driver.find_element_by_css_selector('.Header_nav__search_1YZ input').send_keys(keyword)
        self.driver.find_element_by_css_selector('.Header_nav__search_1YZ button').click()
        return SearchPage(self.driver)