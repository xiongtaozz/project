#coding:utf-8
import urllib
import urllib2
import cookielib
import StringIO,gzip
#教师页面 http://202.115.133.186:8080/Teachers/Teachers.aspx


# Cookie: CNZZDATA1000250372=1615145150-1448604675-%7C1448604675;
# ASP.NET_SessionId=0ulibedqyrfejy0orn3om11v;
# UserTokeID=97c1fe46-932f-4ed0-9092-57e4a89a9f99;
# td_cookie=85193033

# HTTP/1.1 200 OK
# Cache-Control: private
# Content-Type: text/html; charset=utf-8
# Content-Encoding: gzip
# Vary: Accept-Encoding
# Server: Microsoft-IIS/7.5
# Set-Cookie: ASP.NET_SessionId=0ulibedqyrfejy0orn3om11v; path=/; HttpOnly
# X-AspNet-Version: 4.0.30319
# Set-Cookie: UserTokeID=97c1fe46-932f-4ed0-9092-57e4a89a9f99; path=/
# X-Powered-By: ASP.NET
# Date: Fri, 27 Nov 2015 07:31:36 GMT
# Content-Length: 120


headers_index={
    'Accept': 'text/html, application/xhtml+xml, */*',
    'X-HttpWatch-RID': '60325-10152',
    'Referer': 'http://202.115.133.186:8080/Default.aspx',
    'Accept-Language': 'zh-CN',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Accept-Encoding': 'gzip, deflate',
    'Host': '202.115.133.186:8080',
    'DNT': 1,
    'Connection': 'Keep-Alive',
    'Cookie': 'CNZZDATA1000250372=1615145150-1448604675-%7C1448604675; ASP.NET_SessionId=0ulibedqyrfejy0orn3om11v; UserTokeID=97c1fe46-932f-4ed0-9092-57e4a89a9f99; td_cookie=85193033'
}
headers_login={
    'X-HttpWatch-RID': '60325-10080',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://202.115.133.186:8080/Login.html',
    'Accept-Language': 'zh-CN',
    'Accept-Encoding':'gzip, deflate',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Content-Length': 90,
    'DNT':1,
    'Connection': 'Keep-Alive',
    'Cache-Control': 'no-cache',
    'Cookie': 'CNZZDATA1000250372=1615145150-1448604675-%7C1448604675'
}
url = 'http://202.115.133.186:8080/Login.html'
urlLogin='http://202.115.133.186:8080/Common/Handler/UserLogin.ashx'
values = {'username' : '201201010403' , 'password':'a8c0f09e173c00f4f49151e09cfd2db5'}
# cookie = cookielib.MozillaCookieJar('cookie.txt')
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# urllib2.install_opener(opener)
# data = urllib.urlencode(values)
# result = opener.open(urlLogin ,data,headers)
# cookie.save(ignore_discard=True , ignore_expires=True)
# response = opener.open('http://202.115.133.186:8080/Default.aspx')
# html = response.read()
# response = urllib2.urlopen('http://202.115.133.186:8080/Teachers/Teachers.aspx')
# print html
data = urllib.urlencode(values)
request = urllib2.Request(urlLogin,data)
response = urllib2.urlopen(request)
html = response.read()
req = urllib2.Request(url='http://202.115.133.186:8080/Teachers/Teachers.aspx',headers=headers_index)
res = urllib2.urlopen(req)
print res.read()