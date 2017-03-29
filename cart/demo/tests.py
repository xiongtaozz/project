# -*- coding: utf-8 -*-
import urllib2
import lxml
from bs4 import BeautifulSoup
def fetch_weather(url):
    res = urllib2.urlopen('http://yunvs.com/list/mai_1.html')
    page = res.read()
    soup=BeautifulSoup(page,'lxml')
    #获取目标标签下的信息
    params = soup.find_all('td',{'align':'center'})
    #只获取文本
    s = BeautifulSoup(str(params))
    #print s.prettify()# this html

    print s.get_text()
    # for x in s.stripped_strings:
    #     print (repr(x).decode('raw_unicode_escape'))
    #将文本存储到excel


    # for x in s.get_text().replace("\n"," "):
    #     print x.decode('raw_unicode_escape')


fetch_weather(url='http://yunvs.com/list/mai_1.html')

