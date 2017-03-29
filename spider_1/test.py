# -*- coding:utf-8 -*-
import urllib
import urllib2

# 简单的操作
# url = 'http://www.baidu.com'
# request = urllib2.Request(url)
# response = urllib2.urlopen(request)
# print response.read()

# 简单的模拟登陆操作  url拼接方式是get方式提交
# values = {'username': '33100@qq.com', 'password': '12345678'}
# data = urllib.urlencode(values)
# url = 'http://localhost:8000/test/?'+data
# request = urllib2.Request(url)
# response = urllib2.urlopen(request)
# print response.read()

# POST方式提交
# values = {'username': '33100@qq.com', 'password': '12345678'}
# data = urllib.urlencode(values)
# url = 'http://localhost:8000/test/'
# url = 'http://www.imooc.com/user/login'
# request = urllib2.Request(url, data)
# response = urllib2.urlopen(request)
# print response.read()
#
# # 封装 herders,模拟浏览器方式提交
# headers = {
#     ''
# }
# values = {'username': '33100@qq.com', 'password': '12345678'}
# data = urllib.urlencode(values)
# url = 'http://localhost:8000/test/?'+data
# request = urllib2.Request(url)
# response = urllib2.urlopen(request)
# print response.read()
# import re
#
# expx ='([a-z0-9]*)[\s|\S]*?([A-Za-z]+)[\s|\S]*?(\d.*\.\d+\.\d+\.\d+|\-)[\s|\S]*?([A-Za-z0-9\-]*|\-)[\s|\S]*?([A-Za-z0-9\-]*|\-)[\s|\S]*?(\w.*)'
# comp ='centos7  STOPPED  -           -     -       YES'
# r = re.findall(expx , comp)
# print r
# 账号登陆 存放cookie
import cookielib
try:
    cookie = cookielib.MozillaCookieJar('cookie.txt')
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    values = {'username': '33100@qq.com', 'password': '12345678'}
    data = urllib.urlencode(values)
    url = 'login'
    resutl = opener.open(url)
    cookie.save(ignore_discard=True, ignore_expires=True)
    response = opener.open('登录成功指向的网址')
    print response.read()
except urllib2.HTTPError as e:
    print e.code
    print e.reason
except urllib2.URLError as e:
    print e.reason


# 创建代理
url = ''
proxy_handler = urllib2.ProxyHandler({"http": 'http://120.195.192.221:80'})
opener = urllib2.build_opener(proxy_handler)
urllib2.install_opener(opener)
request = urllib2.Request(url)
response = opener.open(request)
print response.read()

