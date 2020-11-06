'''
    基本的 通用的工具 方法 存放位置
'''
import re
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


if __name__ == '__main__':
    r = CommonUtil()
    a = {
        "mobile": "17606119611",
        "username": "3中文"
    }

    print(int(r.value_trans(17606119611.0)))
    m={"sourceType":"0","userName":"${userName}$","password":"${password}$"}
    nn=r.res_find(str(m))
    print(r.res_value_replace(nn[0],"user1",str(m)))