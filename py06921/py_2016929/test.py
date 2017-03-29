# coding:utf-8

import urllib
import urllib2
import re
import os

url = 'http://product.pchouse.com.cn/list/c56.html'
req = urllib2.Request(url)
res = urllib2.urlopen(req)
content = res.read()
pattern = re.compile('<img src="(.*?)" .*?/>')
items = re.findall(pattern, content)
if items:
    for item in items:
        # url fname:如果只有文件名,默认存储的地方,当前文件夹
        # 相对路径
        if not os.path.exists('qiangzhi'):
            os.mkdir('qiangzhi')
        urllib.urlretrieve(item, "qiangzhi/"+item.split('/')[-1])

