from unittest import mock


# 模拟mock封装
# run.run_main,'GET',login_url,data,"abc"
def mock_def_test(funcname, method, url, data, response_data):
    mock_data = mock.Mock(return_value=response_data)
    func = mock_data(method, url, data)
    return func


def mock_direct(response_data):
    mock_data = mock.Mock(return_value=response_data)
    return mock_data
