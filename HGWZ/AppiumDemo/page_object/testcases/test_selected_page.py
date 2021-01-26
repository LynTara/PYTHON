import time

import pytest

from HGWZ.AppiumDemo.page_object.pages import App
from HGWZ.AppiumDemo.page_object.pages import MainPage
from HGWZ.AppiumDemo.page_object.pages.SearchPage import SearchPage


class TestSelected(object):
    @classmethod
    def setup_class(cls):
        cls.mainPage = App.main()

    def setup_method(self):
        self.mainPage:MainPage = TestSelected.mainPage
        self.searchPage = self.mainPage.gotosearch()

    def test_price(self):
        # main = App.main().gotoselected()
        assert self.mainPage.gotoselected().getPriceByName('阿里巴巴') > 221

    def test_is_selected_stock(self):
        self.searchPage.search("alibaba")
        time.sleep(10)
        assert self.searchPage.isInSelected("BABA")==True
        assert self.searchPage.isInSelected("09988")==False

    @pytest.mark.parametrize("key,code",[
        ("招商银行","SH600036"),
        ("平安银行","SZ000001"),
        ("中国平安","SH601318")
    ])
    def test_is_selected_stock_hs(self, key, code):
        self.searchPage.search(key)
        assert self.searchPage.isInSelected(code) == False

    def test_add_stock_hs(self):
        key = "招商银行"
        code = "SH600036"
        self.searchPage.search(key)
        if self.searchPage.isInSelected(code) == True:
            self.searchPage.removeFromSelected(code)
        self.searchPage.addToSelected(code)
        assert self.searchPage.isInSelected(code) == True

    def teardown_method(self):
        self.searchPage.cancel()

    def test_is_followed_user(self):
        self.searchPage.searchByUser("小白读财经")
        assert SearchPage.isfollowed("小白读财经") == True
        print("user is followed")