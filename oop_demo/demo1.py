#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
经典类与新式类 --- 3.x 所有的默认新式
经典类：没有父类的时候，不需继承object
新式类：没有父类的情况下，也需要继承object
新式类是在2.2中开始引入的，3.x中统一为新式类
1、经典类中不能使用property和super，新式类中能使用property和super
2、经典类的类型是classobj，新式类的类型是type
3、在多继承中，新式类采用广度优先搜索，而旧式类是采用深度优先搜索。
"""


class Ab(object):
    def __init__(self, x, y):
        self.x = 1
        self.y = 2


class Abc(Ab):

    def __init__(self):
        # super().__init__()
        super(Abc, self).__init__(2, 3)
        self.z = 4

a = Abc()
# print a.x, a.y, a.z

# 2.7.x
class A:  # 父类   #A 类本身的实例 self 类本身对象的实例
    def __init__(self):
        # super(A, self).__init__()
        # A.__init__()
        pass


class B(object):  # 子类  cls 类本身 self 类本身的实例对象
    def __init__(self):
        super(B, self).__init__()
        pass

    # instance

    @classmethod
    def classB(cls):
        pass

    @staticmethod
    def add():
        pass
    pass
# B().add()
print type(A)
print type(B)
print type(A())
print type(B())

# # class C(A, B):
# #     pass
# a = A()
# b = B()
#
# print(type(A))
# print(dir(a))
#
# print(type(B))
# print(dir(b))


# ------------------------
# 经典类：A->B->D->C
# 新式类：A->B->C->D->object
# http://blog.csdn.net/imzoer/article/details/8737642

class D(object):
    def foo(self):
        print("class D")


class B(D):
    pass


class C(D):
    def foo(self):
        print 'class C'


# 新式 : A B C D
# 经典 : A B D C
class A (C, B):  # 谁在前面执行谁(X) --->新式类当中不成立
    pass

f = A()
f.foo()  # class C  class D
# print A.__doc__




