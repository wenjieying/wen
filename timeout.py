'''
timeout
1,接口性能测试，比较某个接口在500ms返回：
2，耗时比较久的操作，默认的超时时间执行不完，比如上传超大文件
'''
import requests
ur1 = 'https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel=19919940323'
for i in range(100):
    #0.1表示100ms
    try:
        r = requests.get(ur1,timeout=0.1)
        print(r.status_code)
    except Exception as e:
        print(e)


r = requests.get(ur1)
print(r.text)

'''
proxie 代理
1，通过代理抓包，用fiddler抓自动化发的报文分析
2，服务器吧IP封掉，可以通过代理换个IP访问
'''
proxy = {
    "http":"http://127.0.0.1:8888",#http
    "https":"http://127.0.0.1:8888" #ttps代理
}
#设置proxies时，需要打开代理服务器fiddler
r = requests.get("www.baidu.com",proxyes=proxy)
print(r.text)
#不加verify=False时，会校验证书，发送请求错误：certificate verfy failed 可以设置verity=False不校验证书
r = requests.get("https://www.bagevent.com",proxies=proxy,verfy=False)
print(r.text)