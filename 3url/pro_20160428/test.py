# -*- coding:utf-8 -*-
'''
  业务
'''
import time


# def add(*agrs,**kwagrs):
#     print agrs, kwagrs

# try:
#     f =open('test.txt')
#     print f.read()
#     f.flush()
#     f.close()
# except:
#     pass
# else:  # try没有异常则会执行
#     # f.close()
#     pass
# finally:  # 始终要执行
#     print u'执行完毕'
#
# raise NameError()
import MySQLdb

# if __name__ == '__main__':
#      # print add(1, 2, 3, a=3, b=2, c=3)

import HTMLParser


class add(HTMLParser.HTMLParser):
    def __int__(self):
        pass

    def handle_starttag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        print data

a = add()
a.feed('<title>abc</title><body><div>sdf<div></body>')

