class global_var():
    # 定义case 的列 id . openpyxl
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
