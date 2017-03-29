# -*- coding:utf-8 -*-
# [start:end:vlaue] start 起始值 end 结束值 value 步长
s = '218916754'  # 起始值 0 1 2 3
# 字符串当中 起始值和结束值同时存在的时候, 他是半开半闭 start>= s > end
# print s[1::2]
# print s[::-1]
# print s[1:]
# s = s[1:]
# print s[1:]+s[:1]
# sumer = ''
# while True:
#     sumer += s[:1]
#     if len(s) > 1:
#         s = s[2:]+s[1:2]
#     else:
#         break
# print sumer

inp = int(raw_input('>'))
print inp
'''
完数:因子数之和 == 本身 ,说明它就是完数
分子数
因子数 = inp%分子数 == 0
'''
print range(1, int(inp))
l = []
for x in range(1, int(inp)):
    if int(inp) % x == 0:
        l.append(x)
print l
print sum(l)
if int(inp) == sum(l):
    print '完数'

print inp == sum([x for x in range(1, inp) if inp % x == 0])

'''
 [x for x in inp if x else 0] :列表推导式
'''



# def add():
#     print 111
#
# add()

# if __name__ == '__main__':
#     add()
