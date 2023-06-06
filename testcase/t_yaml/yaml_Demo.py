import os

import yaml

#读取单个文档
# with open("data.yaml", "r", encoding="utf-8") as f:
#     r = yaml.safe_load(f)
#     print(r)

#读取多个文档

path=os.path.join(os.path.abspath(os.path.dirname(__file__)),"data.yaml")



# with open(path, "r",encoding="utf-8") as f:
#     r = yaml.safe_load_all(f)
#     for i in r:
#         print(i)



