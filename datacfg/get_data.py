from utils.operation_excel import OperationExcel
from datacfg import data_config,op_excel_value
from datacfg.get_conf import GetConf
from utils.operation_json import OperationJson
from utils.common_util import CommonUtil
import json

class GetData():
    def __init__(self, filename=None, sheet_id=None):
        self.opera_excel = OperationExcel(filename, sheet_id)
        self.com_util = CommonUtil()
        self.op_excel_value=op_excel_value.OpValue()
        self.get_conf=GetConf()

    def trans_value(self, v):
        return self.com_util.value_trans(v)

    # 获取当前 sheet name
    def get_current_sheet_name(self):
        return self.trans_value(self.opera_excel.get_sheet_name())

    # 获取excel行数
    def get_case_lines(self):
        return self.trans_value(self.opera_excel.get_sheet_rows_num())

    # 通过caseidname 获取行号
    def get_case_row_by_idname(self, idname):
        col_num = 1
        for i in self.opera_excel.get_col_value(1):
            if idname == i:
                return col_num
            col_num += 1
        return False

    # 获取case id
    def get_case_id_name(self, row):
        col = data_config.get_id_col()
        case_id = self.opera_excel.get_cell_value(row, col)
        if case_id:
            return self.trans_value(case_id)
        else:
            return ""

    #获取模块名称
    def get_mod_name(self,row):
        col=data_config.get_modname_col()
        modname=self.opera_excel.get_cell_value(row,col)
        return self.trans_value(modname)
    #获取api接口名称
    def get_apiname(self,row):
        col=data_config.get_apiname_col()
        apiname=self.opera_excel.get_cell_value(row,col)
        return self.trans_value(apiname)

    #获取url 请求地址
    def get_url(self, row):
        col = data_config.get_url_col()
        url = self.opera_excel.get_cell_value(row, col)
        if url:
            return self.trans_value(url)
        else:
            return ""
    def get_url_final(self,row):
        url=self.get_url(row)
        if url:
            url = str(self.get_conf.read_conf_value_toexcel("urlprefix")).replace('"','') + str(url)
        return url

    # 是个否运行
    def get_is_run(self, row):
        flag = None
        col = data_config.get_run_col()
        is_run = self.opera_excel.get_cell_value(row, col)
        if str(is_run).lower() == "yes" or str(is_run).lower() == "y":
            flag = True
        else:
            flag = False
        return self.trans_value(flag)

    # 获取请求的方式
    def get_request_method(self, row):
        col = data_config.get_request_method_col()
        method = self.opera_excel.get_cell_value(row, col)
        return self.trans_value(method)

    #获取 cookie值
    def get_is_cookie(self,row):
        col = data_config.get_cookie_col()
        is_cookie = self.opera_excel.get_cell_value(row,col)
        return self.trans_value(is_cookie)

    # # 是否携带 header
    # def get_is_header(self, row):
    #     col = data_config.get_header_col()
    #     is_header = self.opera_excel.get_cell_value(row, col)
    #     if str(is_header).lower() == "yes":
    #         return self.trans_value(data_config.get_header_info())
    #     else:
    #         return None

    ##获取header值
    def get_header_info(self,row):
        col=data_config.get_header_col()
        headerinfo=self.opera_excel.get_cell_value(row,col)
        if str(headerinfo) != "" or str(headerinfo) != None:
            return json.loads(headerinfo)
        else:
            return None

    # 获取 dependent caseid name
    def get_dependent_caseid(self, row):
        col = data_config.get_dependent_caseid_col()
        caseid = self.opera_excel.get_cell_value(row, col)
        if caseid == "":
            return None
        else:
            return caseid

    # 获取dependent data 内容
    def get_dependent_data(self, row):
        col = data_config.get_dependent_data_col()
        dependent_data = self.opera_excel.get_cell_value(row, col)
        return dependent_data

    # 获取depent  filed字段内容
    def get_dependent_filed(self, row):
        col = data_config.get_dependent_filed_col()
        filed_data = self.opera_excel.get_cell_value(row, col)
        return filed_data

    # 获取请求数据
    def get_request_data(self, row):
        col = data_config.get_request_data_col()
        data = self.opera_excel.get_cell_value(row, col)
        if data == "":
            return None

        return self.trans_value(data)

    # 通过关键字拿到 request_data数据
    def get_request_data_final(self, row):
        request_data = self.get_request_data(row)       #请求数据，关键字

        if str(request_data).startswith("json_"):       #如果json_开头则进行json获取
            opera_json = OperationJson()
            request_data = opera_json.get_value(request_data)
            return self.trans_value(request_data)
        elif str(request_data) != "" :
            request_data = self.op_excel_value.replace_value(request_data)  # 更新替换excel请求中带的变量
            return self.trans_value(request_data)       #如果不为空，不是json_开头，那么就替换变量再返回数据
        else:
            return None                  #没有请求数据，则返回None

    #保存响应中的指定值（json获取方式）
    def get_save_value(self,row):
        col=data_config.get_save_value_col()
        savevalue = self.opera_excel.get_cell_value(row,col)
        if str(savevalue) != "" or str(savevalue) != None:
            return str(savevalue)
        else:
            return None

    # 获取预期响应结果
    def get_expect_result(self, row):
        col = data_config.get_expect_result_col()
        expect_value = self.opera_excel.get_cell_value(row, col)
        if expect_value == "":
            return None
        return self.trans_value(expect_value)

    #获取预期响应code
    def get_expect_code(self, row):
        col = data_config.get_except_code_col()
        expect_code = self.opera_excel.get_cell_value(row, col)
        if expect_code == "":
            return 200
        return self.trans_value(expect_code)

    #获取数据库校验语句
    def get_dbcheck_sql(self,row):
        col =data_config.get_dbcheck_col()
        dbchecksql=self.opera_excel.get_cell_value(row,col)
        if str(dbchecksql) != "" or str(dbchecksql) != None:
            return str(dbchecksql)
        else:
            return None

    #获取备注信息
    def get_comment_info(self,row):
        col=data_config.get_comment_col()
        commentinfo = self.opera_excel.get_cell_value(row,col)
        if str(commentinfo) != "" or str(commentinfo) != None:
            return str(commentinfo)
        else:
            return ""

    # 判断是否需要 依赖case
    def get_is_dependent(self,row):
        data = self.get_dependent_caseid(row)
        if data:
            return True
        else:
            return False


    #写 当前结果到excel
    def write_current_result(self, row, value):
        col = data_config.get_current_result_col()
        writevalue = self.opera_excel.write_cell_value(row, col, value)
        if writevalue:
            return True
        else:
            return False

    #写 当前响应到excel
    def write_current_code(self,row,value):
        col=data_config.get_current_code_col()
        writevalue = self.opera_excel.write_cell_value(row,col,value)
        if writevalue:
            return True
        else:
            return False

    #写 测试结果到excel
    def write_test_result(self, row, value):
        col = data_config.get_test_result_col()
            ## row,col,value,result(通过value来判断pass,fail,else 用于写不同的颜色)
        writevalue = self.opera_excel.write_cell_value(row, col, value,result=value)
        if writevalue:
            return True
        else:
            return False


if __name__ == '__main__':
    ab = GetData()
    print(ab.get_request_data_final(3))
    print(ab.get_request_data(2))
    # print(ab.get_expect_result(2))
    # print(ab.get_case_row_by_idname('login_01'))
