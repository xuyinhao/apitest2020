'''
    基本的 通用的工具 方法 存放位置
'''

class CommonUtil():
    def is_contain(self, str_src, str_dst):
        flag = False
        if str(str_src) in str(str_dst):
            flag = True
        else:
            return flag
        return flag

    def value_trans(self, value):
        if isinstance(value, float):
            value = int(value)
        return value


if __name__ == '__main__':
    r = CommonUtil()
    a = {
        "mobile": "17606119611",
        "username": "3中文"
    }

    print(int(r.value_trans(17606119611.0)))
