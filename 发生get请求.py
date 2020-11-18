# '''
# 发送get请求
# '''

import requests

# 接口地址:"http://www.baidu.com“
# 发送一个get请求，r是收到的响应

r = requests.get("http://www.baidu.com")
# 文本格式的相应内容
print(r.text)
# 响应码
# print(r.status_code)
assert r.status_code == 200
# ok
# print(r.reason)
assert r.reason == 'OK'

# 金融项目：获取用户列表
# 发送 请求
# 接口地址 member/list ？ + 变量名
uel = "http://jy001:8081/futureloan/mvc/api/loan/member/list"
r = requests.get(uel)
# 检查结果
print(r.text)
# assert r.status_code == 200
# assert r.reason == 'OK'
# assert r.json()['status'] == 1
# assert r.json()['code'] == '10001'
# #'
# get 请求带参数
# 方法1： 评价到URl后面（金融项目注册接口）
# 方法2： 使用params传参数


# 方法1：拼接到URL后面（金融项目注册接口）
ur1 = "http://jy001:8081/futureloan/mvc/api/member/register?mobilephone=&pwd=123456&regname=helloword"
r = requests.get(ur1)
print(r.text)
# 方法2：使用params
url = "http://jy001:8081/futureloan/mvc/api/member/register"
canshu = {"mobilephone": "18902232324", "pwd": 123456, "regname": ""}
r = requests.get(url, params=canshu)
print(r.text)

# get请求带请求头，设置User-Agent伪装成浏览器发送的请求,避免服务器屏蔽自动化发的请求
ur1 = "http://www.httpbin.org/get?mobilephone=&pwd=123456&regname=helloworld"  # 一个测试网站， get 是测试网站
r = requests.get(ur1)  # “User -Agent”: “python-requests/2.18.4"
print(r.text)
# User -Agent 包含浏览器的版本号 ，操作系统的版本号等信息
tou = {
    "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
r = requests.get(ur1, headers=tou)
print(r.text)

ur1 = "https://wenku.baidu.com/view/027d607deff9aef8941e06c0.htm1"
r = requests.get(ur1, headers=tou)
print(r.text)
print("蜂群算法源代码" in r.text)

"""
发送get请求
"""

import requests

# 发送一个get请求，response是收到的响应
response = requests.get("http://www.baidu.com")
# 文本格式的响应内容
print(response.text)
# 响应状态码
print(response.status_code)
assert response.status_code == 200
# 响应状态描述
print(response.reason)
assert response.reason == 'OK'

# 发送请求
response1 = requests.get("http://jy001:8081/futureloan/mvc/api/member/list")
assert response1.status_code == 200
assert response1.reason == "OK"
# 检查结果
assert response1.json()['code'] == '10001'
assert response1.json()['status'] == 1
assert response1.json()['msg'] == '获取用户列表成功'

# get请求带参数
# 方法1：拼接到Url后面（金融项目注册接口）


# User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36

url = "http://jy001:8081/futureloan/mvc/api/member/register?mobilephone=13315076461&pwd=123456"
# params = ['mobilephone', 'pwd', 'regname']

r = requests.get(url)
print(r.text)
print(r.status_code)
assert r.status_code == 200

print(r.reason)
assert r.reason == 'OK'
# 方法2：使用params传参数
url1 = "http://jy001:8081/futureloan/mvc/api/member/register"
canshu = {"mobilePhone": "18023232123", "pwd": "123456", "regname": ""}
r1 = requests.get(url1, params=canshu)
print(r1.text)

# get请求带请求头 设置"User-Agent"伪装成浏览器发送的请求:
url2 = "http://www.httpbin.org/get?mobilePhone=13315076471&pwd=123456&regname="  # 一个测试网站。get接口名，发送的请求，原封的返回来
r = requests.get(url2)  # "User-Agent": "python-requests/2.24.0",
print(r.text)
# "User-Agent" 包含浏览器的版本号，操作系统的版本号等信息
tou = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
r4 = requests.get(url2, headers=tou)
print(r4.text)
