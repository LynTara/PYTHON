from HGWZ.AppiumDemo.page_object.pages import App
from HGWZ.AppiumDemo.page_object.pages import MainPage


class TestSelected(object):
    @classmethod
    def setup_class(cls):
        cls.mainPage = App.main()

    def setup_method(self):
        self.mainPage:MainPage = TestSelected.mainPage


    def test_price(self):
        # main = App.main().gotoselected()
        assert self.mainPage.gotoselected().gotoHS().getPriceByName('科大讯飞') >= 41.0