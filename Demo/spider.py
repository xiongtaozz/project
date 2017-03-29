# coding: utf8  
import urllib2  
import re  
import pymongo  
  
db = pymongo.Connection().test  
url = 'http://piratebay.se/browse/200/%d/3'  
find_re = re.compile(r'<tr>.+?\(.+?">(.+?)</a>.+?class="detLink".+?">(.+?)</a>.+?<a href="(magnet:.+?)" .+?已上传 <b>(.+?)</b>, 大小 (.+?),', re.DOTALL)  
  
# 定向爬去10页最新的视频资源  
for i in range(0, 10):  
    u = url % (i)  
    # 下载数据  
    html = urllib2.urlopen(u).read()  
    # 找到资源信息  
    for x in find_re.findall(html):  
        values = dict(  
            category = x[0],  
            name = x[1],  
            magnet = x[2],  
            time = x[3],  
            size = x[4]  
        )  
        # 保存到数据库  
        db.priate.save(values)  
  
print 'Done!'  