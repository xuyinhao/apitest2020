class global_var():
    # 定义case 的列 id . openpyxl
    var_arr = []       #1   2       3   4       5
    var_arr = ["NULL","ID","url","run","method","cookie",
               "header","dependent_caseid","dependent_data",        #6  7   8
               "dependent_filed","request_data","expect_result",    #9  10  11
               "current_result","test_result"]                      #12 13


def get_id_col():
    return global_var.var_arr.index("ID")


def get_url_col():
    return global_var.var_arr.index("url")


def get_run_col():
    return global_var.var_arr.index("run")


def get_request_method_col():
    return global_var.var_arr.index("method")

def get_cookie_col():
    return global_var.var_arr.index("cookie")

def get_header_col():
    return global_var.var_arr.index("header")

#不常用，暂时header 写死
def get_header_info():
    header_info = {
               "User-Agent":"Mozilla/5.5 (Windows NT 10.0; Win64; x64) AppleWebKit/555.55 (KHTML, like Gecko) Chrome/55.5.555.555 Safari/555.55 Edge/55.55555"}
    return header_info


def get_dependent_caseid_col():
    return global_var.var_arr.index("dependent_caseid")


def get_dependent_data_col():
    return global_var.var_arr.index("dependent_data")


def get_dependent_filed_col():
    return global_var.var_arr.index("dependent_filed")


def get_request_data_col():
    return global_var.var_arr.index("request_data")


def get_expect_result_col():
    return global_var.var_arr.index("expect_result")


def get_current_result_col():
    return global_var.var_arr.index("current_result")


def get_test_result_col():
    return global_var.var_arr.index("test_result")

