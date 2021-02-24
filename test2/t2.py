# -*- codeing =utf-8 -*-
# @Time : 2021/2/22 18:10
# @Author : Iestyn
# @File : t2.py
# @Software : PyCharm

#引入自定义模块
from test1 import t1
print(t1.method1(1,2))

#引入系统模块
import sys
import os

#引入第三方模块
from bs4 import BeautifulSoup    #网页解析，获取数据
import re     #正则表达式，进行文字匹配

import urllib.request,urllib.error
#指定URL，获取网页数据

import xlwt    #进行excel操作
import sqlite3    #进行SQLite数据库操作