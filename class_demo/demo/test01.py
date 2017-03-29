# coding:utf-8
import urllib
import urllib2

if __name__ == '__main__':
    url = 'http://www.maiziedu.com/user/login/'
    # 类似输入网址
    # 设置头部，以获取与浏览器访问一样的结果
    headers = {'User-Agent':' Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'}
    # 设置要提交的数据
    values = {'account_l':'maomao@111.com', 'password_l':'aaaaaa'}
    # 转换值
    data = urllib.urlencode(values)
    request = urllib2.Request(url=url,  data=data, headers =headers)
    # send request
    # get response
    # 类似敲回车键
    response = urllib2.urlopen(request)
    # 类似张开眼睛看内容
    print response.read()


from Tkinter import *
import tkSimpleDialog
