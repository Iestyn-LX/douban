# -*- codeing =utf-8 -*-
# @Time : 2021/2/23 11:24
# @Author : Iestyn
# @File : testBs4.py
# @Software : PyCharm

from bs4 import BeautifulSoup
file =open("./douban.html","rb")   #二进制转义
html =file.read()
bs =BeautifulSoup(html,"html.parser")  #用html的解析器

# # print(bs.title)
# print(bs.head)
# print(bs.a)
# print(type(bs.title))
# #1.Tag 标签及内容：拿到它所找到的第一个内容，比如第一个a
#
# print(bs.title.string)  #只拿标签中的内容
#
# print(type(bs.title.string))
#
# #2.NavigableString 标签里的内容类型（字符串）
#
# print(bs.a.attrs)  #快速拿到标签值里的所有属性，字典格式



# print(type(bs))
# #3.BeautifulSoup   表示整个文档
#
# print(bs.name)  #表示整个文档
# print(bs)


# print(bs.a.string)
# print(type(bs.a.string))
# #4.Comment  特殊的NvigableString类型，但不输出标签注释符号



#——————————————————————————————

#文档的遍历
# print(bs.head.contents[1])
# #搜出来的是列表，可以定位下标来捕捉某个元素


#文档的搜索
#（1）find_all()
# a.字符串过滤：会查找与字符串【完全】匹配的内容
# t_list =bs.find_all("a")    #查找所有的a
# print(t_list)

# import re
# # b.正则表达式搜索：使用search()方法来匹配内容
# t_list =bs.find_all(re.compile("a"))
# #匹配标签内带a的内容
# print(t_list)


# c.方法：传入一个函数（方法），根据函数的要求来搜索  （了解）
# def name_is_exists(tag):
#     return tag.has_attr("name")
#
# t_list =bs.find_all(name_is_exists)
#
# for item in t_list:
#     print(item)


#（2）kwargs 参数

# t_list = bs.find_all(id="db-global-nav")
# # print(t_list)
# t_list =bs.find_all(class_=True)
# #找到有class的子集
# t_list =bs.find_all(href= "https://movie.douban.com/subject/1299398/")
# #找到含有该值的内容
#
# for item in t_list:
#     print(item)



#（3）text参数
# import re
# #查找text内容
# # t_list =bs.find_all(text="大话西游之月光宝盒")
# # t_list =bs.find_all(text=["大话西游之月光宝盒","我不是药神"])
#
# #使用正则表达式来查找包含特定文本的内容
# t_list = bs.find_all(text= re.compile("\d"))

#（4）limit 参数
# t_list =bs.find_all("a",limit=3)
# #限制a标签，前3条



#CSS选择器

t_list =bs.select("title")  #通过标签来查找

t_list =bs.select(".mnav")    #通过类名来查找

t_list = bs.select("a[class='bri']")   #通过id来查找

t_list =bs.select("head > title")   #通过子标签来查找

t_list = bs.select(".mnav ~ bri")   #找mnav的兄弟同级标签bri

for item in t_list:
    print(item)