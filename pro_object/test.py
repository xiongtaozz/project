# coding:utf-8
# import urllib.request
# import urllib.parse
#
#
# if __name__=='__main__':
#
#     Url='http://www.qiushibaike.com/'
#     user_agent='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
#     Headers ={'User-Agent':user_agent}
#     # values = {'name': 'Michael Foord','location': 'Northampton','language': 'Python' }
#     # data = urllib.parse.urlencode(values)
#     # data = data.encode('ascii')
#     req = urllib.request.Request(url=Url, headers=Headers)
#     response = urllib.request.urlopen(req)
#     content = response.read()
#     print(content)

# 什么是完数
# 完数: 因子数之和等本身 则他就是完数

# inp = int(raw_input('>'))
# # 得到 inp 因子数
# # 分子数 :range(1,inp) == 分子数的列表
# # 因子数 = inp % 分子数的列表[i]  == 0
# # 因子数之和 == inp 就是完数
#
# sumer = 0
# for x in range(1, inp):
#     if inp % x == 0:
#         sumer = sumer + x
# if inp == sumer:
#     print '%d 完数'.decode('utf-8') % inp
# else:
#     print '%d 不是完数'.decode('utf-8') % inp
