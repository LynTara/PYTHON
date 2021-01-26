from HGWZ.AppiumDemo import BasePage
from HGWZ.AppiumDemo import MainPage


class App(BasePage):
    @classmethod
    def main(cls):
        cls.getClient().restart_app()
        # AndroidClient.restart_app()
        return MainPage()