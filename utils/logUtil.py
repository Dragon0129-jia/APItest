import datetime
import logging
import os.path

from config.config import ConfigYaml, get_log

#定义日志级别的映射
log_l={
    "info": logging.INFO,
    "debug": logging.DEBUG,
    "warning": logging.WARNING,
    "error": logging.ERROR
}

class Logger:
    def __init__(self,log_file,log_name,lgo_level):
        self.log_file=log_file
        self.loog_name=log_name
        self.log_level=lgo_level

        self.loger = logging.getLogger(self.loog_name)
        # 2、设置log级别
        self.loger.setLevel(log_l[self.log_level])
        if not self.loger.handlers:
            #输出控制台
            fh_stream = logging.StreamHandler()
            fh_stream.setLevel(log_l[self.log_level])
            formatter = logging.Formatter('%(asctime)s%(name)s%(levelname)s%(message)s')
            fh_stream.setFormatter(formatter)
            #写入控制台
            fh_file = logging.FileHandler(self.log_file)
            fh_file.setLevel(log_l[self.log_level])
            fh_file.setFormatter(formatter)
            # 6、添加hedler
            self.loger.addHandler(fh_stream)
            self.loger.addHandler(fh_file)


#log目录
log_path=get_log()
#获取当前时间
corenttime = datetime.datetime.now().strftime("%Y-%m-%d")
#获取日志扩展名
extension = ConfigYaml().get_conf_log_extension()
logfile=os.path.join(log_path,corenttime+extension)
#日志级别
loglevel=ConfigYaml().get_cong_log_level()
# print(loglevel)

def my_log(logname=__file__):
    return Logger(log_file=logfile,log_name=logname,lgo_level=loglevel).loger

if __name__ == '__main__':
    my_log().debug("this is debug")