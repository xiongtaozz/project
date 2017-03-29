# -*- coding:utf-8 -*-

'''
   @author: xt
   @data: 2016-7-4
   @capacity: lambda表达式

   函数式:def func(x,y): return x+y
   lambda表达式: lambda x,y:x+y
   python当中的特殊函数:
   filter,map,reduce,zip
   filter(函数对象,处理类容) --->过滤掉False结果 --->过滤器(筛选)
'''

# 函数式编程和过程式编程


# def l_pro():
l = []
for x in range(1, 11):
   if x > 5:
      l.append(x)
print l


def func(x): return x > 5
print filter(func, tuple(range(1, 11)))  # 过滤,

# print l_pro()


# def func(x, y): return x+y
# print func(1, 2)
# print lambda x, y: x+y
#
#
print filter(lambda x: x > 5, range(1, 11))
# 一行表达式
# lambda 没有return

print map(lambda x, y: x*y, tuple(range(1, 11)), tuple(range(11, 21)))
print sum(range(1, 101))
print reduce(lambda x, y: x+y, range(1, 101), -20)
#
# # 有参匿名函数
# lambda : True
# def func(): return True
# # 无参数匿名函数