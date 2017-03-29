# -*- coding:utf-8 -*-

# 定义方法
def add():
    print 'hello!'
    return

# 类和实例
class Hello():
    # name = ''  # 安全性问题
    # name = 'Lily'

    def __init__(self,name,age): # 构造函数
        #  双闭合双下滑 都系统函数
        print '--init---'
        self.__name = 'Tom'   # __修饰私有的
        self.__age = age

    @classmethod  # 告诉它 它是类的一个方法
    def add(cls):

        print 'in add'

    @staticmethod
    def statadd(email):
        print 'in static ',email

    def get_all(self):
        print 'Get--> ', self.__name, self.__age

    def set_all(self, name, age):
        self.__age = age
        self.__name = name

    def __private(self):
        print 'in private ',self.__name
    pass

h = Hello('Tom',28)  # 类实例  类对象
# print h
# print Hello
# h.name = 'Tom'
# print h.name,h.age
h.add()

# 安全性  共有 私有
h.__name = 'Jack' # 类实例  __ 类,共有变量

print h.__name

h.get_all()
# h.set_all('Lily',25)
h.__init__('Lily', 25)
h.get_all()

# 修饰符
# print h._Hello__name
Hello.add()
Hello.statadd('11@qq.com')



