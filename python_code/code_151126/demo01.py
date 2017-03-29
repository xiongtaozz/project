#coding:utf-8

import hashlib

md5 = hashlib.md5()
md5.update('123456')
print md5.hexdigest()
def Lonig(passd):
    pwd =plus('e10adc3949ba59abbe56e057f20f883e')
    if passd == pwd:
        print 'OK'

def plus(pwd):
    return pwd+'django'

Lonig(plus('e10adc3949ba59abbe56e057f20f883e'))