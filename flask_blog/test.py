# -*- coding: UTF-8 -*-
import math                                   #导入开平方所需的包

def PrimeFactor(n):
    sum=0
    for i in range(1,int(math.sqrt(n))+2):  #质因子不会大于sqrt(num))+1
       if n%i==0:
           sum=sum+i                           #将质因子累加
    if n==sum:
        print("这个数是完数")                #如果累加之和与原数相等即为完数
    else:
        print("这个数不是完数")              #否则不是完数

num=input(u"请输入一个整数:")                  #输入一个整数
print (type(num))
PrimeFactor(int(num))