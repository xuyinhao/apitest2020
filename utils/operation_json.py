import json
import os

# json_data = json.load(open("../datacfg/login.json"))
# print(json_data["login"])

class OperationJson():
    def __init__(self, file_name=None):
        if file_name:
            self.file_name = file_name
        else:
            self.file_name = "../data/login.json"
        self.data = self.__get_file_data()

    # 获取json句柄 对象 文件
    def __get_file_data(self):
        if os.path.getsize(self.file_name) == 0 :
            with open(self.file_name,'w', encoding='utf-8') as fp:
                fp.write("{}")

        with open(self.file_name, encoding='utf-8') as fp:
            json_data = json.load(fp)
            return json_data

    # 通过key 获取value
    def get_value(self, key):
        json_data = self.__get_file_data()
        return json_data[key]

    #写cookie
    def write_data(self,value):
        with open(self.file_name,'w',encoding='utf-8') as fp:
            fp.write(json.dumps(value))
        # json_data[]=value
        return True
    #获取cookie
    def get_cookie(self):
        pass

    def get_all_value(self):
        with open(self.file_name,encoding='utf-8') as fp:
            value = fp.read()
        return value


if __name__ == '__main__':
    # r = OperationJson()
    # print(r.get_value('login'))
    r = OperationJson(file_name="../data/cookie.json")
    print(r.get_all_value())
    # r = OperationJson(file_name="../data/login.json")
    # r.write_cookie('{"aaa":"abcdefg"}')
    # print(r.get_all_value())