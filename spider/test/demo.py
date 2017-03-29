# -*- coding: utf-8 -*-
import re
import string
#密码 6位以上
# 一. 判断字符串是否是全部小写字母
s1 = 'adkkdk'

s2 = 'abc123efg'

print string.replace(s1,"dk","",1)
# an = re.match('[a-z]+$', s1)
# if an:
#     print 's2:', an.group(), u'全为小写'
# else:
#     print s2, u"不全是小写！"

# an = re.search('^[a-z]+$', s1)
# print an
# if an:
#     print 's1:', an.group(), u'全为小写'
# else:
#     print s1, u"不全是小写！"


# m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
# m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
# print m.group('first_name')       # The entire match

# 二、使用group用于把匹配结果分组
# a = "123abc456"
# print re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(0)          #123abc456,返回整体
# print re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(1)          #123
# print re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(2)          #abc
# print re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(3)          #456
# # 三、给匹配的分组命名
# a = "123abc456"
# pattern = re.compile("(?P<n1>[0-9]*)(?P<n2>[a-z]*)(?P<n3>[0-9]*)")
# print pattern.search(a).group()      #123abc456,返回整体
# print pattern.search(a).group('n1')
# print pattern.search(a).group('n2')
# print pattern.search(a).group('n3')
# # 四、去掉数字中的逗号
sen = "abc,123,456,789,mnp"
p = re.compile("\d+,\d+?")
for com in p.finditer(sen):
    mm = com.group()
    print "hi:", mm
    print "sen_before:", sen
    sen = sen.replace(mm, mm.replace(",", ""))
    # sen = re.sub(mm ,re.sub(',', '', mm), sen)
    # sen, number = re.subn(mm, re.subn(',', '', mm)[0], sen)
    print "sen_back:", sen, '\n'
# 五、一个采集例子中实际的应用
