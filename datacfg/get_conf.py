import configparser
import traceback
#不可以导LogUtil
class GetConf():
    EXCEL_MANUAL_VALUE = "value"  # 用户自己配置的变量
    EXCEL_AUTO_VALUE = "valueauto"  # 通过case请求保存的变量 存放的位置

    def __init__(self, conf_path=None):
        if conf_path:
            self.conf_path = conf_path
        else:
            self.conf_path = "../conf/conf.ini"
        self.config = configparser.ConfigParser()
        # self.config.read(self.conf_path,encoding='utf-8')

    def read_value(self, section, key):
        self.config.read(self.conf_path, encoding='utf-8')
        return self.config.get(section, key)

    def read_conf_value_toexcel2(self, key):  # excel 请求变量，url里的变量
        self.config.read(self.conf_path, encoding='utf-8')
        return self.config.get(GetConf.EXCEL_MANUAL_VALUE, key)

    def read_conf_value_toexcel(self, key):  # excel 请求变量，url里的变量
        self.config.read(self.conf_path, encoding='utf-8')
        value_final = Exception
        value = None
        try:
            value = self.config.get(GetConf.EXCEL_MANUAL_VALUE, key)
            value_final = value
        except Exception as e:
            try:  # 如果第一个配置没有找到变量，则查找valueauto配置项
                valueauto = self.config.get(GetConf.EXCEL_AUTO_VALUE, key)  # 会把响应的变量值，自动填充进来
                value_final = valueauto
            except Exception as e:
                return Exception
            pass

        if value:  # 如果第一个value配置项找到了变量，检查一下第二个配置项是否存在配置变量
            try:  # 以最新的valueauto配置项
                valueauto = self.config.get(GetConf.EXCEL_AUTO_VALUE, key)  # 会把响应的变量值，自动填充进来
                value_final = valueauto
            except Exception as e:
                pass
                # 异常，则跳过。
                # 如果第二个配置valueauto也有配置变量则更新value_final值
        return value_final

    def read_section(self):
        self.config.read(self.conf_path, encoding='utf-8')
        return self.config.sections()

    # 创建section
    def create_section(self, section_name=None):
        self.config.read(self.conf_path, encoding='utf-8')
        if not section_name:
            section_name = GetConf.EXCEL_AUTO_VALUE

        if section_name not in self.read_section():
            print("add section", section_name)
            self.config.add_section(section_name)
            self.config.write(open(self.conf_path, 'w'))
        return True

    # 写key,value值
    def write_conf_value(self, key, value, section_name=EXCEL_AUTO_VALUE):
        self.config.read(self.conf_path, encoding='utf-8')
        self.create_section(section_name)
        try:
            self.config.set(section_name, key, value)
        except Exception as e:
            traceback.print_exc()
            return False
        try:
            with open(self.conf_path, 'w+',encoding='utf-8') as f:
                self.config.write(f)
                f.flush()

        except ValueError as e:
            raise e
        return True


if __name__ == '__main__':
    ff = GetConf()
    print(ff.read_conf_value_toexcel("username"))
    # ff.read_section()
    print(ff.read_conf_value_toexcel("nnn"))
    print(ff.write_conf_value("nnn", 'vvv2v2'))
    print(ff.read_conf_value_toexcel("nnn"))

