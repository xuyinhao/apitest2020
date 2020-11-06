import configparser
class GetConf():
    def __init__(self,conf_path=None):
        if conf_path:
            conf_path=conf_path
        else:
            conf_path="../conf/conf.ini"
        self.config=configparser.ConfigParser()
        self.config.read(conf_path)

    def read_conf_value_toexcel(self,key):  #excel 请求变量，url里的变量
        return self.config.get("value",key)

    def read_section(self):
        print(self.config.sections())
if __name__ == '__main__':
    ff=GetConf()
    ff.read_conf_value_toexcel("username")
    # ff.read_section()