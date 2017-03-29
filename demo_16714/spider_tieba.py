# -*- coding:utf-8 -*-
import requests
import urllib
from HTMLParser import HTMLParser

# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

def attr(attrs,attrname):
    for attr in attrs:
        if attr[0]==attrname:
            return attr[1]
    return None

class ImgParse(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.in_a=False
        self.img=None

    def handle_starttag(self, tag, attrs):
        if tag=='a' and attr(attrs,'class')=='userinfo_head':
            self.in_a=True
        if tag=='img' and self.in_a:
            self.in_a=False
            self.img=attr(attrs,'src')
            # print self.img

class Name_urlParse(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.nameurl_list=[]
        self.current = {}
        self.in_span=False
    def handle_starttag(self, tag, attrs):
        if tag=='span' and attr(attrs,'class')=='frs-author-name-wrap':
            self.in_span=True
        if tag == 'a' and self.in_span:
            self.current['url']=attr(attrs,'href')
    def handle_endtag(self, tag):
        if tag=='span':
            self.in_span=False
    def handle_data(self, data):
        if self.in_span:
            self.current['name']=data
            self.nameurl_list.append(self.current)
            self.current={}

def download():
    url='http://tieba.baidu.com/f?kw=python&fr=ala0&tpl=5'
    r=requests.get(url)
    n=Name_urlParse()
    n.feed(r.content.decode('utf-8'))
    return n.nameurl_list    # 返回一个内容是元祖的列表，元组内容是url  ，name

def get_img(list):
    downloadurllist=[]
    print len(list)                       # 打出列表的长度
    for i in list:
        url='http://tieba.baidu.com'+i['url']

        r=requests.get(url)

        # try:
        p= ImgParse()
        # p.feed(r.content)
        print p.feed(r.content.decode('utf-8'))
        downloadurllist.append(p.img)  # 1. 我想把解析出来的地址p.img加到downloadurllist列表里边去，运行之后
        # except UnicodeDecodeError as e:    # 列表里边只有两个,但是我的传进来的列表list长度是50
        #     print e                       # 2.捕获的这个异常不知道怎么处理，不知道哪里的错误
    print len(downloadurllist)
    return downloadurllist

if __name__=='__main__':
    d=download()
    g=get_img(d)



