# coding:utf-8
import os
import requests

'''
    页面抓取图片
'''
# import urllib

# import urllib
#
# urllib.urlretrieve('http://tb.himg.baidu.com/sys/portrait/item/4f30e4b88de5ada6e4b9a0e6b2a1e69caae69da55a75', 'xxx.jpg')
# response = urlopen('url')
# response.read()  wb rb b    open --->write

def save_file():
    path = 'maizi_p'
    if not os.path.exists(path):
        os.makedirs(path)
    r = requests.get('http://tb.himg.baidu.com/sys/portrait/item/4f30e4b88de5ada6e4b9a0e6b2a1e69caae69da55a75')
    if not os.path.exists(path+'/中文'.decode('utf-8')):
        os.makedirs(path+'/中文'.decode('utf-8'))
    with open(path+'/中文'.decode('utf-8')+'/buxuxi.jpg', 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
        f.close()

save_file()
# 'http://tb.himg.baidu.com/sys/portrait/item/7585e6af9be8b186e4b98be7a59eb93a'

