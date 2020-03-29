class global_var():
    # 定义case 的列 id xlrd
    # ID = 0
    # url = 1
    # run = 2
    # method = 3
    # header = 4
    # case_depend = 5
    # data_depend = 6
    # filed_depend = 7
    # request_data = 8
    # expect_result = 9
    # current_result = 10
    # test_result = 11
    # # openpyxl 是从1开始计算的
    ID = 1
    url = 2
    run = 3
    method = 4
    header = 5
    dependent_caseid = 6
    dependent_data = 7
    dependent_filed = 8
    request_data = 9
    expect_result = 10
    current_result = 11
    test_result = 12


def get_id_col():
    return global_var.ID


def get_url_col():
    return global_var.url


def get_run_col():
    return global_var.run


def get_request_method_col():
    return global_var.method


def get_header_col():
    return global_var.header


def get_header_value():
    pass


def get_dependent_caseid_col():
    return global_var.dependent_caseid


def get_dependent_data_col():
    return global_var.dependent_data


def get_dependent_filed_col():
    return global_var.dependent_filed


def get_request_data_col():
    return global_var.request_data


def get_expect_result_col():
    return global_var.expect_result


def get_current_result_col():
    return global_var.current_result


def get_test_result_col():
    return global_var.test_result
