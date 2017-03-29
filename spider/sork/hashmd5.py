#coding:utf-8
import hashlib
def getMd5(s):
    md5=hashlib.md5()
    md5.update(s)
    return md5.hexdigest()

print getMd5('654321')
# a8c0f09e173c00f4f49151e09cfd2db5