# coding:utf-8

# try:
#     r = int(raw_input('>'))
# except ValueError:
#     print u'类型错误'
# except NameError:
#     print u'请确认名称'
# else:
#     print r
#     print u'try内容没有异常,则执行'
# finally:
#     print u'始终要执行'
#
# raise ValueError('')


# 函数嵌套 --- > 闭包
def adder(x):  # 2
    print 'info adder'

    def water(y):  # 5
        return x + y  # 6
    return water  # 3
# w = adder(1)  # 1
# print w(2)  # 4
# print w(3)  # 4
# print w(4)  # 4


@adder
def add():
    print 'info add'


url = 'http://www.baidu.com'
# HTTP  超文本协议 http://www.maiziedu.com/home/t/one_meeting/?id=1409
# HTTPS 超文本加密协议
# import urllib2
#
# res = urllib2.urlopen(url)  # get
# print res.read()
# # post
# data = {}
# headers = {}
# res = urllib2.Request(url=url, data=data, headers=headers)
# res.read()
# 代理 , cookie

#  coding=utf-8
import os
import datetime             #导入时间显示所需的包

while True:                #外层循环将用户输入的新文字保存写入原来的文档
    print("保存好的文档是这样的：\n")
    f=open("recode.txt","r")    #读入方法
    while True:             #内层循环用来读入并且显示出保存好的文档
        line=f.readline()
        print(line)          #逐行读入并显示
        if len(line)==0:
            print("\n")
        try:
            str_1=input("请输入内容：")     #显示完毕后请用户输入新的文字
            break
        except:
            pass                          #忽略了输入所产生的异常
    now = datetime.datetime.now()
    otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")   #这两行是导入系统时间并格式化显示
    f=open('recode.txt','a')                              #追加写入
    f.write(str_1+"---"+str(otherStyleTime)+"\n")          #追加并按要求格式写入
    if str_1=="quit" or str_1=="exit":
        break
f.close()
