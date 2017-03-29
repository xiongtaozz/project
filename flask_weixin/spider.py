#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import os
import random


class Spider(object):
    def __init__(self):
        self.url = 'http://www.qiushibaike.com/text/page/%s'
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                          'Chrome/43.0.2357.130 Safari/537.36'

    # 获取网页内容
    def get_page(self, pageIndex):
        headers={'User-Agent': self.user_agent}
        request = urllib2.Request(url=self.url % str(pageIndex), headers=headers)
        response = urllib2.urlopen(request)
        return response.read()

    # 分析网页
    def analysis(self, content):
        pattern = re.compile('<div class="content">(.*?)</', re.S)
        return re.findall(pattern, content)

    # 保存抓取内容
    def save(self, items):

        return random.choice(items).strip().replace('<br/>', '')

    def run(self):
        try:

            # for index in range(1, 35):
            content = self.get_page(random.choice(range(1, 36)))  # 分页
            items = self.analysis(content)  # 分析内容[(),()]
            return random.choice(items).strip().replace('<br/>', '').decode('utf-8')
        except urllib2.HTTPError as e:
            print e
        except urllib2.URLError as e:
            print e
        except Exception as e:
            print e

if __name__ == '__main__':
    spider = Spider()
    spider.run()
