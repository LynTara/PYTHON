import json
import logging
import time

import requests

from TEST.Weixin.department.token import Token


class TestDepartment:
    logging.basicConfig(level=logging.DEBUG)

    @classmethod
    def setup_class(cls):
        Token.get_token()

    def test_create_department(self):
        uid = str(time.time())[0:5]
        data = {
            "name": "lin0126"+uid,
            "parentid": 1
        }
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                     params={"access_token": Token.get_token()},
                     json=data
                         ).json()
        logging.debug(r)
        assert r["errcode"] == 0

    #可以修改部门的名称
    def test_update_department(self):
        data = {
            "id": 6,
            "name": "tara_011255666666",
            "parentid": 3
        }
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/update",
                      params={"access_token": Token.get_token()},
                      json=data).json()
        logging.debug(r)
        assert r["errcode"] == 0


    def test_delete_department(self):
        #todo:校验是否根部门(parent_id=0)；校验不含子部门；校验部门不含成员;校验是否删除成功
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/department/delete",
                     params={"access_token": Token.get_token(),
                             "id": 24
                    }
                     ).json()
        logging.debug(r)
        assert r["errcode"] == 0

    def test_getlist_department(self):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/department/list",
                     params={"access_token":Token.get_token()}).json()
        logging.info(json.dumps(r, indent=2))