# -*- coding:utf-8 -*-

import urllib2,urllib
import re
import os


def get_html():
    url = 'http://www.maiziedu.com/course/python/425-5789/'
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    print response.read()
    return response.read()


def anylsis(content):
    pattern = re.compile('''<source src="(http.*\.mp4)" type="video/mp4">''')
    return re.findall(re.compile(pattern), content)


def save(items, path='maizi'):

    if not os.path.exists(path):
        os.makedirs(path)
    print items
    urllib.urlretrieve(items, '1.mp4')
    print '1.mp4', 'end'

if __name__ == '__main__':
    save('http://ocsource.maiziedu.com/Htmlcss30.mp4')
