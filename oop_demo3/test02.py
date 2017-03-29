# -*- coding:utf-8 -*-

"""
    @author:XT
    @date  : 2016-3-7 09:56:28
    主题:迭代器
    概念:迭代器是访问集合元素的一种方式。迭代器对象从集合的第一个元素开始访问，
    直到所有的元素被访问完结束
    优点:对于原生支持随机访问的数据结构(如:tuple,list),迭代器和经典for循环索引
    访问相比并无优势,反而失去了索引值(可以使用内建函数enumerate()找回索引值),但对
    无法访问的数据结构(如:set)而言,迭代器是唯一的访问元素方式
    迭代器两个基本方法:
    next方法:返回迭代器的下一个元素
    __iter__方法:返回迭代器对象本身
    list = [1,2,3,4,5] ---iter
"""
# 2.7 raw_input('>') ---> int(str) 3.x input('>') 自动转换对应类型
# inp = int(raw_input('>'))
# if sum([x for x in range(1, inp) if inp % x == 0]) == inp:
#     print True
# for x in str: pass
#  [1,2,3,4,5]
#   0 1 2 ..
#   迭代器当中没有索引值
# 斐波那契数列
'''
直接在函数fab(max)中用print打印会导致
我函数的课复用性变差,因为fab返回None,其他函数无法获得fab函数返回的数列
'''


def fab(max):
    l = []
    n, a, b = 0, 0, 1
    while n < max:
        # print b
        l.append(b)
        a, b = b, a + b
        n += 1
    return l
print fab(5)
# 既然返回不了,那么我们可以这样

' 代码是满足了可复用性的需求,但是占用了内存空间,不建议 '


# def fab(max):
#     L = []
#     n, a, b = 0, 0, 1
#     while n<max:
#         L.append(b)
#         a, b = b, a+b
#         n += 1
#     return L

# 那么为了改变以上需求,咱们可以自定义迭代器


class Fab(object):

    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def next(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n += 1
            return r
        raise StopIteration()  # 手动抛出异常
# for key in Fab(5):
#     print key

from itertools import *  # python 内置迭代器库
a = cycle('ABCD')  # 单一方法
# print a
# print a.next()
# print a.next()
# print a.next()
# print a.next()
# print a.next()
# print a.next()

p = product('ABCD', repeat=2)  # 组合查询
# print p.next()
# print p.next()
# print p.next()
# print p.next()
# print p.next()
pe = permutations('ABCD', 2)  # AB AC
# print pe.next()
# print pe.next()
# print pe.next()
# print pe.next()
# print [p[0]+p[1] for p in list(pe)]  # 列表表达式

"""
    生成器:
    带有 yield 的函数在 Python 中被称之为 generator（生成器），
    几个例子说明下（还是用生成斐波那契数列说明)
"""


def fab(max):  # 生成器是否可迭代
                # 也就是说迭代器里面所有方法,
                # 在生成器里面是完全可以使用
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n += 1
# 通过循环是可以实现当前的结果,
# 注意:并一定所有的迭代器和生成器都是可以通过for处理的
# for key in fab(5):
#     print key
#  我们也可以手动调用next方法
f = fab(3)
# print f.next()
# print f.next()
# print f.next()
# print f.next()  # 越界的时候会出现 StopIteration 异常

# 注意:在一个生成器中，如果没有return，则默认执行到函数完毕；
# 如果遇到return,如果在执行过程中 return，则直接抛出 StopIteration 终止迭代
# 生成器对象支持几个方法,如gen.next(),gen.send(),gen.throw()等.
# gen.throw() 异常处理
import types


def gen():
    for x in xrange(4):  # 0 1 2 3
        tmp = yield x   # 在生成器 里面默认是存储的是两个值  >> none 0 > none 1 > hello 2
        if tmp == 'hello':  # tmp 交互口令
            print 'world'
        else:
            print tmp

g = gen()
print g   # <generator object gen at 0x02801760>
print isinstance(g, types.GeneratorType)  # True
print g.__class__
print dir(g)  # help __doc__
# print g.next()  # none  0
# print g.next()  # none  1
print g.send('hello')  # hello 2 生成器可以使用send 方法和外界交互
print g.throw()
# print g.send('hello')

# 注意：宁可有大量简单的可迭代函数，也不要一个复杂的一次只计算出一个值的函数。