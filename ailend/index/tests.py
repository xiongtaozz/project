# coding:utf-8
from django.test import TestCase

# Create your tests here.
# import time
# str1 = '201603300001'
# print time.strftime('%Y%m%d', time.localtime(time.time()))

import string as str


# class js:
#     def __init__(self, a):
#         self.a = a
#
#     def zimu(self):
#         count1 = 0
#         for a1 in self.a:
#             if a1.isalpha() is True:
#                 count1 += 1
#         print count1
#
#     def kongge(self):
#         count2 = 0
#         for a2 in self.a:
#             if a2.isspace() is True:
#                 count2 += 1
#         print count2
#
#     def shuzi(self):
#         count3=0
#         for a3 in self.a:
#             if a3.isdigit() is True:
#                 count3 +=1
#         print count3
#
# p = js(raw_input(u"请输入字符串："))
# p.kongge()
# p.shuzi()
# p.zimu()

char=['赵','钱','孙','李','佘']
char.sort()
for item in char:
    print item.decode('utf-8').encode('gb2312')

