import requests
import logging
import json
import jsonpath
from hamcrest import *
from jsonschema import validate


class TestRequests(object):
    logging.basicConfig(level=logging.INFO)
    url = "https://testerhome.com/api/v3/topics.json?limit=2"
    def test_get(self):
        r = requests.get(self.url)
        logging.info(r)
        logging.info(r.text)
        logging.info(json.dumps(r.json(), indent=2))
        print(json.dumps(r.json(), indent=2))


    def test_post(self):
        r = requests.post(self.url,
                          params={"a":1,"b":"string content"},
                          proxies={"https":"192.168.0.117:9999"},
                          verify=False)
        logging.info(r)
        logging.info(r.text)
        logging.info(json.dumps(r.json(), indent=2))


    def test_xueqiu_quote(self):
        url = "https://stock.xueqiu.com/v5/stock/portfolio/stock/list.json?"
        params = {
            "category": "1",
            "pid":"-1",
            "page":"1",
            "size":"2000",
            "uid":"4436135391",
            "x":"0.143"
        }
        headers = {
            "User-Agent": "Xueqiu iPhone 12.27",
            "Accept": "application/json","Accept-Language": "zh-Hans-CN;q=1, en-CN;q=0.9, ko-CN;q=0.8"
        }
        cookies = {
            "u": "4528501798",
            "xq_a_token": "9413c32d4333c47ba5eda34ae926e38786b32fab",
            "xq_id_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjQ0MzYxMzUzOTEsImlzcyI6InVjIiwiZXhwIjoxNjEzNjM5NTU3LCJjdG0iOjE2MTEwNDc1NTc4NjQsImNpZCI6IldpQ2lteHBqNUgifQ.XTb6KpWu5ypgxXTlEtS1zQlGA9L3CaNd-Qqz7stgQ6zMzA1jyT1yG9vQAiV_5r-clrWnJB5VjWNtIvQ9ftfdgh49oMEUm4gpUwAVhmNrGstezw8U0idkHl0IbWFISsX9Irx0MG4uKeaBPoDXWJKzkzxV8w7xKbGctBxkICv3wYGoXkEwFKAgEKiwWqXCgqU9f-XW_qKQdHVlspokehN6oJwh4I_d9OH-mcXt08_SfY5qj0Erik2ioutj66r6htXxUeiNaOvTXgjGKYsBhxQEn59PJjMvA_MRUFAI_ufUHUMGc4_qbP7oCq2mEcTCbee8UMSo3SRfKzqvLcEjb2kx8A"
        }
        r = requests.get(url,params=params,headers=headers,cookies=cookies,verify=False)
        logging.info(r.text)
        logging.info(json.dumps(r.json(),indent=2))

        assert r.json()["data"]["category"] == 1
        assert r.json()["data"]["stocks"][0]["name"] == "阿里巴巴"
        # logging.info((jsonpath.jsonpath(r.json(), "$.data.stocks[0].name")))
        assert jsonpath.jsonpath(r.json(), "$.data.stocks[?(@.symbol == 'BABA')].name")[0] == '阿里巴巴'
        assert_that(jsonpath.jsonpath(r.json(), "$.data.stocks[?(@.symbol == 'BABA')].name")[0], equal_to("阿里巴巴1"),"比较上市代码与名字")
        # logging.info(jsonpath.jsonpath(r.json(),"$.data.stocks[*].name"))
        assert_that(jsonpath.jsonpath(r.json(), "$.data.stocks[*].name"),any_of(has_items('比亚迪','拼多多')))

    def test_xueqiu_list_schema(self):
        url = "https://stock.xueqiu.com/v5/stock/portfolio/stock/list.json?"
        params = {
            "category": "1",
            "pid": "-1",
            "page": "1",
            "size": "2000",
            "uid": "4436135391",
            "x": "0.143"
        }
        headers = {
            "User-Agent": "Xueqiu iPhone 12.27",
            "Accept": "application/json", "Accept-Language": "zh-Hans-CN;q=1, en-CN;q=0.9, ko-CN;q=0.8"
        }
        cookies = {
            "u": "4528501798",
            "xq_a_token": "9413c32d4333c47ba5eda34ae926e38786b32fab",
            "xq_id_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjQ0MzYxMzUzOTEsImlzcyI6InVjIiwiZXhwIjoxNjEzNjM5NTU3LCJjdG0iOjE2MTEwNDc1NTc4NjQsImNpZCI6IldpQ2lteHBqNUgifQ.XTb6KpWu5ypgxXTlEtS1zQlGA9L3CaNd-Qqz7stgQ6zMzA1jyT1yG9vQAiV_5r-clrWnJB5VjWNtIvQ9ftfdgh49oMEUm4gpUwAVhmNrGstezw8U0idkHl0IbWFISsX9Irx0MG4uKeaBPoDXWJKzkzxV8w7xKbGctBxkICv3wYGoXkEwFKAgEKiwWqXCgqU9f-XW_qKQdHVlspokehN6oJwh4I_d9OH-mcXt08_SfY5qj0Erik2ioutj66r6htXxUeiNaOvTXgjGKYsBhxQEn59PJjMvA_MRUFAI_ufUHUMGc4_qbP7oCq2mEcTCbee8UMSo3SRfKzqvLcEjb2kx8A"
        }
        r = requests.get(url, params=params, headers=headers, cookies=cookies, verify=False)
        logging.info(json.dumps(r.json(), indent=2))
        schema=json.load(open("list_schema.json",'rb'))
        validate(instance=r.json(), schema=schema)

    def test_hamcrest(self):
        assert_that(0.1 * 0.1, close_to(0.01, 0.01000000000001))
        # assert_that(0.1 * 0.1, close_to(0.01, 0.000000000000000001))
        # assert_that(['a','b','c'],has_item('d'))
        assert_that(
            ['a','b','c'],
            any_of(
                has_items('c','a'),
                has_items('a','d')
            )
        )
        assert_that(
            ['a', 'b', 'c'],
            all_of(
                has_items('c', 'a'),
                has_items('a', 'f')
            )
        )

    def test_schema(self):
        schema = {
            "type": "object",
            "properties": {
                "price": {"type": "number"},
                "name": {"type": "string"},
            },
        }
        validate(instance={"name": "Eggs", "price": 34.99}, schema=schema)
        validate(
            instance={"name": "Eggs", "price": "Invalid"}, schema=schema,
        )