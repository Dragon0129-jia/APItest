#创建类
#判断文件是否存在
import os

import yaml

from testcase.t_yaml.yaml_Demo import path


class YamlReader:

   def __init__(self):
       self.path=path
       self.data=None
   def reader(self):
        with open(self.path,"r",encoding="utf-8") as f:
            self.data = yaml.safe_load(f)
        return self.data


if __name__ == '__main__':
    print(YamlReader().reader())




