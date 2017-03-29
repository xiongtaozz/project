#coding:utf-8
a='A'
print ord(a)
b=97
print chr(b)
print u'ABC'.encode('utf-8')
print u'中文'
print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

import base64
s1 = 'hello'
print s1
s2 = base64.b64encode(s1)
print s2  # out: aGVsbG8=
print '---------------------------------------->'

import chardet

def toHexString(s):
    return ":".join("{0:x}".format(ord(c)) for c in s)

def getCharset(s):
    return chardet.detect(s)['encoding']

s = '你好'
print getCharset(s)
s1 = s.decode('utf-8').encode('gb2312')
print getCharset(s1)

import sys
print sys.getdefaultencoding()