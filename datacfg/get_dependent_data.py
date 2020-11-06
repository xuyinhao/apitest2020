from base.runhttp import RunMethod
from datacfg.get_data import GetData
from utils.common_util import CommonUtil
from utils.operation_excel import OperationExcel
from jsonpath_rw import jsonpath, parse
from utils.operation_cookie import OperationCookie
from utils.operation_token import OperationToken
import json


class DependentData():
    def __init__(self):
        # self.case_id = case_id
        self.get_data = GetData()
        self.run_method = RunMethod()
        self.com_util = CommonUtil()
        self.opera_excel = OperationExcel()

    def _get_case_row_num_by_caseid(self):
        rownum = self.get_data.get_case_row_by_idname(self.case_id)
        return rownum

    # rownum = self.get_data.get_case_row_by_idname(self.case_id)

    ## token=True,或者cookie=True是为了 refresh token使用的。单独执行一条case
    def _run_dependent_case(self, token=None, cookies=None):  # 不需要 isrun
        # i = self.get_data.get_case_row_by_idname(self.case_id) #获取id的行号
        i = self._get_case_row_num_by_caseid()
        method = self.get_data.get_request_method(i)
        url = self.get_data.get_url_final(i)
        data = self.get_data.get_request_data_final(i)
        header = self.get_data.get_header_info(i)
        expect_result = self.get_data.get_expect_result(i)
        # 执行请求 , 获得的结果，list[0]为响应code, [1]为结果

        if token:
            run_response_data = self.run_method.run_main(method, url, data=data, header=header)
            # print("#$$# :",str(run_response_data))
            op_token = OperationToken()
            token_value = op_token.trans_response_token_value_by_body(run_response_data[2])
            op_token.write_token(token_value)
            return token_value
        elif cookies:
            run_response_data = self.run_method.run_main(method, url, data=data, header=header)
            op_cookie = OperationCookie()
            cookie_value = op_cookie.trans_response_cookie_value(run_response_data[2])
            op_cookie.write_cookie(cookie_value)
            return cookie_value
        else:

            is_dependent = self.get_data.get_is_dependent(i)
            if is_dependent:
                op = DependentData()
                rs = op.get_dependent_data_for_key(i)
                # print('run dp data get : ' + rs)
                if not rs:  # 如果返回False, 就是依赖的case 失败了,那么这个例子也不用跑了
                    print('fail , dependent return case fail')
                    self.get_data.write_test_result(i, 'fail, dependent case return  fail')
                    return False
                # print('run dp data get : ' + rs)
                filed_data = self.get_data.get_dependent_filed(i)
                data[filed_data] = rs

            run_response_data = self.run_method.run_main(method, url, data, header)

        try:
            if self.com_util.is_contain(expect_result, run_response_data[1]):
                return json.loads(run_response_data[1])
            else:
                return False
        except Exception as e:
            print(e)

    # 通过 dependent 的key获取真实的 value内容
    def get_dependent_data_for_key(self, row):
        self.case_id = self.get_data.get_dependent_caseid(row)  # 获取case id
        denpendet_data = self.get_data.get_dependent_data(row)  # 获取 依赖上层的data key
        print('dp data:' + denpendet_data)
        response_data = self._run_dependent_case()  # 运行依赖
        print('rs data : ', response_data)

        if not response_data:
            return False
        json_exe = parse(denpendet_data)
        madle = json_exe.find(response_data)

        arr0 = [math.value for math in madle][0]
        return arr0  # 获取 依赖data

    ##如果想重新强制获取token更新，则提供登录的caseid:login_01, token=True
    def force_runcase_by_caseid(self, caseid, token=None, cookies=None):
        self.case_id = caseid
        if token:
            return self._run_dependent_case(token=True)

        # TODO
        if cookies:
            return True
        return self._run_dependent_case()


if __name__ == '__main__':
    a = DependentData()
    # a.force_runcase_by_caseid("login_01",token=True) #更新token
    r = a.get_dependent_data_for_key(2)
    # import json
    # print(json.loads(r)['data']['totaldev'])
    # print(r)
#     dp="data.totaldev"
#     rs={
#   "data": {
#     "nums": 3,
#     "start": 2,
#     "totaldev": "2,3,4"
#   },
#   "totalnum": 3
# }
#     jse=parse(dp)
#     md=jse.find(rs)
#     print([math.value for math in md][0])
# 数组
# a = {"data":[{
#     "username":"x"},
#     {"username":"y"}] }
# c = "data[0].username"
# json_exe = parse(c)
# madle = json_exe.find(a)
# print([math.value for math in madle])
