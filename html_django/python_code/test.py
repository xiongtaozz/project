# -*- coding:utf-8 -*-

# import urllib2
import re

# print ("hello,word!")
# number_tuple = [1,3,5,7,9]  # 创建列表
# # print("number_list:" + str(number_list))
# string_tuple = ["abc","bbc","python"]  # 创建列表
# mixed_tuple = ["python","java",3,14]   # 创建列表
# # print("string_list:" + str(string_list))
# # print("mixed_list:" +str(mixed_list))
# second_num = number_tuple[1]   # 获取索引值为1 -->3
# third_string = string_tuple[2]  # 获取索引值为2 --->python
#
# fourth_mixed = mixed_tuple[3]   # 获取索引值3  --->14
# print("second_num:{0} third_string:{1} fourth_mixed:{2}".format(second_num, third_string,fourth_mixed))  # 字符串拼接
# number_tuple[1] = 30  # 更改number_tuple索引值为1  3--->30
# print("number_list after:" + str(number_tuple))  # --[1,30,5,7,9]
#
# del number_list[1]
# print("numeber_list after" + str(number_list))
# abcd_list = [ "a","b","c","d"]
# print(abcd_list[1])
# print(abcd_list[-2])
# print(abcd_list[1:])


# if __name__ == '__main__':
#     # 获取网页源代码
#     # for i in range(1, 25):
#     url='http://www.maiziedu.com/course/teachers/?page=1'
#     user_agent='Mozilla/5.0 (Windows NT 6.1; rv:46.0) Gecko/20100101 Firefox/46.0'
#     headers={'User-Agent':user_agent}
#     request=urllib2.Request(url=url,headers=headers)
#     reponse=urllib2.urlopen(request)
#     content= reponse.read()
#
#     # 数据提取过程
#
#     pattern=re.compile('<li class="t3out">\r\n*<div class="teacherListL">\r\n*<a title="(.*?)" href="(.*?)">'
#                        '<img alt="" src="(.*?)"></a>\r\n*</div>\r\n*<div class="teacherListR">\r\n*<p '
#                        'class="font20 color00 marginB14 t3out p">(.*?)<a href="(.*?)" class="go font12">'
#                        '(.*?)</a></p>\r\n*<p class="color66 marginB14"><span class="color99">(.*?)</span>'
#                        '</p>\r\n*<p class="color66"><span class="color99">(.*?)</span>(.*?)</p>\r\n* </div>\r\n* '
#                        '</li>\r\n*')
#     items = re.findall(pattern, content)
#
#     # 数据保存
#     for item in items:
#         print item[0]+':'+item[8]+'\n'
#         string = item[0]+':'+item[8]+'\n'
#         f = open('teachers_info.txt', 'a+')
#         f.write(string)
#         f.close()


# inp = raw_input('>')
# print len([i for i in inp if i.isalpha()])
# print len([i for i in inp if i.isdigit()])
# print len([i for i in inp if i.isspace()])

# l = ['', '60元', '', '', '10元', '', '30元', '', '35元', '', '15元', '', '45元', '', '45元']
# print [i for i in l if i != '']

# def A(): pass
#
# print A()  # 函数对象

import time

# def adder(u):
#     start = time.time()
#     def water():
#         u()
#         print time.time()-start
#         return time.time()-start
#         pass
#     return water  # 闭包方法对象

# m = adder(1)  # 包涵x的环境
# print m(2)
# print m(4)
# @adder
# def update():
#     pass
# update()

for x in (1, 2, 3, 4, 5, 6):
    print(x)
else:
    print(x+1)