# -*- coding:utf-8 -*-

# 继承


class Student(object):

    def __init__(self):
        print ' init1 '
    # 增删改
    def add(self):
        print 'in add1'

    def update(self):
        print 'in update1'

    def delete(self):
        print 'in del1'


class updateShu(Student):

    def __init__(self):
        # super(updateShu,self).__init__()
        Student.__init__()
        print 'init 2'

    def add(self):  # 如果子类里面有何父类里面相同函数,子类的函数会默认重载掉父类的函数

        print 'in add2'

    def find(self):

        print 'in find2'

#
# s = Student()
#
# s.add()
# s.find()  # 父类是调用不到子类里面的参数的

upstu = updateShu()
# upstu.add()
# upstu.update()
# upstu.delete()

# class shuji(object):
#
#     def shuju(self):
#         pass
#
#     def yuwen(self):
#         pass
#
#     def waiyu(self):
#         pass
#
#     def add(self):
#         print 'in shuji'


# class Student2(shuji, updateShu):
#     pass




# print '------------------>'
# s2 = Student2()
# s2.add()  # -->  add2 or shuji  多继承里面方法都有相同的时候,谁在前面取那个
# s2.yuwen()
# s2.update()

# 双色球
class shuangseqiu:
    def __init__(self):
        pass
    def quhongqiu(self):
        pass
    def qulanqiu(self):
        pass
    def fangruwenjian(self):
        pass