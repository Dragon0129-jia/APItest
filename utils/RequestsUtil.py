# 1、创建封装的方法
import requests

from utils.logUtil import my_log


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


# POST方法封装
# 1、创建方法
def requests_post(url, json=None, headers=None):
    r = requests.post(url, json=json, headers=headers)
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


# 重构方法
class Request:

    def __init__(self):
        self.log=my_log("Requests")
    def requests_api(self, url, data=None, headers=None, json=None, cookies=None, method="get"):
        if method == "get":
            self.log.debug("发送get请求")
            r = requests.get(url, headers=headers, data=data, cookies=cookies)
        elif method == "post":
            self.log.debug("发送post请求")
            r = requests.post(url, json=json, headers=headers, data=data, cookies=cookies)
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

    def get(self, url, **kwargs):
        res = self.requests_api(url, method="get", **kwargs)
        return res

    def post(self, url, **kwargs):
        res = self.requests_api(url, method="post", **kwargs)
        return res
