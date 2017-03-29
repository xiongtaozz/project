# coding:utf-8
def add():
    print 'this is add'

# 类和方法
# 学生 name sorce


class Student:

    def __init__(self, name, sorce):

         self.name = name

         self.sorce = sorce

    def getCorce(self):
        return '%s:%s' % (self.name,self.sorce)

    @classmethod
    def getClass(cls):
        print 'get this %s' % cls.name

    @staticmethod
    def getStatic():
        print Student.name

s1 = Student('tom',98)
s2 = Student('lily',88)
print s1.getCorce()
Student.name = 'Jack'
Student.getClass()
Student.getStatic()

print '---------------------------------------------->'


class techer(object):
    def __init__(self):
        self.name='jack'
        self.age=28
    def print_all(self):
        print '%s:%s'%(self.name,self.age)


class techers(techer):
    def __init__(self,sex):
        techer.__init__(self)
        # super(techers,self).__init__()
        self.sex=sex
    def print_all(self):
        print '%s:%s:%s'%(self.name,self.age,self.sex)
t = techers('nan')
t.print_all()
# class A(object):
#     def __init__(self):
#         self.namea="aaa"
#     def funca(self):
#         print "function a : %s"%self.namea
# class B(A):
#     def __init__(self):
#         #这一行解决问题
#         # A.__init__(self)
#         super(B,self).__init__()
#         self.nameb="bbb"
#     def funcb(self):
#         print "function b : %s"%self.namea
# b=B()
# # print b.nameb
# b.funcb()
# b.funca()