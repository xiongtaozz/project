# coding:utf-8
import re
import os
import urllib.request as r

# 抓取过程；
# 1.访问网页源代码

user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/50.0.2661.102 UBrowser/5.7.15702.19 Safari/537.36'
url = 'http://www.qiushibaike.com/8hr/page/2/?s=4917338'
headers = {'User-Agent': user_agent}
request = r.Request(url=url, headers=headers)
response = r.urlopen(request)
content = response.read()
print(content)
