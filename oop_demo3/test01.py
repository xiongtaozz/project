# -*- coding:utf-8 -*-
"""
    author : XT
    date   : 2016-3-7
    闭包: 如果在一个内部函数里,对在外部作用域(但不是在全局作用域)的变量进行引用,那么
    函数就被认为是闭包.
    闭包 = 函数块 + 定义函数时环境,adder就是函数块,x就是环境.当然这个环境可以使用很多,
    不止一个简单的x
    注意: 闭包中是不能修改外部作用域的局部变量的
    作用:
        当闭包执行完后，仍然能够保持住当前的运行环境。
        闭包可以根据外部作用域的局部变量来得到不同的结果
    参考资料:http://www.cnblogs.com/blueel/archive/2012/12/28/2837673.html
"""

# <name> 表示函数对象, () 函数调用
def w():
    pass

print w
def a():
    pass
# a()
# print a()  # None
# print a
# b = a
# print b

# 函数嵌套 ---> 函数里面在嵌套函数
# 内嵌套
# 外嵌套
# def e():
#     pass
#
# def a(f):
#     def b():
#         pass
#     def c():
#         pass
#     f()
# a(e)


# 假设 y值 我必须从函数外传入 ,那么应该怎么办?
def a(x):
    print x

    def b(y):
        return x + y
    return b

c = a(10)
print c(15)
# c 对象,对象包涵了x = 10 变量
print c(25)
print a(10)(20)


def addx(x):  # 函数嵌套
    # print x

    # 在函数内部再定义一个函数，其实这个里面的函数就被认为是闭包
    def adder(y):
        # 这里打印一下y变量，以便大家可以更清楚传进来的变量时哪一个
        # print y
        return x+y
    # a = adder(1)  # adder必备参数是变动
    # 其实这里返回的就是闭包的结果
    return adder

c = addx(8)  # 生成新的对象,而且包涵x c环境(多个)
print c
print c(10)  # x=8 y=10
print c(20)  # x=8 y=20
# # print c(10)
print addx(10)(15)
print c(20)

# 给addx函数赋值，这个8就是给参数x
# c = addx(8)
# print c
# # 注意这里的10其实给参数y
# print c(10)
# print c(20)  # 当闭包执行完后，仍然能够保持住当前的运行环境。


