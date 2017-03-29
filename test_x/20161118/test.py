# coding:utf-8

# 输入任意数字,判断出他是否是完数  概念: 完数= 因子数之和 == 本身 它就是完数
# 例: 6 = 1 + 2 + 3

inp = int(raw_input(u'请输入数字>'))  # 接收输入值
# # 得到因子数
# i = 1    # 安全性的考虑,
l = 0
# while i < inp:
#     if inp % i == 0:   # % 取摸(去余数)
#         l += i         # = 赋值运算, += 叠加运算 -= *= 叠加
#     i += 1
# if inp == l:
#     print '%d 是完数' % l
# else:
#     print '{} 不是完数'.format(l)


print range(1, 6)  # 半开半闭

for i in range(1, inp):  # 2.7 和 3.x   2.7 range 列表 xrange 迭代器  3.x range tuple
    if inp % i == 0:
        l += i
if inp == l:
    print '%d 是完数' % l  # 格式化, %r '' %d  数字 %s str
    # %r 任何类型 他都会在 之前上上 '' or "" or """"""
    # %d 格式化值 必须是 int类型
    # %s 格式化值 必须是 字符串或者int
else:
    print '{} 不是完数'.format(l)

# 列表推导式
print sum([x for x in range(1, 6) if inp % x == 0])




