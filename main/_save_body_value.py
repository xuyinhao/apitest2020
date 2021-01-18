"""
保存响应体中，需要保存的值
"""
from  datacfg.get_conf import GetConf
import json
class SaveBodyValue():

    '''
    从响应体中，保存需要被保存的变量到conf.ini文件里
    '''
    def __init__(self):
        self.getconf=GetConf()

    def save_value_to_conf(self,save_body_value, current_result):
        current_result=json.loads(current_result)
        print(type(current_result))
        print(current_result[save_body_value])
        pass
if __name__ == '__main__':
    sbv=SaveBodyValue()
    key="key1"
    value="data[0]"
    current_result='{"data":["aaaa","bbb"]}'
    # sbv.save_value_to_conf(value,current_result)
    