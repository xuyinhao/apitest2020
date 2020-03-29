from utils.operation_excel import OperationExcel
from datacfg import data_config
from utils.operation_json import OperationJson
from utils.common_util import CommonUtil


class GetData():
    def __init__(self, filename=None, sheet_id=None):
        self.opera_excel = OperationExcel(filename, sheet_id)
        self.com_util = CommonUtil()

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
        return self.trans_value(case_id)

    # 获取url
    def get_url(self, row):
        col = data_config.get_url_col()
        url = self.opera_excel.get_cell_value(row, col)
        return self.trans_value(url)

    # 是个否运行
    def get_is_run(self, row):
        flag = None
        col = data_config.get_run_col()
        is_run = self.opera_excel.get_cell_value(row, col)
        if str(is_run).lower() == "yes":
            flag = True
        else:
            flag = False
        return self.trans_value(flag)

    # 获取请求的方式
    def get_request_method(self, row):
        col = data_config.get_request_method_col()
        method = self.opera_excel.get_cell_value(row, col)
        return self.trans_value(method)

    # 是否携带 header
    def get_is_header(self, row):
        col = data_config.get_header_col()
        is_header = self.opera_excel.get_cell_value(row, col)
        if str(is_header).lower() == "yes":
            return self.trans_value(data_config.get_header_col())
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

    # 获取depent filed字段内容
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
    def get_request_data_from_json(self, row):
        opera_json = OperationJson()
        request_data = opera_json.get_value(self.get_request_data(row))
        return self.trans_value(request_data)

    # 获取预期结果
    def get_expect_result(self, row):
        col = data_config.get_expect_result_col()
        expect_value = self.opera_excel.get_cell_value(row, col)
        if expect_value == "":
            return None
        return self.trans_value(expect_value)

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

    #写 测试结果到excel
    def write_test_result(self, row, value):
        col = data_config.get_test_result_col()
        writevalue = self.opera_excel.write_cell_value(row, col, value)
        if writevalue:
            return True
        else:
            return False


if __name__ == '__main__':
    ab = GetData()
    print(ab.get_request_data_from_json(2))
    print(ab.get_request_data(2))
    print(ab.get_expect_result(2))
    print(ab.get_case_row_by_idname('id01'))
