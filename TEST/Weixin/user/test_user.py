import json
import logging
import time

import requests

from TEST.Weixin.department.token import Token


class TestUser:
    logging.basicConfig(level=logging.DEBUG)
    uid = str(time.time()).replace(".", "")[0:9]
    def setup_class(cls):
        Token.get_token()

    def test_create_user(self):
        data={
            "userid": self.uid,
            "name": "lyn"+self.uid,
            "email": self.uid+"@1.com",
            "department": 2
        }
        r=requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create",
                      params={"access_token": Token.get_token()},
                      json=data).json()
        logging.debug(r)
        assert r["errcode"] == 0

    #todo:userid通过变量传入，非写死输入查询
    def test_get_user(self):
        r=requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/get",
                     params={
                         "access_token": Token.get_token(),
                         "userid":"161164332"
                     }).json()
        logging.info(json.dumps(r, indent=2))
        assert r["errcode"] == 0

    # todo:userid通过变量传入，非写死输入查询
    def test_update_user(self):
        data={
            "userid":"161164332"
        }
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/update",
                      params={"access_token": Token.get_token()},
                      json=data
                      ).json()
        logging.info(json.dumps(r, indent=2))
        assert r["errcode"] == 0

    # todo:userid通过变量传入，非写死输入查询
    def test_delete_user(self):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/delete",
                         params={
                             "access_token": Token.get_token(),
                             "userid": "161164326"
                         }).json()
        logging.debug(r)
        assert r["errcode"] == 0

    # todo:userid通过变量传入，非写死输入查询
    def test_batchdelete_user(self):
        data = {
            "useridlist": ["lynxu1611580531.5047355","lynxu1611580807.7704203"]
        }
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/batchdelete",
                          params={"access_token": Token.get_token()},
                          json=data
                          ).json()
        logging.debug(r)
        assert r["errcode"] == 0

    def test_simplelist(self):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/simplelist",
                         params={
                             "access_token": Token.get_token(),
                             "department_id": 1,
                             "fetch_child": 1
                         }).json()
        logging.info(json.dumps(r, indent=2))
        assert r["errcode"] == 0

    def test_userlist(self):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/list",
                         params={
                             "access_token": Token.get_token(),
                             "department_id": 1,
                             "fetch_child": 1
                         }).json()
        logging.info(json.dumps(r, indent=2))
        assert r["errcode"] == 0

    def test_get_openid(self):
        data = {"userid": "161164332"}
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/convert_to_openid",
                          params={"access_token": Token.get_token()},
                          json=data
                          ).json()
        logging.info(json.dumps(r, indent=2))
        assert r["errcode"] == 0
