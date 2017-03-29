#coding:utf-8


#输入一个数字 ,判处出它在哪个线上  630以上 重本  600-630 本科, 550 -600 二班  480 -550 专科  480以下 职业学校

# num = int(raw_input(u'请输入你的分数:'))
#
# print num
#
# if num > 630 :
#     print u'重点大学'
# elif num>600 and num<630:
#     print u'一本'
# elif num > 550 and num <600:
#     print u'二本'
# else:
#     print u'专科'

#循环 for  while   1+2+3..100
sumer=0
for i in range(1,101):
      sumer += i
print sumer
i =1
sumer=0
while (i<101):
    sumer +=i
    i +=1
print sumer

a=1
sumer=0
num= 0
while (a<101):
    if (a%2==0):
        sumer +=a
    a +=1
    if sumer > 400:
        # num +=1
        pass
    if(sumer > 1000):
        break
    if sumer <> 500:
        continue

print sumer,num

import random
# 双色球 2组
read_boll=range(1,33)
blue_boll=range(1,17)
print read_boll
print blue_boll
print random.choice(read_boll) # 6 + 1