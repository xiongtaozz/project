# coding:utf-8

from numpy import *

print dtype('f8')

# print sctypeDict.keys()

# t = dtype('float64')
# print t.char
# print t.type
# print t.str

t = dtype([('name', 'str_', 40), ('numitems', 'int32'), ('price', 'float32')])
print t
print t['name']
itemz = array([('Meaning of life DVD', 42, 3.14), ('Butter', 13, 2.73)], dtype=t)
print itemz[1]

# numpy 切片

m = arange(9)
print m[3:7]
print m[:7:2]
print m[:2:-1]

# reshape 切成三维数组
b = arange(24).reshape(2, 3, 4)
print b
print b.ravel()
print b.flatten()

