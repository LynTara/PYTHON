import json
import logging
from datetime import time
import time

import pystache as pystache
import requests

from HGWZ.work_weixin.contact_new import user
from HGWZ.work_weixin.contact_new.token import Weixin
from HGWZ.work_weixin.contact_new.user import User
from HGWZ.work_weixin.contact_new.utils import Utils


class TestUser:
    logging.basicConfig(level=logging.DEBUG)
    depart_id = 1
    @classmethod
    def setup_class(cls):
        #todo:create department
        Weixin.get_token()
        cls.user = User()

    def test_create_user(self):
        uid = "lynxu_"+str(time.time())
        data = {
            "userid": uid,
            "name": uid,
            "department": [self.depart_id],
            "email": uid+"@163.com"
        }
        r = self.user.create(data)
        logging.debug(r)
        assert r["errcode"] == 0


    def test_user_list(self):
        r = self.user.list()
        logging.info(json.dumps(r, indent=2))
        assert r["errcode"] == 0



    # def test_user_by_template(self):
    #     print(pystache.render("hello {{name}} {{#has}} world {{value}} {{/has}}",
    #                           {"name":"lin",
    #                            "has":[{"value": 1},{"value": 2},{"value": 3}]
    #                            }))

    def test_user_by_real(self):
        uid = "lynxu"+str(time.time())
        mobile = Utils.udid()
        email = uid+"@1.com"
        data = Utils.parse("user_create.json",{
            "name":uid,
            "title":"Teacher",
            "email":email,
            "mobile": mobile
            })
        data = data.encode('UTF-8')
        r = self.user.create(data=data)
        logging.debug(r)
        assert r["errcode"] == 0