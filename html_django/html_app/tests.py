# coding:utf-8
from django.test import TestCase

# Create your tests here.
try:
    a = int(raw_input('>'))
except ValueError as e:
    print u'错误'
else:
    if a == sum([x for x in range(1, a) if a % x == 0]):
        print 'ok'
    else:
        print 'no'

# for i in range(1, 10)[::-1]:
#         for j in range(1, i):
#             print "%d * %d = %d\t" % (j, i, j * i),
#         print "%d * %d = %d\n" % (i, i, i * i),

# d = {'a': '123', 'b': '234', 'c': '123', 'd': '235', 'e': '234'}

# from collections import Counter
# # m = Counter(d.values())
# # print m.items()
#
# # print list(set(d.values()))
# print dict([x for x in d.items() if x[1] in [m[0] for m in Counter(d.values()).items() if m[1] > 1]])


# l = [1,1,2,2,2,3,3,3,3,5,6,4,6,4,5,5,5]
# d1 = {}
# for x in set(l):
#     d1[x] = l.count(x)
# print d1

# l = [1, 2, 3, 1, 2, 3]
# for x in range(len(l)):
#     for j in range(x+1, len(l)):
#         if l[x] == l[j]:
#             print x, u'在下标', j, u'重复'


# comp_number = input(u'请输入一个数字：')
#
#
# def fuc(comp_number):
#     i = 1
#     sum_num = 0
#     for i in range(1, comp_number):
#         if comp_number % i == 0:
#             sum_num += i
#         i += 1
#     if sum_num == comp_number:
#         print(u'这个参数是完数')
#     else:
#         print(u'这个参数不是完数')
#
# fuc(comp_number)


# 读写操作
# 读
def find():
    file = open('test.txt')
    print file.read()
    file.close()


# 写
def write_f(r):
    file = open('test.txt', 'a+')
    file.write(r)
    file.close()


while True:
    r = str(raw_input(u'请输入内容:'))
    write_f(r+'\n')
    print u'------打印内容------->'
    find()

