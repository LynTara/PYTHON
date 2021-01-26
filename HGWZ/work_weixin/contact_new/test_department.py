import json

import pytest
import requests
import logging

from HGWZ.work_weixin.contact_new.token import Weixin
from HGWZ.work_weixin.contact_new.utils import Utils


class TestDepartment:
    def test_create(self, token):
        data = {
            "name": "广州研发中心",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1,
            "id": 2
        }
        r=requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create", verify=False,
                      params={"access_token":token},
                      json=data,
                      ).json()
        logging.debug(r)

    def test_list(self, token):
        r=requests.get("https://qyapi.weixin.qq.com/cgi-bin/department/list",
                     params={"access_token": token}).json()
        logging.info(json.dumps(r, indent=2))


    def test_create_name(self, token):
        data = {
            "name": "tara_01125",
            "parentid": 1
        }
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create", verify=False,
                          params={"access_token": token},
                          json=data,
                          ).json()
        logging.debug(r)


    def test_create_depth(self, token):
        parentid = 1
        for i in range(5):
            data = {
                "name": "tara_01125"+str(parentid),
                "parentid": parentid
            }
            r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create", verify=False,
                              params={"access_token": token},
                              json=data,
                              ).json()
            parentid=r["id"]
            logging.debug(r)
            assert r["errcode"] == 0

    @pytest.mark.parametrize("name",[
        "杭州研发中心",
        "東京研究センター",
        "東京動漫研究所",
        "Tokyo Anime Research Institute"
    ])
    def test_create_order(self, name, token):
        data = {
            "name": name+Utils.udid(),
            "parentid": 1
        }
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create", verify=False,
                          params={"access_token": token},
                          json=data,
                          ).json()
        logging.debug(r)