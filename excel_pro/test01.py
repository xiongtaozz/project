# coding:utf-8

import urllib2
import json

html = urllib2.urlopen('https://movie.douban.com/j/search_subjects?'
                       'type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&'
                       'page_limit=20&page_start=0')
jon =json.dumps(html.read())
print jon

# 解析器: 正则表达式{数据在js里面}
#         Htmlpaeser(代码要求比高)
#         xpath,bs4,css
import lxml.etree
import bs4
# <div></div>1111<span></span>