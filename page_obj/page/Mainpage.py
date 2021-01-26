from page_obj.page.Searchpage import Searchpage
from page_obj.page.Basepage import Basepage


class Mainpage(Basepage):
    def search(self,keyword):
        self.driver.find_element_by_name("q").send_keys(keyword)
        self.driver.find_element_by_xpath('//*[@class="iconfont_iconfont_9UW  search"]').click()
        return Searchpage(self.driver)
