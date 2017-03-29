# coding:utf-8
import re

# str = 'dkajsdal222dK'
#
# an = re.search('[a-z]+$', str)
# print an
# if an:
#     print(1111)
# else:
#     print(2222)


raw = raw_input('>')
if int(raw) == sum([x for x in range(1, int(raw)) if int(raw) % x == 0]):
    print u'完数'
else:
    print u'不是完数'
