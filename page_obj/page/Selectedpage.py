from page_obj.page.Basepage import Basepage


class Selectedpage(Basepage):
    def select(self,keyword,market):
        self.driver.find_element_by_css_selector('.optional .search__dropdown').send_keys(keyword)



