import requests

from utils.RequestsUtil import requests_get, requests_post, Request


def login():

    url="http://admin.5istudy.online/login/"
    data={"username":"18875286857","password":"jia123456"}
    response = Request().post(url, json=data)
    print(response)

def info():
    url="http://admin.5istudy.online/users/1/"
    token="JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxNjk5ODIsInVzZXJuYW1lIjoiMTg4NzUyODY4NTciLCJleHAiOjE2ODY1ODU4NzIsImVtYWlsIjpudWxsfQ.h_k4CHA-wRfIzS4dJCMzN7gcnj70Ii5dPCkMu2a8DD4"
    # re= requests_get(url, headers={"Authorization": token})
    request = Request()
    res = request.get(url, headers={"Authorization": token})
    print(res)



def goods_list():
    url = "http://admin.5istudy.online/orders/"
    token = "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxNjk5ODIsInVzZXJuYW1lIjoiMTg4NzUyODY4NTciLCJleHAiOjE2ODY1ODQ4NjksImVtYWlsIjpudWxsfQ.nd9d7e9fF7dLIZ-O0fktuv50rqPjTLpBWPPlWfGooIc"
    response = requests_get(url, headers={"Authorization": token})
    print(response)

if __name__ == '__main__':
    login()
    # info()
    # goods_list()


