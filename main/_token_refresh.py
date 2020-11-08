'''
重新获取token，cookies使用
需要根据实际情况进行修改
'''
from utils.common_util import CommonUtil
from datacfg.get_dependent_data import DependentData
from base.LogUtil import my_log
log=my_log(__file__)

#check_token_exception
class TokenCheck():

    TOKEN_NOT_OK_VALUE = "Token parsing exception"
    TOKEN_NOT_OK_VALUE2 = "请求token失效"
    COOKIE_NOT_OK_VALUE =""
    SUCCESS_LOGIN_CASE_ID = "login_01"

    def __init__(self):
        self.depent_data = DependentData()
        self.comtool = CommonUtil()

    ##适配 .响应body 里包含了 失效的文字，则重新获取token
    def check_token_exception(self, response_body):
        if self.comtool.is_contain(TokenCheck.TOKEN_NOT_OK_VALUE,str(response_body) )\
                or self.comtool.is_contain( TokenCheck.TOKEN_NOT_OK_VALUE2,str(response_body)) :
            print("token失效了,重新获取")
            if self.__reget_token():
                print("重新获取token成功")
                return True
            return False
            ##
        return False

    def __reget_token(self, loginid=None):
        if not loginid:
            loginid = TokenCheck.SUCCESS_LOGIN_CASE_ID
        #重新执行，获取token接口
        ret = self.depent_data.force_runcase_by_caseid(loginid, token=True)
        return ret

