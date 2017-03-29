#coding:utf-8
# class Student:
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
#     def get_all(self):
#         print '%s:%s'%(self.__name,self.__age)
#     def set_all(self,name,age):
#         self.__name=name
#         self.__age=age
# s = Student('Tom',28)
# print s._Student__name
# s.get_all()
# s.set_all('Jack',25)
# s.get_all()
#继承
class ObjectA(object): #爷爷类
    def __init__(self):
        self.name='Tom'
        self.age=28
        print 'A init'
    def add(self):
        print ' in objectA '
class ObjectB(ObjectA):#父亲类
    def __init__(self):
        # super(ObjectB,self).__init__()
        ObjectA.__init__(self)
        self.sex='nan'
        print 'B init'
    def add(self): #就近原则
        print 'in objectB'
    def update(self):
        print 'in objectB'
b =ObjectB()
b.add()
print '-----------------------'
class ObjectC(ObjectB):#子类
    def __init__(self):
        # super(ObjectC,self).__init__()
        ObjectB.__init__(self)
        self.citty='chengdu'
        print 'C init'
    def add(self):
        print 'in ObjectC()'
    def delete(self):
        print "in objectC"
    def print_all(self):
        return '%s:%s:%s:%s'%(self.name,self.age,self.sex,self.citty)
class ObjectD(ObjectB):
    pass
a = ObjectA()
b = ObjectB()
c = ObjectC()
d = ObjectD()
c.add()
print c.print_all()
print '-------------------------->'
import types
print isinstance(a,list) #flase
print isinstance(a,ObjectA) # true
print a
print b
print id(a) is id(b)
# print hasattr()
print '------------------------->'
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
my =MyObject()
print hasattr(my, 'power') # 有属性'x'吗？
print getattr(my,'power')
# print setattr()
# print getattr(my,'y')


