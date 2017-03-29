# coding:utf-8


# 封装: 属性私有 ,公共 , 受保护 (2.7 防止from注入)
# 对象,万物皆对象
# 它可以是 数据类型, 类, 函数 ---->  参数传递
class A(object):
    a = 1

    def __init__(self):
        self.a = 1
        self.__age = 20
        self._name = 'lily'

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def __set(self):
        pass


class B(A):
    def __init__(self):
        super(B, self).__init__()
        self.b = 2

    def get_age(self):
        return self.b
    pass

a = A()
b = B()
# print dir(A)
# print A.a
# print a
# print b.b
# print a.get_age()
# a.set_age(21)
# print a.get_age()
# print a._A__age

#  描述符(作业)

class B(object):
    a=1
    def add(self):
        print 'info add B'

class C(object):
    a=1
    def add(self):
        print 'info add C'

def move(m):
    m.a
    m.add()

move(C())
move(B())
# print C()
# print B()
# print move
# x = 1
# print x


class D(object):
    a = 1

    @classmethod
    def update(cls):
        print 'info up'

    @staticmethod
    def static():
        print 'info static'

    def add(self):
        pass

print D.a
D.update()
D().static()
D().update()