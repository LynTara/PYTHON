import logging

import requests
import yaml


class Token:
    _token = ""

    @classmethod
    def get_token(cls):

        conf = yaml.safe_load(open("/PYTHON/Test/Weixin/token.yaml",'rb'))
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                     params={
                         "corpid": conf["env"]["corpid"],
                         "corpsecret": conf["env"]["secretid"]
                     }).json()
        logging.debug(conf["env"])
        cls._token = r["access_token"]
        return cls._token