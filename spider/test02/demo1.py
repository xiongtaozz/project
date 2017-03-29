# -*- coding: utf-8 -*
import urllib2
import re
import os

url = 'http://www.jianshu.com/'
user_agent ='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
headers = {'User_Agent':user_agent}
request = urllib2.Request(url=url, headers=headers)
response = urllib2.urlopen(request)
content = response.read()
pattern = re.compile('<h4 class="title">.*?<a target="_blank" href="(.*?)">(.*?)</a>',re.S)
items = re.findall(pattern,content)

for item in items:
    print ('http://www.jianshu.com./' + item[0])
    print item[1].decode('utf-8')
    art_web = 'http://www.jianshu.com./' + item[0]
    url1 = art_web
    user_agent1 = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    headers1 = {'User_Agent': user_agent1}
    request1 = urllib2.Request(url=url1, headers=headers1)
    response1 = urllib2.urlopen(request1)
    content1 = response1.read()
    pattern1 = re.compile('<p>(.*?)</p>', re.S)
    items1 = re.findall(pattern1 , content1)
    for item1 in items1:
        print item1.decode('utf-8')
    art_title = item[1]