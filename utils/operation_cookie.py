import requests
import json
from utils.operation_json import OperationJson

"""
每个测试平台脚本可能不一样的方式
获取token认证值
"""

class OperationCookie():
    def __init__(self, cookie_path=None):
        if cookie_path:
            self.cookie_path = cookie_path
        else:
            self.cookie_path = "../data/cookie.json"
        self.op_json = OperationJson(file_name=self.cookie_path)
        # self.op_json = op_json.data

    def write_cookie(self, value):
        self.op_json.write_data(value)

    def get_cookie(self, key):
        ck = self.op_json.get_value(key)
        return ck

    def get_cookie_file_data(self):
        ck_file = self.op_json.get_all_value()
        return ck_file

    def trans_response_cookie_value(self,response):
        # print(response.cookies,response.content)
        ck_value = requests.utils.dict_from_cookiejar(response.cookies)
        print('cookie value:',ck_value)
        return ck_value

if __name__ == '__main__':
    r = OperationCookie()
    r.write_cookie({"1a": "b"})
    print(r.get_cookie("1a"))

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
