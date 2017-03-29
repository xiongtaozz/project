#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
内建函数
类的常见特殊变量（保留属性）
Class1.__doc__ # 类型帮助信息 'Class1 Doc.' --->help  dir
Class1.__name__ # 类型名称 'Class1'
Class1.__module__ # 类型所在模块 '__main__'
Class1.__bases__ # 类型所继承的基类 (<type 'object'>,)
Class1.__dict__ # 类型字典，存储所有类型成员信息。 <dictproxy object at 0x00D3AD70>
Class1().__class__ # 类型 <class '__main__.Class1'>

类的常见魔术方法（保留方法）

构造和初始化相关的魔术方法：
__init__：构造方法
__new__：new方法，先于构造方法执行
__del__：析构方法 --程序执行完毕之前,会执行  回收

用于比较的魔术方法：
__eq__：定义了等号的行为, == 。
__ne__：定义了不等号的行为, != 。
__lt__：定义了小于号的行为， < 。
__gt__：定义了大于等于号的行为， >=
__cmp__：定义了实现了所有的比较符号(<,==,!=,etc.)

一元操作符和函数的魔术方法：
__pos__：实现正号的特性(比如 +some_object)
__neg__：实现负号的特性(比如 -some_object)
__abs__：实现内置 abs() 函数的特性。
__invert__：实现 ~ 符号的特性

普通算数操作符的魔术方法：
...
...
控制属性访问的魔术方法:
...
...
等等,具体参照:
http://pycoders-weekly-chinese.readthedocs.org/en/latest/issue6/a-guide-to-pythons-magic-methods.html
"""
# 异常处理
# try:
#     inp = raw_input('>')  # 无异常继续执行
# except Exception as e:
#     print e  # 有异常执行这里
# else:
#     pass  # 无异常继续执行
# finally:  # 始终要执行
#     pass


class A(object):

  def get_name(self):
      pass

# print A.__doc__
# print '-'*50
# print dir(A)


# class A:
#     def __init__(self, **kwargs):
#         self.__dict__ = kwargs
#
# a = A(a='haha', b=[1,2,3], c=123)
# print(a.b)

# ----------------------


class A(object):  # 如果不继承object 系统会认为是经典类
    # def __new__(cls, *args, **kwargs):
    #     print u'new函数执行'

    def __init__(self):
        print(u'构造函数执行')  # 2

    def __del__(self):
        print(u'析构函数执行')  # 4

    def test(self):
        print('test')   # 3

    # self时候 类本身的实例, cls  类本身
    def __new__(cls, *args, **kwargs):  # 1
        print(type(cls))
        print(u"new方法执行")
        return super(A, cls).__new__(cls, *args, **kwargs)

# a = A()
# # b = A()
# # print id(a)
# # print id(b)
# a.test()
# print '*'*100

# 1、如果你想改变一个已有类型原有的初始化过程。
# 假设去做一个生成绝对值的类。从int去继承过来的
class D(int):
    def __init__(self, x, base=10):
        super(D, self).__init__(self, abs(x), base)

class E(int):
    def __new__(cls, x):
        return super(E, cls).__new__(cls, abs(x))

# d = D(-7)
# print d
# e = E(-7)
# print e

# 2、通过new方法去实现单例模式

# class A(object):
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, "_instance"):
#             cls._instance = super(A, cls).__new__(cls, *args, **kwargs)
#         return cls._instance

# 3、__call__方法的应用
class Next:
  List = []

  def __init__(self, low, high):
    for Num in range(low, high):
      self.List.append(Num ** 2)

  def get_all(self):
    return self.List

  def __call__(self, a):  # 加入call之后可以吧实例对象变换可调用函数
    return self.List[a]

n = Next(1, 10)
# 切片
# l = [.....]
print n.List[4]
print n.get_all()[4]
print n
print n(4)



class B(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    pass

class C(B):
    def __init__(self, a, b, c):
        super(C, self).__init__(a, b)
        self.c = c
