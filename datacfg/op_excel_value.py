'''
把excel里的变量替换成真实的值
把excel提取的值进行保存
'''
from datacfg.get_conf import GetConf
from utils.common_util import CommonUtil
import json
import traceback
from configparser import NoOptionError

class OpValue():
    def __init__(self):
        self.getcfg = GetConf()
        self.comtool = CommonUtil()

    # 传递含有变量的信息，进行替换 变量值
    def replace_value(self, data):
        # data = {"sourceType": "0", "userName": "${userName}$", "password": "${password}$"}
        # data = {"sourceType": "0", "userName": "${userName2}$", "password": "${password}$"}
        nn = self.comtool.res_find(str(data))  ##找到所有变量
        data_ret=data

        for key in nn:
            try:
                getv = self.getcfg.read_conf_value_toexcel(key)  # 获取key的值
                data_ret = self.comtool.res_value_replace(key, getv, str(data_ret))  # 替换data的赋值给data_ret
            except Exception as e:
                print("替换excel的变量失败，跳过替换。",e)
                pass



        return str(data_ret).replace("'",'"')

    def save_value(self):
        pass


if __name__ == '__main__':
    f = OpValue()
    print(str(f.replace_value()))
