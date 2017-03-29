# coding:utf-8
import re

r = re.compile('([1][3|5|8][0-9]{9})]')
s = '13018023432324'
p = re.findall(r, s, 0)
print p
