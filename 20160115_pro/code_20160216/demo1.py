#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib
import urllib2
import gzip, StringIO
import cookielib
import socket
import httplib
import sys
import pyquery


# 基本操作
# url = 'http://www.baidu.com/'
# # url = 'http://localhost:8000/test/'
# # url = 'http://guomeidiyicheng.soufun.com/xiangqing/'
# request = urllib2.Request(url)
# response = urllib2.urlopen(request)
# # html = response.read()
# # data = StringIO.StringIO(html)
# # gzipper = gzip.GzipFile(fileobj=data)
# # html = gzipper.read()
# print response.read()


# get方式请求

# values = {'username': '33100@qq.com', 'password': '12345678'}
# data = urllib.urlencode(values)
# # url = 'http://localhost:8000/test/?'+data
# url = 'http://www.imooc.com/user/login?'+data
# request = urllib2.Request(url)
# response = urllib2.urlopen(request)
# print response.read()
#
# # post方式请求
# try:
#     values = {'username': '33100@qq.com', 'password': '12345678'}
#     data = urllib.urlencode(values)
#     # url = 'http://localhost:8000/test/'
#     url = 'http://www.imooc.com/user/login'
#     # url = 'http://www.maiziedu.com/user/login/'
#     request = urllib2.Request(url, data)
#     response = urllib2.urlopen(request)
#     print response.read()  # json
#     response = urllib2.urlopen('http://www.imooc.com/space/index')
#     html = response.read()
#     print html
# except urllib2.HTTPError as e:
#     print e.code
#     print e.reason
# except urllib2.URLError as e:
#     print e.reason


# 设置头部信息

# url = 'http://localhost:8000/test/'
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' #Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)
# values = {'username': '33100@qq.com', 'password': '12345678'}
# headers = {'User-Agent': user_agent,
#            'Referer': 'http://www.zhihu.com/articles'}
# data = urllib.urlencode(values)
# request = urllib2.Request(url, data, headers=headers)
# response = urllib2.urlopen(request)
# print response.read()

# 如何去获取登录之后的页面信息，使用登录后的cookie去访问需要登录之后的网页

# try:
#     cookie = cookielib.MozillaCookieJar('cookie.txt')
#     opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
#     values = {'username': '33100@qq.com', 'password': '12345678'}
#     data = urllib.urlencode(values)
#     # url = 'http://localhost:8000/test/'
#     url = 'http://www.imooc.com/user/login'
#     # url = 'http://www.maiziedu.com/user/login/'
#     result = opener.open(url, data)
#     cookie.save(ignore_discard=True, ignore_expires=True)
#     response = opener.open('http://www.imooc.com/space/index')
#     print response.read()
# except urllib2.HTTPError as e:
#     print e.code
#     print e.reason
# except urllib2.URLError as e:
#     print e.reason

# 使用代理
# proxy_handler = urllib2.ProxyHandler({"http": 'http://221.10.102.203:82'}) #1
# opener = urllib2.build_opener(proxy_handler)  # 2
# urllib2.install_opener(opener) # 3
# headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
# url = 'http://www.maiziedu.com/'
# # url ='http://localhost:8000/test/'
# req = urllib2.Request(url=url, headers=headers)
# result = opener.open(req) # 4
# print result.read()

# 使用httplib
# conn = httplib.HTTPConnection("www.maiziedu.com")
# conn = httplib.HTTPSConnection("www.baidu.com")
# conn.request('get', '/',
#              headers = {"Host": "www.baidu.com",
#                                     "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5",
#                                     "Accept": "text/plain"})
# res = conn.getresponse()
# print "version=%s"%res.version
# print "reason=%s"%res.reason
# print "status=%s"%res.status
# print "msg=%s"%res.msg
# print "getheaders=%s"%res.getheaders()
# print res.read()
# conn.close()


# 使用soket访问网页
# HOST = 'www.baidu.com'    # The remote host
# PORT = 80              # The same port as used by the server
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建tcp socket 创建TCP套接字
# s.connect((HOST, PORT))  # 连接套接字
# s.sendall('GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: keep-alive\r\n\r\n') # 完整发送tcp数据
# data = s.recv(80960)  # 接受TCP套接字数据 //recv接收的是字节数
# s.close()  # 关闭套接字
# print data