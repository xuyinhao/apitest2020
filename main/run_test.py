import os,sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
parent_path = os.path.dirname(BASE_DIR)
sys.path.append(parent_path)

from base.runhttp import RunMethod
from datacfg.get_data import GetData
from utils.common_util import CommonUtil
from utils.send_mail import SendMail
from datacfg.get_dependent_data import DependentData
from utils.operation_cookie import OperationCookie
import json

class RunTest():
    def __init__(self):
        self.run_method = RunMethod()
        self.get_data = GetData()
        self.com_util = CommonUtil()
        self.send_mail = SendMail()
        self.op_cookie = OperationCookie()
        self.fail_count = []
        self.break_count=[]
        self.pass_count = []


    # 程序执行
    def get_on_run(self):

        print('执行Sheet : [', self.get_data.get_current_sheet_name(), ']')
        rows_count = self.get_data.get_case_lines()
        for i in range(2, rows_count + 1):  # 因为openpyxl是从1计数
            # 获取 测试的值
            is_run = self.get_data.get_is_run(i)
            if not is_run:
                print('Skip  case : ', self.get_data.get_case_id_name(i))
                self.get_data.write_test_result(i, 'Not run,skip case')
                continue  # 判断是否执行不执行，直接跳过
            print('Start case : ', self.get_data.get_case_id_name(i))
            try:
                method = self.get_data.get_request_method(i)
                url = self.get_data.get_url(i)
                data = self.get_data.get_request_data_from_json(i)
                header = self.get_data.get_is_header(i)   #获取的 header的值
                is_cookie = self.get_data.get_is_cookie(i)
                expect_result = self.get_data.get_expect_result(i)
                # 判断是否有 依赖，如果有 就进行依赖case的测试。如果没有就 直接进行 该api基本测试
                # dp_caseid = self.get_data.get_dependent_caseid(i)
                is_dependent = self.get_data.get_is_dependent(i)
            except Exception as  e:
                print("----Has some error : ",e)
                self.break_count.append(i)
                print('----break case')
                self.get_data.write_test_result(i, 'break'+str(e))
                continue

            if is_dependent:
                op = DependentData()
                dependent_response_data = op.get_dependent_data_for_key(i)
                if not dependent_response_data:  # 如果返回False, 就是依赖的case 失败了,那么这个例子也不用跑了
                    print('----fail , dependent return case fail')
                    self.get_data.write_test_result(i, 'fail, dependent case return  fail')
                    self.fail_count.append(i)
                    continue
                # print('run dp data get : ' + rs)
                filed_data = self.get_data.get_dependent_filed(i)   #获取 当前case 要被替换的字段内容
                data[filed_data] = dependent_response_data

            #处理cookie : write ,yes ,no
            if is_cookie == "write":
                run_response_data = self.run_method.run_main(method,url, data=data, header=header)
                op_cookie = OperationCookie()
                cookie_value  = op_cookie.trans_response_cookie_value(run_response_data[2])
                op_cookie.write_cookie(cookie_value)
            elif is_cookie == "yes":
                # self.op_cookie.get_cookie('loongaio')
                cookie = self.op_cookie.get_cookie_file_data()
                cookie = json.loads(cookie)
                run_response_data = self.run_method.run_main(method, url, data=data, cookie=cookie, header=header)
            else:
                run_response_data = self.run_method.run_main(method, url, data=data,header=header)

            # 执行请求 , 获得的结果，list[0]为响应code, [1]为结果 , [2] 为 response 本身。 把当前 实际结果写到excel
            self.get_data.write_current_result(i, str(run_response_data[1]))

            try:
                if self.com_util.is_contain(expect_result, run_response_data):
                    print('----pass')
                    self.pass_count.append(i)
                    self.get_data.write_test_result(i, 'pass')
                else:
                    print('----fail')
                    self.fail_count.append(i)
                    self.get_data.write_test_result(i, 'fail')
            except Exception as e:
                print(e)
        self._send_test_mail()

    def _fail_row_info(self):
        f_arr = []
        for i in self.fail_count:
            r_info = '[' + self.get_data.get_current_sheet_name() + '] ' + 'Row: ' + str(i) + ', caseid : ' +\
                     self.get_data.get_case_id_name(i) + ', Url : ' + self.get_data.get_url(i)
            f_arr.append(r_info)
        return f_arr

    def _send_test_mail(self):

        passnum = len(self.pass_count)
        failnum = len(self.fail_count)
        breaknum = len(self.break_count)
        totalnum = passnum + failnum + breaknum
        result = "%.2f%%" %(passnum/totalnum*100)

        fm = [i for i in self._fail_row_info()]
        content = "这次接口运行情况如下：\n 总计运行接口个数: %s 。通过: %s , 失败: %s , 中断: %s \n 通过百分比：%s  " \
                  "\n 失败接口如下：\n %s" %  \
                 (totalnum,passnum,failnum,breaknum,result,'\n '.join(fm))
        print(content)
        sub = "自动化测试邮件-api"

        sm = SendMail()
        # sm.send_mail("yellhao@sina.com",sub,content)



if __name__ == '__main__':
    a = RunTest()
    r = a.get_on_run()
