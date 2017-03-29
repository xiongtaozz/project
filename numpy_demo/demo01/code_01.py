# coding:utf-8

import numpy
import sys
import time

# 1) 单纯Python代码写法


def pythonsum(n):
    a = range(n)
    b = range(n)
    c = []

    for i in range(len(a)):
        a[i] = i ** 2
        b[i] = i ** 3
        c.append(a[i] + b[i])

    return c


# 2) 使用numpy的代码


def numpysum(n):
    a = numpy.arange(n) ** 2
    b = numpy.arange(n) ** 3
    c = a + b

    return c


size = 1000

start = time.time()
c = pythonsum(size)
delta = time.time() - start
print "The last 2 elements of the sum", c[-2:]
print 'pythonsum elapsed time in microseconds', delta
start = time.time()
c = numpysum(size)
delta = time.time() - start
print "The last 2 elements of the sum", c[-2:]
print "numpysum elapsed time in microseconds", delta