# coding:utf-8
# 面对对象 {
#  1,继承
#  2,多态 基础python
#  3,封装
# }


# class A():
#     def add(self):
#         print '__init__ A'
#
# def B(a):
#     a.add()
#
# a, b = 1, 'sss'
# a = A()
# print a
# B(a)
# 对象私有和公有
# class Person:  # 经典类
#     # __name = 'Tom'
#     # age = 25
#
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def getName(self):
#         return self.__name
#
#     def setName(self, name):
#         self.__name = name
#
# p = Person('Tom', 28)
# # p.name = 'Lily'
# print p.getName()
# # p.setName('Lily')
# # print p.getName()
# p.__init__('Lily', 27)
# print p.getName()
# print dir(p)
# print p._Person__name

# def add():
#     pass
# print add()
import random as r
import time


# class double_ball(object):
#
#     def __init__(self):
#         self.red_ball = range(1, 33)  # 红球 筛选6
#         self.blue_ball = range(1, 17)  # 篮球 筛选1
#         self.s_ball = []
#
#     def shaiRedBall(self):  # 筛选红球业务
#         while len(self.s_ball) < 6:
#             red = r.choice(self.red_ball)
#             self.red_ball.remove(red)
#             self.s_ball.append(red)
#         return self.s_ball
#
#     def shaiBlueBall(self):
#         self.s_ball.append(r.choice(self.blue_ball))
#         return self.s_ball
#
#     def saveFile(self):  # w s d
#         s = '本次开发奖的红是:%d %d %d %d %d %d 特号是:%d'%tuple(self.s_ball)
#         t = time.strftime('%Y-%m-%d', time.localtime(time.time()))
#         c = s + '\n本次开奖时间:' + t
#         print c.decode('utf-8')
#
#     @classmethod
#     def this(cls):  # 类本身
#         pass
#
#     def run(self):  # 类本身的实例
#         self.shaiRedBall()
#         self.shaiBlueBall()
#         self.saveFile()
#         # print self.s_ball
# if __name__ == '__main__':
#     d = double_ball()
#     d.run()

class A():
    def add(self):
        print '__init__ A'

    def __new__(cls, *args, **kwargs):
        print u'先于构造函数执行'
        pass


class B(A):
    pass


class C(A):
    def add(self):
        print '__init__ C'


class D(B, C):
    pass


d = D()
print dir(d)