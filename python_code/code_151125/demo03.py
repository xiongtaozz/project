#coding:utf-8
# def add():
#     pass
# def update():
#     pass
class Student:
    countName='chengdu'
    def __init__(self,name,age):
        print 'init'
        self.name=name
        self.age=age
    def get_name(self):
        print '%s:%s'%(self.name,self.age)
    def set_age(self,age):
        if age < 0 or age > 100:
            raise ValueError('age is')
        elif not isinstance(age,int) :
            raise ValueError('integer')
        else:
            self.age=age
    @classmethod
    def getClass(self):
        print 'get class'
    @staticmethod
    def getStatic(cls):
        print 'static',Student.countName
s1 = Student('Tom',28)
# s.set_age(50)
# s1.__init__('Lily',27)
s1.get_name()
# Student.getClass() #类本身调用调用本身的方法
# Student.getStatic('sss')
s2 = Student('Jack',25)
s2.get_name()