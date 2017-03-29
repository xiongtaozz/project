#coding:utf-8

a =range(1,5)
print a.reverse()
print a
print '------------------->'
class people(object):
    name='Lily'
    __age = 28
    def __init__(self):
        print u'初始化'
    @classmethod
    def add(self):
        print 'this add'
    def __addprv(self):
        print u'方法私有的'
    @staticmethod
    def staticadd():
        print people.name
    def __del__(self):
        print u'回收'
p = people()
print p.name  #实例化的方式
print people.name  #通过类方式来获取
print people._people__age
p.add()
people.add()
print '--------------------------->'
print p._people__addprv()
p.staticadd()
