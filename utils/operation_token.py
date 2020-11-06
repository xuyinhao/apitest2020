"""
每个测试平台脚本可能不一样的方式
获取token认证值
"""
import requests
import json
from utils.operation_json import OperationJson


class OperationToken():
    def __init__(self, token_path=None):
        if token_path:
            self.token_path = token_path
        else:
            self.token_path = "../data/token.json"
        self.op_json = OperationJson(file_name=self.token_path)
        # self.op_json = op_json.data

    def write_token(self, value):
        self.op_json.write_data(value)

    def get_token(self):
        tk = self.op_json.get_filevalue()
        return tk

    def get_cookie_file_data(self):
        ck_file = self.op_json.get_all_value()
        return ck_file

    def trans_response_token_value_by_body(self,response):
        tk_value=response.json()["data"]["token"]
        print('token value:',tk_value)
        return tk_value

    def trans_respons_token_value_by_headers(self,response):
        try:
            tk_value = response.headers["token"]    #需要修改为自己项目的token header
            return tk_value
        except:
            print("通过headers获取token,失败",str(response))
        return ""


if __name__ == '__main__':
    r = OperationToken()
    r.write_token({"1a": "b"})
    print(r.get_token("1a"))

# url = "http://127.0.0.1:2222/api/login"
# data = {
#     "username" : "admin",
#     "password": "21232f297a57a5a743894a0e4a801fc3"
# }
# grplistutl = "http://127.0.0.1:2222/api/store/devgrp/list"
# cookie = requests.get(url,params=data).cookies
# # cc = res["refreshToken"]["value"]
# cookie = requests.utils.dict_from_cookiejar(cookie)
# print(cookie)
# p = json.dumps(cookie["loongaio"])
# o  = OperationJson()
# o.write_cookie(p)
# a = o.get_value("cookie")
# print("a:",a)
#
# res1 = requests.post(url=grplistutl)
# print(res1.content)
# print(res1.status_code)
