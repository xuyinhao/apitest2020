'''
    基本的 通用的工具 方法 存放位置
'''
import re,json
import jmespath
from base.LogUtil import my_log
log=my_log(__file__)

class CommonUtil():
    def is_contain(self, str_src, str_dst):
        flag = False
        if str(str_src) in str(str_dst):
            flag = True
        else:
            return flag
        return flag

    ##读取excel如果是 .0 结尾就去掉 .0)
    def value_trans(self, value):
        if isinstance(value, float):
            value = int(value)
        return value


    #正则找到所有变量
    def res_find(self,data,pattern_data=None):
        if not pattern_data:
            pattern_data = '\${(.*?)}\$'

        pattern = re.compile(pattern_data)
        re_res=pattern.findall(data)
        return re_res
    #正则替换变量
    def res_value_replace(self,pattern_data,replace,data):
        return re.sub("\${%s}\$"%pattern_data,replace,data)

    #提取json内容
    def json_search(self,json_re,json_content):
        '''
        :param json_re:
        :param json_content:  需要双引号的字符串
        :return: [list] json_search_value
        '''

        if not isinstance(json_content,dict):
            json_content=json.loads(json_content)

        json_search_value=jmespath.search(json_re,json_content)
        return json_search_value


if __name__ == '__main__':
    r = CommonUtil()
    # a = {
    #     "mobile": "17606119611",
    #     "username": "3中文",
    #     "password":"123",
    #     "data":[{"name":"n1","value":"v1"},{"name":"n2","value":"v2"}]
    # }
    #
    #
    # print(int(r.value_trans(17606119611.0)))
    # m='{"sourceType":"0","userName":"${userName}$","password":"${password}$"}'
    # nn=r.res_find(str(m))
    # print(r.res_value_replace(nn[0],"user1",str(m)))
    # print(r.json_search('data[0].name', a))  # json 提取

    value = "data[0]"
    current_result = '{"data":"foo","nn":"a"}'
    print(r.json_search(value,current_result))