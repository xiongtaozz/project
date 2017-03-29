# coding:utf-8


# def fun(x): return x+x
# print fun(1)
# print lambda x: 1+1

# 过程式编程
L1 = [1, 2, 3, 4, 5]
L2 = []

for i in L1:
    if i > 3:
        L2.append(i)
print L2
print '-----------------'


# def func(x): return x > 3
# # lambda表达式里面是没有return的
# # filter 过滤
# print filter(lambda x: x > 3, L1)   # list tuple str
# filter(function_or_None, sequence)
# map(function, sequence)  # list
# reduce(function, sequence)
#  对某一列表内容取 * ** / + -
# print len(range(1, 8))
# print len(range(8, 16))
# # map(function, sequence1,sequence2,sequence3) sequence1 和 sequence2 长度是必须相等的
# print map(lambda x, y: x+y, range(1, 8), range(8, 15))
# print map(lambda x: x+x, range(1, 8))

print '-------------------'
# 1+2...+100
sumer =0
for i in range(1, 101):
    sumer += i
print sumer - 20


def func(x, y): return x+y
print reduce(func, range(101), -20)

