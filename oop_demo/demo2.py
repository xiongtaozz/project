#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
封装（私有(__)、公有、受保护(_)） from xxx import *
1、私有只需要在变量名或方法名前加上 "__"（两个下划线），
但注意要和(特殊变量和魔术方法)区分开，那么这个方法或变量就会为私有的了
2、私有变量（方法）只能在类的内部使用，不能在内的外部使用
3、公有变量（方法）可以随意使用
4、受保护类型变量（方法）可以类内部或者之类中使用，3.x才有受保护类型
5、Python解释器会把私有属性和变量转换为 _类名__变量(方法)名的形式
6、_程序默认也会把他认为是共有变量,只是防止from引入
"""
# a = str,int,float,object,class,....


class Person:

    # def __new__(cls, *args, **kwargs):
    #     pass

    # Person 类本身
    # self  类实例本身
   def __init__(self, name):   # 构造函数 --->实例化即运行而且只能运行一次 ,目的:实例化变量

       print('info init')

       # super(Person, self).__init__()   ages 实例父类里面的内容

       self.name = name
       self.__age = 22  # 私有属性
       self._sex = 1

   def get_age(self):
       return self.__age

   def set_age(self,age):
       self.__age = age

   def __get_name(self):  # 私有方法
       return self.__age

   def get_name(self):  # 比较合理获取方法
       return self.__age

   def set_name(self, age):
       self.__age = age

   # def get_sex(self):
   #     return self.__sex
   #
   # def get_age(self):
   #     return self.age

# Person

# person = Person('Jack')   # person,Person()  实例化对象 ---> self ;  Person:类对象 --cls
# person.__init__('Tom')    # 第二次实例化
# print person.name
# print person.get_age()
# person.set_age(25)
# print person.get_age()
# print dir(person)
# # print person._Person__age
# print person._sex

# print 'person age is:', person._Person__age  # 22
# print dir(person)
# print person._sex
# print 'person age is:', person.age  # 25
# # print 'person name is', person.__name
# print person.get_name()
# # print person._Person__name
# # print 'person name is:', person.get_name()
# person.set_name(u'小花')
# print 'person name is:', person.get_name()
# print person._Person__name
# # # # print person.get_name()
# print dir(person)
#
# print(person.get_name())
# person.set_name('Jack')
# print(person.get_name())
# print(person.__get_name())

# ---------------------
# 使用@property和@xx.setter装饰器  二者必须用到一起


class Square(object):
    def __init__(self, side):
        self._side = side
        self.__name = 'LIly'

    @property    # 修饰符/装饰器  # 描述符: 将函数当做变量使用,并且享受函数里面的方法
    def side(self):  # get
        return self._side

    @side.setter  # 结合xxx.setter
    def side(self, side):  # set
        if side < 0:
            self._side = 0
        elif side > 100:
            self._side = 100
        else:
            self._side = side

    def area(self):
        return self._side ** 2

    def __call__(self, *args, **kwargs):
        pass

# s = Square(20)
# print s.side
# # # # # 装饰器的一个作用 会吧side 看作成一变量 __call__
# s.side = 101
# print s.side
# print s.area()
# print(dir(s))
# print s._Square__name

# class F(object):
#     def foo(self):
#         print 'foo F'
# class E(F):
#     pass
# def G():
#     return
# def H(e):
#     print e.foo()
# e = E()
# print H(e)  # A, 对象加内存地址. B.None  C.对象地址,None

# 双色球

import random as r


class double_ball(object):

    def __init__(self):
        self.red_ball = range(1, 33)
        self.blue_ball = range(1, 17)
        self.s_ball = []

    def s_red(self):
        self.s_ball = r.sample(self.red_ball, 6)
        self.s_ball.sort()

    def s_blue(self):
        self.s_ball.append(r.choice(self.blue_ball))

    def run(self):
        self.s_red()
        self.s_blue()
        print self.s_ball

if __name__ == '__main__':
    double_ball().run()