#coding:utf-8

# def add(x):
#     print x
#
# add(1)
class objectA():
    count =0
    def add(self,name):
        self.name=name
        print name
    def update(self):
        print 'update``'
    def delete(self):
        print 'del...'
# a = objectA() #实例变量
# a.add(1)
# a.delete()
# a.update()
class objectB(objectA):
    def add(self,name):
        print 'class B'
a = objectA()
a.add(2)
b= objectB()
b.add(1)