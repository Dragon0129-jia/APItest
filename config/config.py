#1、获取当前绝对路径
import os


from utils.YamlUtil import YamlReader

abspath = os.path.abspath(__file__)
# print(abspath)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# print(path)
_config_path=BASE_DIR+os.sep+"config"
_config_file=_config_path+os.sep+"config.yml"
# print(_config_file)
_log_path=BASE_DIR+os.sep+"logs"
def get_config_path():
    return _config_path
def get_config_file():
    return _config_file
def get_log():
    return _log_path
#2、读取配置文件
class ConfigYaml:
    def __init__(self):
        self.config=YamlReader(get_config_file()).data()
    def get_conf_file(self):
        return self.config["Base"]["test"]["url"]
    def get_cong_log_level(self):
        """
        获取日志级别
        :return:
        """
        return self.config["Base"]["log_level"]
    def get_conf_log_extension(self):
        """
        获取日志扩展名
        :return:
        """
        return  self.config["Base"]["log_extension"]

if __name__ == '__main__':
    conf = ConfigYaml()
    # result = conf.get_conf_file()
    # print(result)
    extension = conf.get_conf_log_extension()
    level = conf.get_cong_log_level()
    print(extension,level)
    print(get_log())