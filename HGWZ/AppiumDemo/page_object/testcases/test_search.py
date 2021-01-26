import pytest

from HGWZ.AppiumDemo.page_object.pages import App
from HGWZ.AppiumDemo.page_object.pages import MainPage


class TestSelected(object):
    @classmethod
    def setup_class(cls):
        cls.mainPage = App.main()

    def setup_method(self):
        self.mainPage:MainPage = TestSelected.mainPage
        self.searchPage = self.mainPage.gotosearch()

    @pytest.mark.parametrize("key,code",[
        ("alibaba","BABA"),
        ("alibaba","09988")
    ])
    def test_is_selected_stock(self, key, code):
        self.searchPage.search(key)
        self.searchPage.select_tab(code)
        assert self.searchPage.isInSelected(code)==True


    @pytest.mark.parametrize("key,code",[
        ("招商银行","SH600036"),
        ("平安银行","SZ000001"),
        ("中国平安","SH601318")
    ])
    def test_is_selected_stock_hs(self, key, code):
        self.searchPage.search(key)
        self.searchPage.select_tab(code)
        assert self.searchPage.isInSelected(code) == True

    def test_add_stock_hs(self):
        key = "招商银行"
        code = "SH600036"
        self.searchPage.search(key)
        if self.searchPage.isInSelected(code) == True:
            self.searchPage.removeFromSelected(code)
        self.searchPage.addToSelected(code)
        assert self.searchPage.isInSelected(code) == True


    def test_is_followed_user(self):
        self.searchPage.searchByUser("小白读财经")
        assert self.searchPage.isfollowed("小白读财经") == True
        print("user is followed")


    def teardown_method(self):
        self.searchPage.cancel()