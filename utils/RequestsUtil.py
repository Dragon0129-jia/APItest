# 1、创建封装的方法
import requests



def requests_get(url, headers):
    # 2、发送请求
    r = requests.get(url, headers=headers)
    code = r.status_code
    # 3、获取相应的内容
    try:
        body = r.json()
    except Exception as e:
        body = r.text
    # 4、内容存到字典
    res = dict()
    res["code"] = code
    res["body"] = body

    # 5、字典返回
    return res

#POST方法封装
#1、创建方法
def requests_post(url,json=None,headers=None):
    r = requests.post(url,json=json,headers=headers)
    #
    code = r.status_code
    # 3、获取相应的内容
    try:
        body = r.json()
    except Exception as e:
        body = r.text
    # 4、内容存到字典
    res = dict()
    res["code"] = code
    res["body"] = body
    return res

#重构方法
class Request:
    def requests_api(self,url,headers=None,json=None,method="get"):
        if method=="get":
            r=requests.get(url, headers=headers)
        elif method=="post":
            r=requests.post(url,json=json,headers=headers)
        code = r.status_code
        # 3、获取相应的内容
        try:
            body = r.json()
        except Exception as e:
            body = r.text
        # 4、内容存到字典
        res = dict()
        res["code"] = code
        res["body"] = body

        # 5、字典返回
        return res
    def get(self,url,**kwargs):
        res = self.requests_api(url,method="get", **kwargs)
        return res



