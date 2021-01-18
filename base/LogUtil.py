# coding:utf-8
"""
@author:yangyu
@time: 2020/01/06
@function： Logger封装类，使用一个方法解决日志打印
"""

import datetime,os,logging
# from config.Conf import ConfigYaml
# from config import Conf
from datacfg.get_conf import GetConf


#定义日志级别的映射
log_l = {
    "info": logging.INFO,
    "debug": logging.DEBUG,
    "warning": logging.WARNING,
    "error": logging.ERROR
}

class Logger():


    def __init__(self,logs_file=None,logs_name=None,logs_level=None):
        get_conf = GetConf()
        log_path = get_conf.read_value('common', 'logpath')     ## 日志文件名称 = logs目录 + 当前时间+扩展名
        current_time = datetime.datetime.now().strftime("%Y-%m-%d")
        logfile_loc = os.path.join(log_path, current_time + ".log")
        loglevel_loc = get_conf.read_value('common', 'loglevel')
        self.log_file=logfile_loc
        self.log_level=loglevel_loc
        self.log_name=__file__
        if logs_file:
            self.log_file = logs_file #扩展名 配置文件
        if logs_name:
            self.log_name = logs_name #参数
        if logs_level:
            self.log_level = logs_level # 配置文件

        # 设置logger名称
        self.logger = logging.getLogger(self.log_name)
        # 设置log级别
        self.logger.setLevel(log_l[str(self.log_level).lower()]) #logging.INFO
        #判断handlers是否存在
        if not self.logger.handlers:
            # 输出控制台
            fh_stream = logging.StreamHandler()
            fh_stream.setLevel(log_l[self.log_level])
            #日志格式
            formatter = logging.Formatter('%(asctime)s %(name)s line:%(lineno)s [%(levelname)s]:%(message)s ')
            fh_stream.setFormatter(formatter)
            # 写入文件 utf-8 防止中文乱码
            fh_file = logging.FileHandler(self.log_file,encoding="utf-8")
            fh_file.setLevel(log_l[self.log_level])
            fh_file.setFormatter(formatter)

            # 添加handler
            self.logger.addHandler(fh_stream)
            self.logger.addHandler(fh_file)

# print(loglevel)
def my_log(log_name = __file__):
    return Logger(logs_name=log_name).logger

if __name__ == "__main__":
    my_log().debug("this is a debug")
    my_log().info("this is info")
    my_log(log_name="abcd").info("aaaa")
    my_log().info("222info")