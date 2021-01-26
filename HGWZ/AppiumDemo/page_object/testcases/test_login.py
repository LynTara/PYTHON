from HGWZ.AppiumDemo.page_object.pages import App
from HGWZ.AppiumDemo.page_object.pages import MainPage


class TestLogin(object):
    @classmethod
    def setup_class(cls):
        cls.mainPage = App.main()

    def setup_method(self):
        self.mainPage:MainPage = TestLogin.mainPage
        self.loginPage = self.mainPage.gotoprofile().gotologin()


    def test_login_password(self):
        self.loginPage.loginByPassword("15168228946000","111111")
        assert "手机号码" in self.loginPage.getErrorMsg()
        self.loginPage.back()

        self.loginPage.loginByPassword("15168228946","111111")
        assert "密码错误" in self.loginPage.getErrorMsg()
        self.loginPage.back()



    def teardown_method(self):
        pass