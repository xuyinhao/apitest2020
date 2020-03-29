from base.runhttp import RunMethod
from datacfg.get_data import GetData
from utils.common_util import CommonUtil
from utils.operation_excel import OperationExcel
from jsonpath_rw import jsonpath, parse
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

    def _run_dependent_case(self):      #不需要 isrun
        # i = self.get_data.get_case_row_by_idname(self.case_id) #获取id的行号
        i = self._get_case_row_num_by_caseid()
        method = self.get_data.get_request_method(i)
        url = self.get_data.get_url(i)
        data = self.get_data.get_request_data_from_json(i)
        header = self.get_data.get_is_header(i)
        expect_result = self.get_data.get_expect_result(i)
        # 执行请求 , 获得的结果，list[0]为响应code, [1]为结果

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
        run_result = self.run_method.run_main(method, url, data, header)

        try:
            if self.com_util.is_contain(expect_result, run_result[1]):
                return json.loads(run_result[1])
            else:
                return False
        except Exception as e:
            print(e)

    # 通过 dependent 的key获取真实的 value内容
    def get_dependent_data_for_key(self, row):
        self.case_id = self.get_data.get_dependent_caseid(row)  # 获取case id
        denpendet_data = self.get_data.get_dependent_data(row)  # 获取 依赖上层的data key
        # print('dp data:' + denpendet_data)
        response_data = self._run_dependent_case()  # 运行依赖
        # print('rs data : ' ,response_data)

        if not response_data:
            return False
        json_exe = parse(denpendet_data)
        madle = json_exe.find(response_data)

        arr0 = [math.value for math in madle][0]
        return arr0  # 获取 依赖data


if __name__ == '__main__':
    a = DependentData()
    r = a.get_dependent_data_for_key(8)
    import json
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
