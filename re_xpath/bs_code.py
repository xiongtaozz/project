# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from lxml import etree
import httplib
import urllib2
# urllib2.urlopen()

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" id ="p"><b class='co'>The Dormouse's story<span>xxx</span></b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>

"""

soup = BeautifulSoup(html_doc, 'lxml')
# print soup

# print soup.title
#
# print soup.title.name
#
# print soup.title.text
# # #
# print soup.title.string
# #
# print soup.div
#
# print soup.p
#
# print soup.a
#
# print soup.find_all('a')
#
# print soup.find(id='link3').text

# print soup.get_text()

# 遍历树

# print soup.find_all('title')
#
# print soup.find_all('p', 'title')[0].text
#
# print '....', soup.find_all('p', 'story')[0].text
#
# print soup.find_all(id="link2")
#
# print soup.find_all(id=True)
#
# print soup.find_all()
# # 应用css 查询
#
# print soup.select('.title b.co span')[0].text

# xpath 引用
s = etree.fromstring(str(soup))
print s.xpath('//p[2]')[0].text
