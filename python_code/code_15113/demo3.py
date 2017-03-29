#coding:utf-8
a = 'hello word'
print '---',a

a,b,c = 1,2,3
c,b,a= 1,2,3
a,b=1,2
a =str(a)
print a
# list tuple 字典
print '-------------------------------'
list =range(10);
print list
del list[1]
print list
list.pop(0)
print list
list.remove(4) # 2.7.x append
t=tuple(list)
print t[0]


map ={'name':'zhangsan','age':30} #key value
print map.get('name')
print map.items() #list tuple [(),()]
for k,v in map.iteritems():
    print k
    print v
print map.iteritems(),map.iterkeys(),map.itervalues()


#  600-630 一本 550-600 二本 , 550以下 专科  750
# num = int(raw_input(u'输入高考分数:'))
#
# if num >= 600 and num <630 : # and 且 or 或
#     print u'一本'
# elif num >= 550 and num <600 :
#     print u'二本'
# else:
#     print u'专科'

# a =a+1 -->a+=1  //=

print '----------------------'
print list
a= 2
print a in list

#for while
sumer=0
for i in range(1,101):
    sumer +=i
print sumer
#while
i=1
sumer=0
while (i<101):
    sumer +=i
    i +=1
print sumer

print '------------------------'


i=0
while True:
    i +=1
    print i
    if i==50:
        pass
    if i==51:
        break

# 使用基本语法写出双色球 开奖作业： red blue
# 引用 random 模块库  用到 range（）函数
import random
red_boll=range(1,33)
bule_boll=range(1,17)
print red_boll
print bule_boll
print random.choice(red_boll) #[1,2,3,4,5,6,7]
