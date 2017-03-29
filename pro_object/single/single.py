# -*- coding:utf-8 -*-

"""
   单例模式
   概念:什么是单例模式
   要知道什么是python的单例模式，所谓单例模式就是一个类只能创建一个实例化。
   然后，就是python单例模式的方法
   模式特点：保证类仅有一个实例，并提供一个访问它的全局访问点
"""


class A(object):
    a = 1

# a = A()
# b = A()
# print id(a)
# print id(b)
# print a is b
# b.a = 2
# print a is b

# 方法1,实现__new__方法
# 并在将一个类的实例绑定到类变量_instance上,
# 如果cls._instance为None说明该类还没有实例化过,实例化该类,并返回
# 如果cls._instance不为None,直接返回cls._instance


class Singleton(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class myClass(Singleton):
    a = 1

# one = myClass()
# two = myClass()
# thr = myClass()

# two.a = 3
#
# print one.a
#
# print id(one)
#
# print id(two)
#
# print one is two


# 方法二
def Singleton2(cls, *args, **kwargs):
    instance = {}

    def _instance():
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return _instance


@Singleton2
class myClass2(object):
    a = 1

    def __init__(self, x=0):
        self.a = x

one = myClass2()
two = myClass2()

two.a = 3

print one.a

print id(one)

print id(two)

print one is two
