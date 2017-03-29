# coding:utf-8


# class Box(object):
#
#     def __init__(self, length, width, height):
#         self.length = length
#         self.width = width
#         self.height = height
#         self.__proportion = length * height * width
#
#     def proinfo(self):
#
#         return self.__proportion
#
# b = Box(1, 2, 3)
#
# for x in range(5):
#     if x == 0:
#         print b.proinfo()
#     else:
#         b.__init__(1+x, 2+x, 3+x)
#         print b.proinfo()
#     # print b.proinfo()

# import os
# a = '中文'
# os.makedirs(a.decode('utf-8'))

# at = raw_input()
# print a.decode('GBK')


# import re
#
# a = "您的IP是：[112.44.101.123] 来自:四川省成都市    移动"
# reg = re.compile(r"(\d+.\d+..\d+.\d+).*?来自:(.*?)[\s]+(.+)")
# item = re.findall(reg, a)
# print item
# for content in item:
#     print content[0]
#     print content[1]
#     print content[2]

# l = [12, 24, 32, 28, 25, 60, 48, 9, 15]
# l.sort()
# print len(l)
# s = []
# for x in range(len(l))[::-1]:
#     n = -1
#     c = len(l) % 2
#     # if len(l) % 2 == 1:
#     #     c += 1
#     if len(s) == 0:
#         s.append(l[x])
#     elif len(s) % 2 == 0 and x != c:
#         s.append(l[n])
#         n += -2
#     elif len(s) % 2 == 1 and x != c:
#         s.append(l[x])
# print s
# l1 = l[0::2][::-1]
# l2 = l[1::2][::-1]
# print l1
# print l2
# # for x in range(len(l)):
# #     if len(s) % 2 == 0:
# #         s.append()

# a = [12, 3, 5]
# a = list(reversed(sorted(a)))
# print a
# a_len = len(a)
# ha_len = a_len/2 + 1
# print ha_len
# if ha_len < 5:
#     ha_len += 1
# for i in range(1, ha_len+1, 2):
#     a.insert(i, a.pop())
# print a




class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def __add__(self,oth):
		return Point(self.x + oth.x , self.y + oth.y)

	def info(self):
		print(self.x,self.y)

class D3Point(Point):
	def __init__(self,x,y,z):
		super(D3Point,self).__init__(x,y)
		self.z = z

	def __add__(self,oth):
		return D3Point(self.x + oth.x , self.y + oth.y , self.z + oth.z)

	def info(self):
		print(self.x,self.y,self.z)

class D3Point2:
	def __init__(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z

	def __add__(self,oth):
		# return D3Point2(self.x + oth.x , self.y + oth.y , self.z + oth.z)
		return self.x + oth.x , self.y + oth.y , self.z + oth.z

	def info(self):
		print(self.x,self.y,self.z)

def myadd(a,b):
	return a + b


if __name__ == '__main__':
	myadd(Point(1,2),Point(3,4)).info()
	myadd(D3Point(1,2,3),D3Point(4,5,6)).info()
	myadd(D3Point2(1,2,3),D3Point(4,5,6)).info()