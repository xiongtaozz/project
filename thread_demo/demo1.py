# -*- coding:utf-8 -*-
import urllib
import urllib2

# 简单的操作
# url = 'http://www.baidu.com'
# request = urllib2.Request(url)  # 请求
# response = urllib2.urlopen(url)  # 响应 # get
# print response.read()

# 简单的模拟登陆操作  url拼接方式是get方式提交
# values = {'username': '33100@qq.com', 'password': '12345678'}
# data = urllib.urlencode(values)
# url = 'http://www.imooc.com/user/login?'+data
# request = urllib2.Request(url)
# response = urllib2.urlopen(request)
# print response.read()
#
# # POST方式提交
# values = {'username': '33100@qq.com', 'password': '12345678'}
# data = urllib.urlencode(values)
# # url = 'http://localhost:8000/test/'
# url = 'http://www.imooc.com/user/login'
# request = urllib2.Request(url, data)
# response = urllib2.urlopen(request)
# print response.read()
#
# # 封装 herders,模拟浏览器方式提交
headers = {
    ''
}
# values = {'username': '33100@qq.com', 'password': '12345678'}
# data = urllib.urlencode(values)
# url = 'http://localhost:8000/test/'
# request = urllib2.Request(url, data, headers)
# response = urllib2.urlopen(request)
# print response.read()
# import re
# <video id="microohvideo_html5_api" class="vjs-tech" autoplay="" preload="none" poster=""
# src="http://ocsource.maiziedu.com/1.1kechengjieshao11.mp4">
# <source src="http://ocsource.maiziedu.com/1.1kechengjieshao11.mp4" type="video/mp4">
# </video>

# 下载视频地址  url  -->MP4地址  , fname --->文件名称
# urllib.urlretrieve('http://ocsource.maiziedu.com/1.1kechengjieshao11.mp4', 'maiziedu.mp4')
# print 'end!'

# 账号登陆 存放cookie
# import cookielib
# try:
#     # CookieJar —-派生—->FileCookieJar  —-派生—–>MozillaCookieJar和LWPCookieJar
#     cookie = cookielib.MozillaCookieJar('cookie.txt')
#     # 手动构造怎么opener对象
#     # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
#     opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
#     values = {'username': '33100@qq.com', 'password': '12345678'}
#     data = urllib.urlencode(values)
#     url = 'http://www.imooc.com/user/login'
#     result = opener.open(url, data)  # 手动构造的对象
#     cookie.save(ignore_discard=True, ignore_expires=True)
#     response = opener.open('http://www.imooc.com/u/2150319/courses')
#     co = response.read()
#     print co
# except urllib2.HTTPError as e:
#     print e.code
#     print e.reason
# except urllib2.URLError as e:
#     print e.reason
#
#
# 创建代理
proxy_handler = urllib2.ProxyHandler({"http": 'http://124.239.237.9'})
opener = urllib2.build_opener(proxy_handler)
urllib2.install_opener(opener)
headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
url = 'https://www.baidu.com/'
req = urllib2.Request(url=url, headers=headers)
result = opener.open(req)
print result.read()
