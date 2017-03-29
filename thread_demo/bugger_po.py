# coding:utf-8

import re
import urllib2
import os
from threading import Thread


def spider_teacher(page):
    print u'开始', page
    url = 'http://www.maiziedu.com/course/teachers/?page='+str(page)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'}
    try:
        request = urllib2.Request(url=url, headers=headers)
        response = urllib2.urlopen(request)
        content = response.read()
    except urllib2.HTTPError as e:
        print e
        exit()
    except urllib2.URLError as e:
        print e
        exit()
    pattern = re.compile('p">(.*?)<a href.*?简介：</span>(.*?)</p>.*?</div>', re.S)
    items = re.findall(pattern, content)
    path = 'maizi'
    if not os.path.exists(path):
        os.makedirs(path)
    file_path = path+'/'+'teacher'+'.txt'
    f = open(file_path, 'a+')
    for item in items:
        f.write(item[0]+':\n '+item[1] + '\n')

    print u'结束'


if __name__ == '__main__':
    for x in range(1, 24):
        Thread(target=spider_teacher, args=(x,)).start()
