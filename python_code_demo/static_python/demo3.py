# -*- coding:utf-8 -*-

l = range(10)
x, y = 1, 2

w = x if x > y else y  # x 可看成一个新生成变量
# if x > y:
#     print x
# else:
#     print y
print '----------------'
f = [x for x in l if x > 5]  # [x+y for x in l for y in l]
print w
print f

sumer = 6

print sumer == sum([x for x in range(1, 6) if 6 % x == 0])
