# coding:utf-8


# 上下文自由获取

def make_adder(x):  # 100

    # print 'x is :',x  # adder函数全局变量

    def adder(y):

        # print 'y is:',y # 12

        return x+y

    return adder


def make_adder1(x):

    return x

m1 = make_adder(100)(12)  # 实例当前函数的时候

# print '---->',make_adder(100)(12)
# m1 = adder()
# m1(23)

# print m1(23)
print m1

print type(m1)

m3 = make_adder1

print m3
print m3(100)

# m2 = make_adder1(100)
#
# print type(m2)
