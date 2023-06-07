#创建类
#判断文件是否存在
import os

import yaml

class YamlReader:

   def __init__(self,yaml):
       if os.path.exists(yaml):
        self.yaml=yaml
       else:
           raise FileNotFoundError("文件不存在")
       self._data=None
       self._data_all=None
   def data(self):
        if not self._data:
            with open(self.yaml,"rb") as f:
                self._data = yaml.safe_load(f)
        return self._data

   def data_all(self):
       if not self._data_all:
           with open(self.yaml, "rb") as f:
               self._data_all = list(yaml.safe_load_all(f))
       return self._data_all






