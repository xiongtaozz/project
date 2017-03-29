# coding:utf-8
import os
import sys
import time
import random as r


# s = 'http://img0.pchouse.com.cn/pchouse/corp/1506/30/logo.jpg'
# print s.split('/')[-1]
fname = 'D:/workbase/py06921/py_2016929\qiangzhi'
print os.path.join(os.path.dirname(__file__), "qiangzhi")
# print dir(os)

print time.strftime("%y-%m-%d %H:%M:%S", time.localtime(time.time()))  # long


print r.choice(range(1, 17))
print r.sample(range(1, 33), 6)