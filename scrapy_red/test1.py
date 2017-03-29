# coding:utf-8


class A(object):

    def update(self):
        print 'info A'


class B(object):
    def update(self):
        print 'info B'

print id(A)
print id(B)


def move(m):  # 可接收 数据类型{int,float,tuple} --对象
    # print m
    m.update()
    # m.add()

    pass

class Ac(object):
    a=1

class Ab(object):
    a=2


class myFactry(object):
    def get_ins(self, ins):
        return ins()

if __name__ == "__main__":
    # print c
    print myFactry().get_ins(Ac).a
    # pass
    # A().update()
    # # a = A()
    # # a.update()
    # b = B()
    # # print a
    # # move('sss')
    # move(A())
    # move(b)