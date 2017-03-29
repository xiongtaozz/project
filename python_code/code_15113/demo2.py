#coding:utf-8

#最简单的写法
print sum(range(1,101))
#for 循环实现
sumer=0;
for i in range(1,101):
    sumer +=i
print sumer
#while 循环实现
i = 1
sumer=0
while i<101:
    sumer +=i
    i +=1
print sumer
#特殊语法实现 reduce + lamdba
print reduce(lambda x,y:x+y,range(1,101))
#函数过程式写法
def add(x,y):return x+y
print reduce(add,range(1,101))