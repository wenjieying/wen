'''
上传文件，一般都是post接口，用files参数上传文件
'''

import  requests
ur1 = "http://www.httpbin.org/post"
'''
files 参数，字典的格式，’name‘:file-tuple
'''

with open("d:/text.txt",encoding='utf-8') as f:
    file = {"file1":("text.txt",f,"txt/plain")}  #MINE类型：text/plain.image/png.image/gif.application/json
    r = requests.post(ur1,files=file)
    print(r.text)

# 上传一个图片文件 10K以内
#
# with open("D:\\text.txt", encoding='utf-8') as f:
#     file = {"file1":("text.txt",f,"image/txt")}
#     r = requests.post(ur1,files =file)
#     print(r.text)
#
with open("C:\\Users\\86199\\Desktop\\timg.jpg",mode='rb') as f:
    file = {"file2":("timg.jpg",f,"image/jpg")}
    r = requests.post(ur1,files=file)
    print(r.jpg)
# 可以上传多个文件。
# with open("d:/test.txt",encoding='utf-8')as f1:
#     with open("C:\\Users\\86199\\Desktop\\timg.jpg",mode='rb') as f2:
#         file = {"file1":("test.ping",f1,"image/ping"),"file2":("timg.jpg",f2,"image/jpg")}
#         r = requests.post(ur1,files= file)
#         print(r.reason)