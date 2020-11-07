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
from utils.operation_token import OperationToken
from main._token_refresh import TokenCheck
from main._save_body_value import SaveBodyValue
import json
import traceback

class RunTest():
    def __init__(self):
        self.run_method = RunMethod()
        self.get_data = GetData()
        self.com_util = CommonUtil()
        self.send_mail = SendMail()
        self.op_cookie = OperationCookie()
        self.op_token = OperationToken()
        self.token_check=TokenCheck()
        self.save_body_values = SaveBodyValue
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
            #获取row 测试相关信息
            try:
                method = self.get_data.get_request_method(i)
                url = self.get_data.get_url_final(i)
                data = self.get_data.get_request_data_final(i)
             #@  header = self.get_data.get_is_header(i)   #获取的 header的值
                header = self.get_data.get_header_info(i)  #获取的 header的值
                is_cookie = self.get_data.get_is_cookie(i)  #获取cookie\token相关信息 进行cookie或者token处理
                expect_result = self.get_data.get_expect_result(i)  #获取期望的结果（包含的内容）
                expect_code = self.get_data.get_expect_code(i)  #获取期望的code
                    # save_body_value -- {"user1":".data.records[0].name"}
                save_body_value = self.get_data.get_save_value(i)   #获取需要保存的key,value
                # 判断是否有 依赖，如果有 就进行依赖case的测试。如果没有就 直接进行 该api基本测试
                # dp_caseid = self.get_data.get_dependent_caseid(i)
                is_dependent = self.get_data.get_is_dependent(i)
            except Exception as  e:
                print("----Has some error : ",traceback.print_exc())
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

            #处理cookie : wc更新cookies,yc携带cookies ,nc不需要cookies
            if is_cookie == "wc":   #需要更新cookies,通过响应值获取ck
                run_response_data = self.run_method.run_main(method,url, data=data, header=header)
                op_cookie = OperationCookie()
                cookie_value  = op_cookie.trans_response_cookie_value(run_response_data[2])
                op_cookie.write_cookie(cookie_value)
            elif is_cookie == "yc":
                # self.op_cookie.get_cookie('loongaio')
                cookie = self.op_cookie.get_cookie_file_data()
                cookie = json.loads(cookie)
                run_response_data = self.run_method.run_main(method, url, data=data, cookie=cookie, header=header)
            elif is_cookie == "nc":
                run_response_data = self.run_method.run_main(method, url, data=data,header=header)
            # 处理token
            elif is_cookie == "wt": #需要更新token,通过响应值获取token
                run_response_data = self.run_method.run_main(method, url, data=data, header=header)
                # print("#$$# :",str(run_response_data))
                op_token=OperationToken()
                token_value=op_token.trans_response_token_value_by_body(run_response_data[2])
                op_token.write_token(token_value)
            elif is_cookie == "yt":
                token=self.op_token.get_token()
                header["token"]=token           ##根据当前web系统适当调整，这里的token是加在header
                run_response_data = self.run_method.run_main(method, url, data=data, header=header)
                if self.token_check.check_token_exception(run_response_data):
                    token = self.op_token.get_token()
                    header["token"] = token  ##根据当前web系统适当调整，这里的token是加在header
                    run_response_data = self.run_method.run_main(method, url, data=data, header=header)
            else:   #其他值，则不需要token和cookies
                run_response_data = self.run_method.run_main(method, url, data=data, header=header)



            # 执行请求 , 获得的结果，list[0]为响应code, [1]为结果 , [2] 为 response 本身。 把当前 实际结果写到excel
            current_code=str(run_response_data[0])
            current_result=str(run_response_data[1])
            self.get_data.write_current_result(i, current_result)
            self.get_data.write_current_code(i,current_code)


            try:
                #判断case成功
                if self.com_util.is_contain(expect_result, current_result)\
                        and str(expect_code) == str(current_code):
                    print('----pass')
                    self.pass_count.append(i)
                    self.get_data.write_test_result(i, 'pass')

                # 成功后，检查是否有需要保存的变量和需要正则获取的值（json）
                if save_body_value:
                    print("##get 需要保存值", str(save_body_value))
                    self.save_body_values.save_value_to_conf(save_body_value, current_result)

                ##判断case失败
                else:
                    print('----fail')
                    self.fail_count.append(i)
                    self.get_data.write_test_result(i, 'fail')
            except Exception as e:
                print(traceback.print_exc())
        self._send_test_mail()      #输出结果，并发送邮件

    def _fail_row_info(self):
        f_arr = []
        for i in self.fail_count:
            r_info = '[' + self.get_data.get_current_sheet_name() + '] ' + 'Row: ' + str(i) + ', caseid : ' +\
                     self.get_data.get_case_id_name(i) + ', Url : ' + self.get_data.get_url_final(i) + \
                     ", Comment : " +  self.get_data.get_comment_info(i)
            f_arr.append(r_info)
        return f_arr

    def _send_test_mail(self):

        passnum = len(self.pass_count)
        failnum = len(self.fail_count)
        breaknum = len(self.break_count)
        totalnum = passnum + failnum + breaknum
        result = "%.2f%%" %(passnum/totalnum*100)

        fm = [i for i in self._fail_row_info()]
        if fm:  #有失败时，打印信息
            content = "这次接口运行情况如下：\n 总计运行接口个数: %s 。通过: %s , 失败: %s , 中断: %s \n 通过百分比：%s  " \
                      "\n 失败接口如下：\n %s" %  \
                     (totalnum,passnum,failnum,breaknum,result,'\n '.join(fm))
        else:   #全部成功时，打印信息
            content = "这次接口运行情况如下：\n 总计运行接口个数: %s 。通过: %s , 失败: %s , 中断: %s \n 通过百分比：%s  " % \
                      (totalnum, passnum, failnum, breaknum, result)
        print(content)
        sub = "自动化测试邮件-api"

        sm = SendMail()
        # sm.send_mail("yellhao@sina.com",sub,content)



if __name__ == '__main__':
    a = RunTest()
    r = a.get_on_run()
