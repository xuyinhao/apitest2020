import configparser
class GetConf():
    def __init__(self,conf_path=None):
        if conf_path:
            conf_path=conf_path
        else:
            conf_path="../conf/conf.ini"
        self.config=configparser.ConfigParser()
        self.config.read(conf_path)

    def read_conf_value_toexcel2(self,key):  #excel 请求变量，url里的变量
        return self.config.get("value",key)

    def read_conf_value_toexcel(self, key):  # excel 请求变量，url里的变量
        value_final=Exception
        value=None
        try:
            value = self.config.get("value", key)
            value_final=value
        except Exception as e :
            try:        # 如果第一个配置没有找到变量，则查找valueauto配置项
                valueauto = self.config.get("valueauto", key)  # 会把响应的变量值，自动填充进来
                value_final=valueauto
            except Exception as e:
                return Exception
            pass

        if value:   #如果第一个value配置项找到了变量，检查一下第二个配置项是否存在配置变量
            try:  # 以最新的valueauto配置项
                valueauto = self.config.get("valueauto", key)  # 会把响应的变量值，自动填充进来
                value_final = valueauto
            except Exception as e:
                pass
                #异常，则跳过。
                #如果第二个配置valueauto也有配置变量则更新value_final值
        return value_final

    def read_section(self):
        print(self.config.sections())
if __name__ == '__main__':
    ff=GetConf()
    print(ff.read_conf_value_toexcel("username"))
    # ff.read_section()