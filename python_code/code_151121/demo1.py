#coding:utf-8
def printime(str,age=15):
    print str
    print age
# printime(111) #必备参数
# printime(str='hello word') #命名参数
printime(str='hello') #age 缺省
printime(str='hello',age=10) #age缺省
print '%s %s %s %s'%(1,2,3,4)
print '-----------------------'
def add(t):
     return t
print add(10)
print '-----------------------'
def add1(t1):
    a =11 #成员 局部
    print t1
    return a
print add1(10)
list = range(1,5)
print list.reverse()
print list
import random as r
from random import choice

# 位置--打开文件 ---读写---关闭
import os
filePath = os.path.join(os.path.dirname(__file__),'text.txt')
file = open(filePath,'r')
# print file.read()
for f in file.readlines():
    '''doc'''
    print f
# write(), writelines()
file.close()
print '-------------------------'
list1 = ['1111' , '22222' , '33333']
# String = raw_input('需要提示内容>') #input
filePath = os.path.join(os.path.dirname(__file__),'text.txt')
file = open(filePath,'a+') # r r+ w w+ a a+ b
# print file.read()
file.writelines(list1) #\n \t \r
# write(), writelines()
file.close()
# try else except findlly
try:
    String = int(raw_input(u'需要提示内容>'))
    print String #1
except ValueError:
    raise ValueError(u'1111')
    # print u'错误信息' #2
# except KeyboardInterrupt:
#     raise (u'wwwww')
# except KeyError:
#     pass
else:
    print u'成功' #3 如果try里面的内容无异常则执行,反之同理
finally:
    print u'最终要执行的' #4