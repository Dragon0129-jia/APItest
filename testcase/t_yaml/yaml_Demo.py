import os

import yaml

from utils.YamlUtil import YamlReader

#读取单个文档
# with open("data.yaml", "r", encoding="utf-8") as f:
#     r = yaml.safe_load(f)
#     print(r)

re = YamlReader("./data.yaml").data()
print(re)

#读取多个文档

reall = YamlReader("./data.yaml").data_all()
print(reall)


# with open("./data.yaml", "r",encoding="utf-8") as f:
#     r = yaml.safe_load_all(f)
#     for i in r:
#         print(i)


