# '''
# cookie
# '''
import requests
#headers请求头 由key ： value 组成 参数名与值 冒号分隔  cookie:  存在：客户端
#cookie是访问网站时，由网站服务器返回的一种标记为cookie
#类型数据，存储在浏览器的上，以后每次访问本完整，浏览器都会在http请求中将该数据发送过来

head = {
    "Cookie": "BAGSESSIONID=c9993b5d-16f9-4b56-ac90-6d44a706287a; Hm_lvt_1fc37bec18db735c69ebe77d923b3ab9=1604649158; MEIQIA_TRACK_ID=1juLik4zNoIOBVgLJyBiPaTn4VW; MEIQIA_VISIT_ID=1juLikZIr0crrnVHIXpgwXmWO0D; __asc=6bbc4a7d1759c8b0b7d052de4b2; __auc=6bbc4a7d1759c8b0b7d052de4b2; _ga=GA1.2.1550897674.1604649163; _gid=GA1.2.983314573.1604649163; JSESSIONID=6BBF1F576F143958EA674FB3D4A74848; _gat=1; Hm_lpvt_1fc37bec18db735c69ebe77d923b3ab9=1604649257; BAG_EVENT_TOKEN_=30a6e07399c5d7b305fc614a1294bb254b1acac9; BAG_EVENT_CK_KEY_=15353342865; BAG_EVENT_CK_TOKEN_=4d5fcdad7419493a983b1281078c7f28"
}



#获取登录网址  requestsqs：请求    headers请求头
r = requests.get("https://www.bagevent.com/account/dashboard",headers=head)
print(r.text)
# 没登陆时，title显示为<title><title>
# 登录后，title 显示为<title>摆个活动-账号总览</title>

'''
requests 中自动管理cookies的机制
'''
# Session会话 
# 1. 当登录成功后，session第一次被创建，一个唯一的标识被存储于本地的cookie中的sessionid中。
#  2. 再次打卡浏览器后回去数据库查session的id去比对
s = requests.session() #创建一个session，通过session 发送请求
print("登录之前的cookies",s.cookies)
#登录
#字典的形式，一个key 对应一个值 例a如ccess_type=1  "access_type":1,
#点击 webFroms获取canshu
canshu = {
    "access_type":1,
    "loginType": 1,
    "emai1LoginWay": 0,
    "account": "2780487875@qq.com",
    "password": "qq2780487875",
    "remindmeBox": "on",
    "remindme": 1


}


#调用dashboard
r = s.post("https://www.bagevent.com/user/login",data=canshu)
print("登录之后的cookies",s.cookies)
print(r.text)
#调用dashboard的接口 "https://www.bagevent.com/user/login"
r = s.get("https://www.bagevent.com/account/dashboard")
print("<title>百格活动 - 账户总览</title>"in r.text)

#获取活动列表
r = s.get("https://www.bagevent.com/account/myevents?published=1")
print(r.text)
#查看某个活动下
