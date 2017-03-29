# -*- coding:utf-8 -*-
from HTMLParser import HTMLParser
import requests

response = requests.get('http://www.qiushibaike.com/text/')


def _attr(attrs, attrname):
    for attr in attrs:
        if attr[0] == attrname:
            return attr[1]
    return None


class QiushiHtml(HTMLParser):

    flag = False

    def handle_starttag(self, tag, attrs):
        if tag == 'div' and _attr(attrs, 'class') == 'content':
            self.flag = True

    def handle_data(self, data):
        if self.flag:
            print data.decode('utf-8')
            self.flag = False


qiu = QiushiHtml()
qiu.feed(response.content)
