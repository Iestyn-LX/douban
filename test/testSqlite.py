# -*- codeing =utf-8 -*-
# @Time : 2021/2/24 12:22
# @Author : Iestyn
# @File : testSqlite.py
# @Software : PyCharm

import  sqlite3

conn = sqlite3.connect("test.db")  #打开或创建数据库文件
print("opened database successfully")


c = conn.cursor()     #获取游标

sql = '''
    create table one
    ( id int primary key not null,
    name text not null,
    age int not null,
    address char(50),
    salary char(50)
    );

'''

c.execute(sql)        #执行sql语句
conn.commit()         #提交数据库操作
conn.close()          #关闭数据库

print("成功建表")


#插入数据



#查询数据