import json


# json_data = json.load(open("../datacfg/login.json"))
# print(json_data["login"])

class OperationJson():
    def __init__(self, file_name=None):
        if file_name:
            self.file_name = file_name
        else:
            self.file_name = "../data/login.json"

    # 获取json句柄 对象 文件
    def __get_file_data(self):
        with open(self.file_name, encoding='utf-8') as fp:
            json_data = json.load(fp)
            return json_data

    # 通过key 获取value
    def get_value(self, key):
        json_data = self.__get_file_data()
        return json_data[key]


if __name__ == '__main__':
    r = OperationJson()
    print(r.get_value('login'))
