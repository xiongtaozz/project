# coding:utf-8

import urllib2
import os
import time
print int(time.time())
# url = 'http://www.maiziedi.com'
#
# response = urllib2.urlopen(url)
# print response.read()

items = [('111', '中文'), ('1111', '中文1'), ('11111', '中文2')]
print items[1][0]

for item in items:
    print item[1].decode('utf-8')
    path = item
#     p = 'C:\Users\Administrator.USER-20160812AM\Desktop'
#     if not os.path.exists(item[0]):
#         os.makedirs(p+item[0])
#
#     open(p+item[0]+'/'+item[0]+'.txt', 'w')



