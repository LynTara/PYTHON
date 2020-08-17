import json
import logging
import requests


class TestRequests(object):
    logging.basicConfig(level=logging.INFO)
    url = "https://testerhome.com/api/v3/topics.json?limit=2"
    def test_get(self):
        r=requests.get(self.url)  #ctrl+B进入request库说明
        logging.info(r)
        logging.info(r.text)
        logging.info(json.dumps(r.json(),indent=2))

    def test_post(self):
        r=requests.get(self.url,
                        params={'a':1,'b':'string',},
                        headers={"a":"1","b":"b2"},
                        proxies={'https':'127.0.0.1:8888','http':'127.0.0.1:8888'},
                        verify=False)
        logging.info(r.url)
        logging.info(r.text)
        logging.info(json.dumps(r.json()),indent=2)
        # 调试：1.代理工具 verify=False可跳过证书的验证

    def test_cookies(self):
        url="http://www.httpbin.org/cookies"
        r=requests.get(self.url,
                       params={"category":"1"},
                       headers={"User-Agent":"Xueqiu Android 11.19"},
                       cookies={"u":"194858","xq_a_token":"11111111111"})
        logging.info(json.dumps(r.json(),indent=2))

