# -*- coding:utf-8 -*-
# def bonus_total(n):
#     if n<=100000:
#         m=n*(10/100)
#         print(u"利润(I)低于或等于10万元，奖金为："+str(m))
#     if 100000<n<=200000:
#         m=100000*(10/100)+(n-100000)*(7.5/100)
#         print(u"利润高于10万元，低于20万元，奖金为："+str(m))
#     if 200000<n<=400000:
#         m=100000*(10/100)+100000*(7.5/100)+(n-200000)*(5/100)
#         print(u"利润20万到40万之间，奖金为："+str(m))
#     if 400000<n<=600000:
#         m=100000*(10/100)+100000*(7.5/100)+200000*(5/100)+(n-400000)*(3/100)
#         print(u"利润40万到60万之间，奖金为："+str(m))
#     if 600000<n<=1000000:
#         m=100000*(10/100)+100000*(7.5/100)+200000*(5/100)+200000*(3/100)+(n-600000)*(1.5/100)
#         print(u"利润60万到100万之间，奖金为："+str(m))
#     if n>=1000000:
#         m=100000*(10/100)+100000*(7.5/100)+200000*(5/100)+200000*(3/100)+400000*(1.5/100)+(n-1000000)*(1/100)
#         print(u"利润高于100万元，奖金为："+str(m))
#
# profit=int(input("please enter the profit in this month:"))
# bonus_total(profit)

#判断完数函数
def perfect_number(x):
    sum=0
    for i in range(1,x):
        if x%i==0:
            sum=sum+i
    if sum==x:
        return True
    return False
while True:
    x=int(input("Please enter number:"))
    n=perfect_number(x)
    if n==True:
        print(str(x)+" is a perfect number")
        continue
    else:
        print(str(x)+" is not a perfect number")
        continue
