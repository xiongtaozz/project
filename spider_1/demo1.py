#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib
import urllib2
import cookielib
import socket
import httplib

# 基本操作

request = urllib2.Request('http://www.baidu.com')
response = urllib2.urlopen(url='http://www.baidu.com')
print response.read()

# get方式请求

# values = {'username': '33100@qq.com', 'password': '12345678'}
# data = urllib.urlencode(values)
# print data
# # url = 'http://localhost:8000/test/?'+data
# url = 'http://www.imooc.com/user/login?'+data
# # request = urllib2.Request(url)
# response = urllib2.urlopen(url=url)
# print response.read()

# post方式请求

# try:
#     values = {'username': '33100@qq.com', 'password': '12345678'}
#     # 把key-value这样的键值对转换成我们想要的格式，返回的是a=1&b=2这样的字符串
#     data = urllib.urlencode(values)
#     # url = 'http://localhost:8000/test/'
#     # url = 'http://www.imooc.com/user/login'
#     url = 'http://www.maiziedu.com/user/login/'
#     # 得到Request对象  403  404  301 302  500  200
#     request = urllib2.Request(url,data)
#     # 访问网页并返回response对象
#     response = urllib2.urlopen(request)
#     print response.read()
#     # response = urllib2.urlopen('http://www.imooc.com/space/index')
#     # print response.read()
# except urllib2.HTTPError as e:
#     print e.code
#     print e.reason
# except urllib2.URLError as e:
#     print e.reason



# 设置头部信息

# url = 'http://localhost:8000/test/'
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# values = {'username': '33100@qq.com', 'password': '12345678'}
# headers = {'User-Agent': user_agent,
#            'Referer': 'http://www.zhihu.com/articles'}
# data = urllib.urlencode(values)
# request = urllib2.Request(url, data,headers)
# response = urllib2.urlopen(request)
# print response.read()

# 如何去获取登录之后的页面信息，使用登录后的cookie去访问需要登录之后的网页

# try:
#     # 得到cookie对象
#     cookie = cookielib.MozillaCookieJar('cookie.txt')
#      # urllib2.urlopen()函数不支持验证、cookie或者其它HTTP高级功能。
#      # 要支持这些功能，必须使用build_opener()函数创建自定义Opener对象
#     opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
#
#     values = {'username': '33100@qq.com', 'password': '12345678'}
#     data = urllib.urlencode(values)
#     # url = 'http://localhost:8000/test/'
#     url = 'http://www.imooc.com/user/login'
#     # url = 'http://www.maiziedu.com/user/login/'
#     result = opener.open(url, data)
#     # 保存cookie
#     cookie.save(ignore_discard=True, ignore_expires=True)
#     response = opener.open('http://www.imooc.com/space/index')
#     print response.read()
# except urllib2.HTTPError as e:
#     print e.code
#     print e.reason
# except urllib2.URLError as e:
#     print e.reason
#
# # 使用代理
# # 创建代理
# proxy_handler = urllib2.ProxyHandler({"http": 'http://120.195.192.221:80'})
# opener = urllib2.build_opener(proxy_handler)
# urllib2.install_opener(opener)
# headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
# url = 'http://www.maiziedu.com/'
# # url = 'http://localhost:8000/test/'
# req = urllib2.Request(url=url, headers=headers)
# result = opener.open(req)
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

# # 导入socket库:
# import socket
# # 创建一个socket:
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 建立连接:
# s.connect(('www.sina.com.cn', 80))
# s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# # 接收数据:
# buffer = []
# while True:
#     # 每次最多接收1k字节:
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = ''.join(buffer)
# # 关闭连接:
# s.close()
# header, html = data.split('\r\n\r\n', 1)
# print header
# # 把接收的数据写入文件:
# with open('sina.html', 'wb') as f:
#     f.write(html)

# 使用soket访问网页
# HOST = 'www.baidu.com'    # The remote host
# PORT = 80              # The same port as used by the server
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #创建tcp socket
# s.connect((HOST, PORT)) #连接套接字
# s.sendall('GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: keep-alive\r\n\r\n') # 完整发送tcp数据
# data = s.recv(80960) # 接受TCP套接字数据
# s.close() # 关闭套接字
# print data

# server.py
import socket
import threading
import time

# def tcplink(sock, addr):
#     print "Accept new connection from %s:%s..." % addr
#     sock.send('Welcome!')
#     while True:
#         data = sock.recv(1024)
#         time.sleep(1)
#         if data == "exit" or not data:
#             break
#         sock.send("Hello, %s" % data)
#     sock.close()
#     print "Connection from %s:%s closed." % addr

# if __name__ == "__main__":
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.bind(('127.0.0.1', 9000))
#     s.listen(5)
#     print "server start..."
#     while True:
#         sock, addr = s.accept()
#         t = threading.Thread(target=tcplink, args=(sock, addr))
#         t.start()
