# coding:utf-8
import urllib,urllib2
import cookielib

# 存放cookie的方式
# try:
#     url = 'http://www.imooc.com/user/login'
#     values = {'username': '33100@qq.com', 'password': '12345678'}
#     data = urllib.urlencode(values)
#     # 创建cookie信息
#     cookie = cookielib.MozillaCookieJar('cookie.txt')
#     # 必须构造咱们opener
#     opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
#     result = opener.open(url, data)
#     cookie.save(ignore_expires=True, ignore_discard=True)
#     response = opener.open('http://www.imooc.com/space/index')
#     print response.read()
# except urllib2.HTTPError as e:
#     print e.code
#     print e.reason
# except urllib2.URLError as e:
#     print e.reason

# 使用代理
proxy_handler = urllib2.ProxyHandler({"http": 'http://221.10.102.203:82'})  # 1
opener = urllib2.build_opener(proxy_handler)  # 2
urllib2.install_opener(opener) # 3
headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
url = 'http://www.maiziedu.com/'
# url = 'http://localhost:8000/test/'
req = urllib2.Request(url=url, headers=headers)
result = opener.open(req)  # 4
print result.read()