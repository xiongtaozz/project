#coding:utf-8
# 使用基本语法写出双色球 开奖作业： red blue
# 引用 random 模块库  用到 range（）函数
import random
red_boll=range(1,33)
bule_boll=range(1,17)
print red_boll
print bule_boll
random.choice(red_boll) #[1,2,3,4,5,6,7]
#6 + 1
list=[]
while len(list)<7:
    if len(list)<6:
        red = random.choice(red_boll)
        list.append(red)
        red_boll.remove(red)
    else:
        blue=random.choice(bule_boll)
        list.append(blue)
print list
print '---------------------'
print 'hello word'
print u'函数'
#str='hello word 缺省参数  str必备
def add(str):
    #插入数据
    global str2
    print '操作'
def update(str):
    return True
def delete(str):
    return str
a = add('hello!')
print a
print '-------------------------------'
import os as o
from sys import argv
#frist,...
print argv
print o.path.join(o.path.dirname(__file__),'demo05.py')
filePath='D:\工作\作业\面向对象基础'
print filePath
#内置 uillib1,uillib2,time

#文件处理
#找到书--- 打开-- 写入/读取 --- 关闭
#读取
filePath=o.path.join(o.path.dirname(__file__),'text.txt')
file=open(filePath)
print file.read()
file.close()
#写入
filePath=o.path.join(o.path.dirname(__file__),'text.txt')
#异常处理 try ... except ... else ... findlly
try:
    file=open(filePath,'a+')
    file.write('\nhsjdddddd')
except ValueError:
    print u'值错误'
else:
    print 'this esle'
finally:
    file.close()
    print u'始终要执行的'


a=range(1,6)
b=a.reverse()
print b
print '-------------------------------------------'

def count():
    list=[]
    for i in range(1,4):
        list.append(i*i)
    print list
count()