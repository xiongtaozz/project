#coding:utf-8
# 父类需要继承object对象
class A(object):
    def __init__(self):
        self.namea="aaa"
    def funca(self):
        print "function a : %s"%self.namea
class B(A):
    def __init__(self):
        #这一行解决问题
        # A.__init__(self)
        super(B,self).__init__()
        self.nameb="bbb"
    def funcb(self):
        print "function b : %s"%self.nameb
b=B()
print b.nameb
b.funcb()
b.funca()
# from collections import Iterable
# list =range(1,10)
# print isinstance(list,Iterable)