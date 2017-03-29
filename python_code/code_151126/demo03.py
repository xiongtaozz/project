#coding:utf-8
import chardet
import sys
import urllib
print sys.getdefaultencoding()
s ='中文'.decode('utf-8').encode('gbk')
print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
print s
def getCharset(s):
    return chardet.detect(s)['encoding']
print getCharset(s)
print ord('a')
print chr(65)

