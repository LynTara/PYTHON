import logging
import requests
import yaml

class Weixin():
    logging.basicConfig(level=logging.DEBUG)
    _token = ""

    @classmethod
    def get_token(cls):
        if len(cls._token) == 0:
            cls._token = cls.get_token_new()
        return cls._token



    @classmethod
    def get_token_new(cls):
        conf = yaml.safe_load(open("weixin.yaml",'rb'))
        logging.debug(conf["env"])
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                         params={
                             "corpid": conf["env"]["corpid"],
                             "corpsecret": conf["env"]["secretid"]}
                         ).json()
        return r["access_token"]