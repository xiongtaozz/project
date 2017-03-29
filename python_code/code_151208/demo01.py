# coding:utf-8

a = 0
a = 'abc'
b = 'str'
print a,b
print type(a),type(b)
c, d, e = 1, 2, 3
print c, d, e
e, d, c = c, d, e
print c, d, e
print '--------------->'
a = 'Hello World!'
#    012345
print a[::-1]  #a[start:end:增] start>=  end < step
list = range(10)
print list[1::2]
list.append(11)
print list+[12]
list[5] = 20  # 下标,还是内容 -->下标
print list
list.pop() # 默认删除最后一个
list.remove(8)# 内容为8
del list[5] # 删除的是下标
print list
print u'---------tuple元组----------------'
t = tuple(list) # [] --list --()
print t
a = 1,
print type(a),'str'
print '%s %s'%(1, 2)
print 1, 2
print u'----------字典--------------'
map = {'name':'Tom','age':28} #key value
print map.keys()

print map.values()
print map.items()
print map.items()[0]
print map.items()[0][1]
print map.get('age')
print map['age']
print 'l' * 30
#  if  elif else
#   600 -->630  重本 600-->550 本科 500以下
# num = int(raw_input(u'请输入考试分数>'))
# if 600 <= num < 630:
#     print u'重本'
# elif 550 <= num < 600:
#     print u'本科'
# else:
#     print u"专科"

# for x  in  可循环: ---->
sumer=0
for x in range(101):
    sumer +=x
print sumer

# while () : -->
a =0
sumer = 0
while a<101:
    sumer += a
    a += 1
print sumer

a= 0
# while True:
#     a += 1
#     print a
#     if a == 100:
#         pass #占位符
def add():
    pass


import random
red_boll = range(1,33)
blue_boll = range(1,17)
print red_boll
print blue_boll
print random.choice(blue_boll)# [1,2,3,4,5,6,7]

