# coding:utf-8
import demo01
import pdb

# pdb.set_trace()
# a = 10
# b = 11
# c = demo01.add(a,b)
# print c

a=dict(a=1,b=2,c=3)
print a

map = {'key1':'value1', 'key2':'value2', 'key3':'value3'}

print '-----------dict-------------' #1
for d in map:
    print "%s:%s" %(d, map[d])

print '-----------item-------------' #2
for (k,v) in map.items():
    print '%s:%s' %(k, v)
#效率最高
print '------------iteritems---------' #3
for k,v in map.iteritems():
    print '%s:%s' % (k, v)
#最笨的方法
print '---------iterkeys---------------' #4
for k in map.iterkeys():
    print '%s:%s' % (k, map[k])

print '------------iterkeys, itervalues----------' #5
for k,v in zip(map.iterkeys(), map.itervalues()):
    print '%s:%s' % (k, v)