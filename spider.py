# -*- codeing =utf-8 -*-
# @Time : 2021/2/22 18:04
# @Author : Iestyn
# @File : spider.py
# @Software : PyCharm


#引入第三方模块
from bs4 import BeautifulSoup    #网页解析，获取数据
import re     #正则表达式，进行文字匹配

import urllib.request,urllib.error
#指定URL，获取网页数据

import re
import xlwt    #进行excel操作
import sqlite3    #进行SQLite数据库操作



def main():
    baseurl ="https://movie.douban.com/top250?start="
    #1.网页爬取
    datalist =getData(baseurl)
    savepath =".\\豆瓣电影Top250.xls"

    #3.保存数据
    saveData(datalist,savepath)


findLink = re.compile(r'<a href="(.*?)">')  #创建正则表达式对象，表示规则（字符串模式）
#贪婪模式和懒惰模式，此处后面添加？是懒惰模式
#影片片名
findTitle =re.compile(r'<span class="title">(.*)</span>')
#影片图片
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)  #让换行符包含在字符中
#影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#评价人数
findJudge =re.compile(r'<span>(\d*)人评价</span>')
#概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
#影片相关内容
findBd =re.compile(r'<p class="">(.*?)</p>',re.S)



#1.爬取数据
def getData(baseurl):
    datalist =[]
    for i in range(0,10) :  #调用获取页面信息的函数，10次，左闭右开
        url = baseurl + str(i*25)
        html= askURL(url)

        # 2.逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all("div", class_="item"):  # 查找符合要求的字符串，形成列表
            data = []
            item = str(item)
            # print(item)

            # 影片详情的链接
            link = re.findall(findLink, item)[0]  # re 库用来通过正则表达式查找指定的字符串
            data.append(link)
            # print(re.findall(findImgSrc, item))
            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)
            titles = re.findall(findTitle, item)  # 可能只有一个中文名，没有外文名
            if (len(titles) == 2):
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/", "")  # 去掉无关的符号
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(" ")  # 留空外文名

            rating = re.findall(findRating, item)[0]
            data.append(rating)  # 添加评分

            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)  # 添加评价人数

            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", "")
                data.append(inq)  # 添加概述
            else:
                data.append(" ")  # 留空

            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)  # 去掉<br/>
            bd = re.sub('/', " ", bd)  # 替换/
            bd = re.sub("\xa0", " ", bd)  # 去掉\xa0
            data.append(bd.strip())  # 去掉前后的空格

            datalist.append(data)  # 把处理好的电影信息存入datalist

    print(datalist)
    return datalist



#3.保存数据
def saveData(datalist,savepath):
    print("saving")
    book =xlwt.Workbook(encoding="utf-8",style_compression=0)   #创建workbook对象，样式效果的设定
    sheet = book.add_sheet("豆瓣电影Top250",cell_overwrite_ok=True)    #创建工作表，可以覆盖以前内容
    col =("电影链接","图片链接","影片中文名","影片外文名","评分","评价数","概况","相关信息")
    for i in range(0,8):
        sheet.write(0,i,col[i])   #列名
    for i in range(0,250):
        print("第%d条"%i)
        data = datalist[i]
        for j in range(0,8) :
            sheet.write(i+1,j,data[j])    #写入数据，第一个参数“行”，第二个参数“列”，第三个参数内容
    book.save('douban.xls')    #保存数据表


#得到指定一个URL的网页内容
def askURL(url):
    head = { #模拟浏览器头部信息，向服务器发送消息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0"
    }
    #用户代理，表示告诉服务器，我们是什么类型的机器，浏览器等信息

    request =urllib.request.Request(url,headers=head)
    html =""
    try:
        response = urllib.request.urlopen(request)
        html =response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)   #反映错误结果的编码
        if hasattr(e,"reason"):
            print(e.reason)   #反映错误结果的原因
    return html



if __name__ =="__main__":   #当程序执行时，入口点
#调用函数
    main()
    print("爬取完毕")