#coding:utf-8

class Pserion:
    name='Tom'
    __age=30
    def getName(self):
        return self.name,self.__age #[] ,{}
    def setName(self,name,age):
        self.name=name
        self.__age=age
p =Pserion()
print p.getName()
p.setName('Lily',25)
print p.getName()
print '------------------------>'
from collections import Iterable
import types
li =range(1,4)
print isinstance(111,Iterable)
print '----------------------->'
class MyIterator(object):
  def __init__(self, step):
      self.step = step
  def next(self):
      """Returns the next element."""
      if self.step==0:
           raise StopIteration('this') #手动抛异常
      self.step-=1
      return self.step
  def __iter__(self):
      """Returns the iterator itself."""
      return self
for el in MyIterator(0):
  print el
print '---------------生成器----------->'
def add():
    return 1
def gen():
    for x in xrange(4):
        tmp = yield x #(tmp,x)
        if tmp == 'hello':
            print 'world'
        else:
            print str(tmp)
g=gen()
a= add()
print a
print g   #<generator object gen at 0x02801760>
print isinstance(g,types.GeneratorType) #True
print g.next()
print g.next()
print g.send(None)
print g.send('hello')
print '--------------------------'
def stop_immediately(name):
    if name == 'skycrab':
        yield 'okok'
    else:
        print 'nono'
s=stop_immediately('skycrab')
s.next()
print '----------函数式,过程式------------'
#过程
def up():
    list =range(1,10)
    l=[]
    for l1 in list:
        l.append(l1)
#函数式
# def add(x):return x+x
# filter(add,range(1.5))
#map,reduce(),lambda
print "------------dic------------->"
import time
def timeit(func):
    """ doc """
    def water():
        start = time.clock()
        func()
        end = time.clock()
        print 'time is:',start-end
    return water()
@timeit
def foo():
    print 'in foo'
print '------------Factory--------------->'
#--->banane
# class Factory():
#     def find(self,fut):
#          if fut=='banane':
#              return Banane('banane')
#          else:
#              return Shuiguo()
#
# class Shuiguo():
#     def __init__(self):
#         print 'init'
#     def __str__(self):
#         print self
# class  Apple(Shuiguo):
#     def __str__(self):
#         print self
# class Banane(Shuiguo):
#     def __str__(self):
#         print self
# fac = Factory()
# fac.find('banane')
print '------------------------------>'
#闭包
a,b=1,2
a,b=b,a
def make_adder(addend): #23
    def adder(augend): #100
        print 'addend',addend
        print 'augend',augend
        return augend + addend
    return adder
p = make_adder(23)
q = make_adder(44)
print '---------',p
print '---------',q
print p(100) #123  #200
print q(100) #144  #200