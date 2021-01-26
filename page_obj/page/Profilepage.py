from page_obj.page.Basepage import Basepage
from page_obj.page.Selectedpage import Selectedpage


class Profilepage(Basepage):
    def login(self):
        self.driver.add_cookie({"name": "device_id", "value": "24700f9f1986800ab4fcc880530dd0ed"})
        self.driver.add_cookie({"name": "Hm_lvt_1db88642e346389874251b5a1eded6e3", "value": "1605840520,1606463759"})
        self.driver.add_cookie({"name": "xq_is_login", "value": "1"})
        self.driver.add_cookie({"name": "u", "value": "4436135391"})
        self.driver.add_cookie({"name": "snbim_minify", "value": "true"})
        self.driver.add_cookie({"name": "bid", "value": "19d4c3aff656a17b359eb68b20218dfe_ki47vhus"})
        self.driver.add_cookie({"name": "__utma", "value": "1.656444562.1606720465.1606720465.1606720465.1"})
        self.driver.add_cookie({"name": "__utmc", "value": "1"})
        self.driver.add_cookie(
            {"name": "__utmz", "value": "1.1606720465.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)"})
        self.driver.add_cookie({"name": "is_overseas", "value": "0"})
        self.driver.add_cookie({"name": "Hm_lpvt_1db88642e346389874251b5a1eded6e3", "value": "1606720619"})
        self.driver.add_cookie({"name": "s", "value": "d419xyavom"})
        self.driver.add_cookie({"name": "xq_a_token", "value": "cdfa8b5e0a2da43c2b2657f44c22e6526008cebe"})
        self.driver.add_cookie({"name": "xq_id_token",
                                "value": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjQ0MzYxMzUzOTEsImlzcyI6InVjIiwiZXhwIjoxNjA5MzExOTcwLCJjdG0iOjE2MDY3MTk5NzA5OTQsImNpZCI6ImQ5ZDBuNEFadXAifQ.cN9YhQn74_njJlEJum9zDL_-SzX3RxAYi6vs0xZZ3nEiEE0AhPUTIvqO_k5cuYqwo-CKVkxFEcKo1dZSREYQvRF4HyafOcy8RJk8dBfDfsCr5PeD_LWwmZYell1rR0f9A_Ow_7P5L2BSHfZUnP4PdYllH4zsQZ0CYKkzvYppts8smWRXV3KhZIPfJuEdYq_ZXb-oA-QHPkfrdyOMkiOcPe-h7ly_GYhx-4VtdXMhkp6muUJ6mCpFrOVEe1FIqJ3-QLDJYNO-GyjZwtPBn-GG7IfvsOHej6eEANbISUXU0lCYeUsXWnz-BVExF0h-fH1nmJ0UiAR5STMGE5Gb5Yx2pw"})
        self.driver.add_cookie({"name": "xqat", "value": "cdfa8b5e0a2da43c2b2657f44c22e6526008cebe"})
        self.driver.add_cookie(
            {"name": "acw_tc", "value": "2760823e16067198430921484e510af2ed378ef3422b7b63501dd78acde544"})
        self.driver.add_cookie({"name": "is_overseas", "value": "0"})
        self.driver.add_cookie({"name": "remember", "value": "1"})
        self.driver.add_cookie({"name": "xq_r_token", "value": "919f437eff736f375db0968078b4794fbf5384c5"})

        print(self.driver.get_cookies())
        self.driver.refresh()


    def gotoselected(self):
        return Selectedpage()
