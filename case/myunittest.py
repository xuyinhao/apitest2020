import unittest
from unittest import mock
from base.runhttp import RunMain
import time
from base.mock_demo import mock_def_test,mock_direct
import HTMLTestRunner
login_url = 'http://127.0.0.1:8000/login'
data = {'username': 'xyh', 'password': '123456'}

class TestMain(unittest.TestCase):
    def setUp(self):
        print('')
        run = RunMain()
        print('start--------------------- setUp')

    def tearDown(self):
        print('end-----------------------tearDown')
        time.sleep(0.2)

    def atest_001(self):
        run = RunMain('POST',login_url,data)
        print(run.results)

    def test_002(self):
    ##mock  - 一个类的方法
        mock_value={"abcmock":"mock"}
        r = RunMain()
        # r.run_main = mock.Mock(return_value=mock_value)
        run = r.run_main('POST',login_url,data)
        print(run)
        # self.assertIn('fail',str(run.results))
        #https://blog.csdn.net/weixin_34259159/article/details/93200873

        
    def test_003(self):
        run=RunMain()
        need_data={"hahamock":"abc"}
        res = mock_def_test(run.run_main,'POST',login_url,data,need_data)
        res2 = run.run_main('POST', login_url, data)
        print(res)
        # self.assertIn('fail',str(run.results))


    def test_mock(self):
        run = RunMain()

        need_data = {"need":"abc","abc":123}
        run.run_main = mock_direct(need_data)
        res = run.run_main('POST', login_url, data)
        print(res)


if __name__ == '__main__':
    unittest.main()

