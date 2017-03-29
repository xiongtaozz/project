#coding:utf-8
from collections import Iterable
list = range(10)
print isinstance(list,Iterable) #否是可迭代
print isinstance(111,Iterable)
print isinstance('aaa',Iterable)
print iter(list)
print '---------------------------->'
class MyIterator(object):
  def __init__(self, step):
      self.step = step
  def next(self):
      """Returns the next element."""
      if self.step==0:
           raise StopIteration
      self.step-=1
      return self.step
  def __iter__(self):
      """Returns the iterator itself."""
      return self
# for el in MyIterator(4):
#   print el
print '___________________________'
import types
def gen():
    for x in xrange(4):
        tmp = yield x # 0~3 ,状态
        if tmp == 'hello':
            print 'world'
        else:
            print str(tmp)
g=gen()
print g   #<generator object gen at 0x02801760>
print isinstance(g,types.GeneratorType) #True 生成器可以不迭代还是必须迭代
print g.next()
print g.next()
print g.send(None)
print g.send('hello')
# print g.throw()
# raise
print '------------------------------------>'
def make_adder(addend): #23
    print '-',addend
    def adder(augend):
        print '--',augend  # 100
        return augend + addend
    return adder
p = make_adder(23)
q = make_adder(44)
print p(100) #123  200
# print q(100) #144  200