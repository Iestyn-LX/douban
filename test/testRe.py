# -*- codeing =utf-8 -*-
# @Time : 2021/2/23 13:09
# @Author : Iestyn
# @File : testRe.py
# @Software : PyCharm

#正则表达式：字符串模式 判断字符串是否符合一定的标准

import re
# 创建模式对象，有模式对象
# pat =re.compile("AA")   #此处的AA，是正则表达式用来去验证其他的字符串
# # m =pat.search("ABCAA")   #search字符串被校验的内容
# m =pat.search("AABCAA")    #只找到第一个AA


#没有模式对象
# m =re.search("asd","Aasd")   #前面的字符串是规则（模板），后面的字符串是被校验的对象
# print(m)

#re.findall
#前面的字符串是规则（正则表达式），后面字符串是被校验的字符串
# print(re.findall("a","SADFAassdfa"))
#
# print(re.findall("[A-Z]","ASDFEAaaa213"))
#
# print(re.findall("[A-Z]+","ASDEAaaAAa213"))

#sub
print(re.sub("a","A","asdfagaeedd"))   #找到a用A替换，在第三个字符串中查找

# 建议在正则表达式中，被比较的字符串前面加上r，不用担心转义字符的问题
a = r"\aafds-\'"
print(a)


