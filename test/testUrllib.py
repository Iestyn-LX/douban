# -*- codeing =utf-8 -*-
# @Time : 2021/2/22 19:12
# @Author : Iestyn
# @File : testUrllib.py
# @Software : PyCharm

import urllib.request

#
# #获取一个get请求
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))    #对获取的网页源码进行utf-8解码

# #获取一个post请求
# #模拟用户真实登录，输入cookie，账号密码等
# import  urllib.parse  #解析二进制
# data =bytes(urllib.parse.urlencode({"key":"value"}),encoding="utf-8")   #转换成二进制的包
# response =urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode("utf-8"))

#超时处理
# try:
#     response =urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)
#     #如果超时0.01s，则跳过
#     print(response.status)
# except urllib.error.URLError as e:
#     print("time out!")

#response返回网页的值
# response = urllib.request.urlopen("http://www.baidu.com")
# # print(response.status)     #返回状态码  如404，200，418
# #print(response.getheaders())   #返回response的headers
# print(response.getheader("Server"))

headers ={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0"
}
#封装好headers信息，假装不是代码

url ="https://movie.douban.com/"
data = bytes(urllib.parse.urlencode({"name":"Iestyn"}),encoding="utf-8")
req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")

response =urllib.request.urlopen(req)
print(response.read().decode("utf-8"))  #把从服务器端口中返回的数据重新编码
