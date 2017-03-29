# coding=utf-8


class switch(object):
    def __init__(self,value):         # 初始化需要匹配的值value
        self.value = value
        self.fall = False             # 如果匹配到case中语句没有break，则fall为true

    def __iter__(self):
        yield self.match              # 调用match方法，返回一个生成器
        raise StopIteration           # StopIteration 异常来判断for循环是否结束

    def match(self, *arga):           # 模拟case 子句的方法
        if self.fall or not arga:     # 如果fall 为true，则继续执行下面的case 子句
            return True               # 或case 子句没有匹配项，则流转到默认分支
        elif self.value in arga:      # 匹配成功
            return True
        else:                         # 匹配失败
            return False

operator = "*"
x = 1
y = 2

for case in switch(operator):         # switch 只能用于for in 循环中
    if case ('+'):
        print x +y
        break
    if case ('-'):
        print x-y
        break
    if case ('*'):
        print x *y
    if case ('/'):
         print x/y
         break

    if case ():
         print ""
