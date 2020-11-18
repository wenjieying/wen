'''
发送post 请求
    1. 使用data传表单格式的参数
    2. 使用json传json 格式的参数
'''

import requests

# 发送Post请求，带参数时，可以使用data或者json来传参，具体使用哪个要看系统怎么实现的
# 上一步注册成功的手机号，验证登录，登录使用post

ur1 = "http://jy001:8081/futureloan/mvc/api/member/login"
canshu = {"mobilephone": "18023232123", "pwd": 123456}
r = requests.post(ur1, data=canshu)  # 表单
print(r.text)
# r = requests.post(ur1, json=canshu)  # json,金融系统不支持json方式传参
# print(r.text)
#
# # 发送请求到httpbin,观察区别
# r = requests.post("http://www.httpbin.org/post", data=canshu)
# print(r.text)
# r = requests("http://www.httpbin.org/post", json=canshu)  # ”Conter-Type
# print(r.text)
