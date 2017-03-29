#coding:utf-8
s = 'lession'
print s[0:3:2]
print s[::-1]
print s[-5:-1]
print s[-5:-1:2] #s['初始值':'结束值':'步数']
print '----------------->'
list =range(10)
print list #3种 del  remove pop
list.pop(2)
print list
list.remove(8)
print list
del list[3] #list里面删除的值为下标
print list
# insert  append  exclud  拼接
list2=list + [4,5]
print list2
print '--------------------->'
t = tuple(list)+(4,5)#元组里面内容是不可更变的
print type(t)
a = (1,)             #定义单元素元组的时候,后面必须加, __get...__
print type(a)
print len(a)
print '-------------------->'
map ={'name':'zhangsan','age':28}
print map.keys()
print map.values()
print map.iteritems()
print map.items()
print map.items()[0][0]
''' ''' ' ' """ """
string = """hello word"""

print '------------------------------'
print 9.8//4  # 想下取整
print '------------------------->'
# 600-630  重本 550 600 本科   550以下 专科
num =620
if 600 <= num < 630:
    print u'重本'
elif 550 <= num <600:
    print u"本科"
else:
    print u'专科'

print '--------------------------->'
sumer=0
for i in range(101):
    sumer +=i
print sumer
print '--------------------------->'
# num = 1
# s = 0
# while True:
#     num += 1
# 	if num > 100:
# 	    break
# 	s +=num
# print s
# a=0
# while a<100:
#     'TODO'
#     pass

red_boll=range(1,33)
blue_boll=range(1,17)
print red_boll
print blue_boll
import random
print random.choice(red_boll)
list =[]
while len(list)<7:
    if len(list)<6:
        red = random.choice(red_boll)
        list.append(red)
        red_boll.remove(red)
    else:
        list.append(random.choice(blue_boll))
print list