from HGWZ.work_weixin.contact_new.token import Weixin


class TestWeixin:
    def test_get_token(self):
        print(Weixin.get_token())
        assert Weixin.get_token() != ""
