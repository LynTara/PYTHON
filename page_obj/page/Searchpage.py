from page_obj.page.Basepage import Basepage


class Searchpage(Basepage):
    def follow(self,keyword):
        # self.driver.find_element_by_xpath("//*[@id='app']/div[2]/div/div[3]/div[1]/table/tr[2]/td[6]/a").click()
        self.driver.find_element_by_xpath('//*[contains(text(),"%s")]/../../../..//*[@class="follow__control"]' %keyword).click()
        self.driver.implicitly_wait(10)
        return self