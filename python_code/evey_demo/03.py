#coding:utf-8
import types

def gen():
    for x in xrange(4):
        tmp = yield x
        if tmp == 'hello':
            print 'world'
        else:
            print str(tmp)
g=gen()
print g
print isinstance(g,types.GeneratorType)
print g.next()
print g.next()
print g.send('hello') #world  2

