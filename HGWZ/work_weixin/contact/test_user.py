import json
import logging
from datetime import time
import time

import pystache as pystache
import requests

from HGWZ.work_weixin.contact.token import Weixin


class TestUser:
    logging.basicConfig(level=logging.DEBUG)
    depart_id = 1
    @classmethod
    def setup_class(cls):
        #todo:create department
        Weixin.get_token()

    def test_create_user(self):
        uid = str(time.time())
        data = {
            "userid": uid,
            "name": uid,
            "department": self.depart_id,
            "email": uid+"@163.com"
        }
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create",
                      params={"access_token": Weixin.get_token()},
                      json=data
                      ).json()
        logging.debug(r)
        assert r["errcode"] == 0


    def test_user_list(self):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/simplelist",
                     params={
                         "access_token": Weixin.get_token(),
                         "department_id": 1,
                         "fetch_child": 1
                     }).json()
        logging.info(json.dumps(r, indent=2))
        assert r["errcode"] == 0



    # def test_user_by_template(self):
    #     print(pystache.render("hello {{name}} {{#has}} world {{value}} {{/has}}",
    #                           {"name":"lin",
    #                            "has":[{"value": 1},{"value": 2},{"value": 3}]
    #                            }))

    def test_user_by_template(self):
        uid = "lynxu"+str(time.time())
        mobile = str(time.time()).replace('.','')[0:11]
        email = uid+"@1.com"
        data = self.get_user({"name":uid, "title":"Teacher", "email":email,"mobile": mobile})
        data = data.encode('UTF-8')
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create",
                          params={"access_token": Weixin.get_token()},
                          data=data,
                          headers={"content-type":"application/json; charset=UTF-8"}
                          ).json()
        logging.debug(r)
        assert r["errcode"] == 0

    def get_user(self, dict):
        template="".join(open("user_create.json",encoding='UTF-8').readlines())
        logging.debug(template)
        return pystache.render(template,dict)

    def test_get_user(self):
        logging.debug(self.get_user({"name":"lynxu", "title":"Teacher", "email":"1@1.com"}))