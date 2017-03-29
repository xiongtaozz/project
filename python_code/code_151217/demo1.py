# -*- coding:utf-8 -*-

# a = 'World'

# t = ('Hello',a)

# print '%s %s'% t

# list = range(10)
#
# print list.reverse()
# #  for ----> list =
# print list
#
# def Hello(a,d=1,*b,**c):
#     # print 'Hello', a
#     #
#     # print '--->',b
#     print list
#     print '--->',d
#     return d
# def World():
#     x = 1
#
# h = Hello(1)
# print h

# from random import sample,choice
# import  random as r
# r.sample

import os

# path = os.path.join(os.path.dirname(__file__),'demo.txt')
path = 'demo.txt' #找到文件路劲
# print path
# lsit = ['1111','2222','3333','44444','55555']
# f = open(path,'a+')
# # str = raw_input(u'请出入要内容:')
# f.writelines(lsit)
# f.close()

# input()  3.0

# try:
#     f = open(path)
#     # print f.readlines()
#     for i in f.readlines():
#         print i
# except :
#     print u'错误'
# else:
#     print 'in close'
#     f.close()
# finally:
#     pass

# try else except finally 异常处理
# try:
#     string = int(raw_input(u'请输入:'))
# except TypeError as e:
#     print e # try 内出现异常,则执行
# except ValueError as e:
#     print e
# except :
#     raise ValueError('this')
# else:
#     print 'in else!' # try 内无异常,在执行
# finally:
#     print 'in finally!' # 最终要执行.
from random import choice
import time

print time.time()
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

# red_ball = range(1, 34)
# blue_ball = range(1, 17)
# lsit = []
# while len(lsit) < 7:
#     if len(lsit) < 6:
#         r = choice(red_ball)
#         lsit.append(r)
#         red_ball.remove(r)
#     else:
#         lsit.append(choice(blue_ball))
# print lsit
