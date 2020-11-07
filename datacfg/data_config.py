class global_var():
    # 定义case 的列 id . openpyxl 从1开始
    var_arr = []       #1   2          3        4        5      6          7
    var_arr = ["NULL","ID","modname","apiname","url","isrun","method","cookie",
               "header","dependent_caseid","dependent_data",        #8 9 10
               "dependent_filed","request_data","save_value","expect_result", "expect_code" ,  #11 12 13 14 15
               "dbcheck","current_result","current_code","test_result","comment"]    # 16 17 18 19 20



# 函数
def get_id_col():
    return global_var.var_arr.index("ID")

#获取url列id
def get_url_col():
    return global_var.var_arr.index("url")
#获取模块名称的列id
def get_modname_col():
    return  global_var.var_arr.index("modname")
#获取接口名称的列id
def get_apiname_col():
    return global_var.var_arr.index("apiname")
#获取是否运行的列id
def get_run_col():
    return global_var.var_arr.index("isrun")

#获取请求方式的列id
def get_request_method_col():
    return global_var.var_arr.index("method")

#获取是否携带cookie的id
def get_cookie_col():
    return global_var.var_arr.index("cookie")

#获取请求头的列id
def get_header_col():
    return global_var.var_arr.index("header")

# #不常用，暂时header 写死
def get_header_info():
    header_info = {
               "User-Agent":"Mozilla/5.5 (Windows NT 10.0; Win64; x64) AppleWebKit/555.55 (KHTML, like Gecko) Chrome/55.5.555.555 Safari/555.55 Edge/55.55555"}
    return header_info

#获取case 依赖某条case的列id
def get_dependent_caseid_col():
    return global_var.var_arr.index("dependent_caseid")

#获取依赖数据的列id
def get_dependent_data_col():
    return global_var.var_arr.index("dependent_data")

#获取填充依赖的id
def get_dependent_filed_col():
    return global_var.var_arr.index("dependent_filed")

#获取请求数据的列id
def get_request_data_col():
    return global_var.var_arr.index("request_data")

#获取保存响应值的列id
def get_save_value_col():
    return global_var.var_arr.index("save_value")
#预期结果
def get_expect_result_col():
    return global_var.var_arr.index("expect_result")
#预期响应
def get_except_code_col():
    return global_var.var_arr.index("expect_code")

#实际结果
def get_current_result_col():
    return global_var.var_arr.index("current_result")
#实际响应
def get_current_code_col():
    return global_var.var_arr.index("current_code")
#数据库验证语句 TODO
def get_dbcheck_col():
    return  global_var.var_arr.index("dbcheck")

#执行结果
def get_test_result_col():
    return global_var.var_arr.index("test_result")

#获取备注
def get_comment_col():
    return global_var.var_arr.index("comment")
if __name__ == '__main__':
    print(get_id_col())


