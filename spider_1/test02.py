# -*- coding:utf-8 -*-
import urllib
import urllib2


# 最基本操作方式
# url = 'http://www.baidu.com'
# request = urllib2.Request(url)  # 请求信息
# response = urllib2.urlopen(request)  # 返回相应信息
# print response.read()

# get 方式提交
# values = {'username': '33100@qq.com', 'password': '12345678'}  # 字典
# data = urllib.urlencode(values)  # tn=monline_3_dg&b=2
# print data
# # url = 'http://www.baidu.com'
# url = 'http://www.imooc.com/passport/user/login/?'+data
# # url = 'http://localhost:8000/test/?'+data
# request = urllib2.Request(url)  # 请求信息
# response = urllib2.urlopen(request)  # 返回相应信息
# print response.read()

# POST 方式 模拟登陆
# values = {'username': '33100@qq.com', 'password': '12345678'}  # 字典
# data = urllib.urlencode(values)  # tn=monline_3_dg&b=2
# print data
# # url = 'http://www.baidu.com'
# url = 'http://www.imooc.com/user/login'
# # url = 'http://localhost:8000/test/?'+data
# request = urllib2.Request(url, data)  # 请求信息
# response = urllib2.urlopen(request)  # 返回相应信息
# response = urllib2.urlopen(url='http://www.imooc.com/space/index')
# print response.read()

# 模拟header信息
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
# }
# values = {'username': '33100@qq.com', 'password': '12345678'}  # 字典
# data = urllib.urlencode(values)  # tn=monline_3_dg&b=2
# print data
# url = 'http://localhost:8000/test/'
# # 请求信息
# request = urllib2.Request(url, data, headers)
# response = urllib2.urlopen(request)  # 返回相应信息
# print response.read()
# cookie 信息存储
import cookielib
cookie = cookielib.MozillaCookieJar('cookie.txt')
# urllib2.urlopen 不支持函数验证,cookie或者其他HTTP高级及功能
# 如果要支持,必须使用 build_opener()函数来创建自定义的 opener对象
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))  # 创建opener对象
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
}
values = {'username': '33100@qq.com', 'password': '12345678'}  # 字典
data = urllib.urlencode(values)  # tn=monline_3_dg&b=2
url = 'http://www.imooc.com/user/login'
# url = 'http://localhost:8000/test/'
# 请求信息
result = opener.open(url, data)
cookie.save(ignore_expires=True, ignore_discard=True)
response = opener.open('http://www.imooc.com/space/index')  # 返回相应信息
print response.read()

# 代理
