# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import os

class Spider(object):
    def __init__(self):
        self.url = 'http://www.qiushibaike.com/text/page/%s'
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36'

    # 获取网页内容
    def get_page(self, pageIndex):
        headers={'User-Agent': self.user_agent}
        request = urllib2.Request(url=self.url % str(pageIndex), headers=headers)
        response = urllib2.urlopen(request)
        return response.read()

    # 分析网页
    def analysis(self, content):
        # .*? [\d|\D]*? [\w|\W]*? [\s|\S]*?
        pattern = re.compile('<div[\d|\D]*?class="author[\s|\S]*?>[\s|\S]*?<img[\s|\S]*?/>([\s|\S]*?)</a>[\s|\S]*?</div>[\s|\S]*?<div[\s|\S]*?class="content[\s|\S]*?>([\s|\S]*?)<!--([\s|\S]*?)-->[\s|\S]*?</div>', re.S)
        # pattern = re.compile('<a[\s|\S]*?>([\s|\S]*?)</a>', re.S)
        return re.findall(pattern, content)

    # 保存抓取内容
    def save(self, items, path):
        for item in items:
            if not os.path.exists(path):
                os.makedirs(path)
            filepath = path+'/'+item[0].strip()+'-'+item[2].strip()+'.txt'
            f = open(filepath, 'w')
            # f.write(item[1].strip().replace('<br/>', '\r\n'))
            # 正则替换
            result, number = re.subn('<br.*?/>', '\r\n', item[1].strip())
            f.write(result)
            f.close()
    def run(self):
        try:
            print u'开始抓取内容了...'
            for index in range(1, 35):
                content = self.get_page(index) # 分页
                items = self.analysis(content) # 分析内容[(),()]
                self.save(items, 'qiubai')
            print u'好累,终于抓取完了...'
        except urllib2.HTTPError as e:
            print e
        except urllib2.URLError as e:
            print e
        except Exception as e:
            print e

if __name__ == '__main__':
    spider = Spider()
    spider.run()

# try:
#     for i in range(1, 35):
#         url = 'http://www.qiushibaike.com/text/page/'+str(i)
#         user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36'
#         headers={'User-Agent': user_agent}
#         request = urllib2.Request(url=url, headers=headers)
#         response = urllib2.urlopen(request)
#         content = response.read()
#         # .*? [\d|\D]*? [\w|\W]*? [\s|\S]*?
#         pattern = re.compile('<div[\d|\D]*?class="author[\s|\S]*?>[\s|\S]*?<img[\s|\S]*?/>([\s|\S]*?)</a>[\s|\S]*?</div>[\s|\S]*?<div[\s|\S]*?class="content[\s|\S]*?>([\s|\S]*?)<!--([\s|\S]*?)-->[\s|\S]*?</div>', re.S)
#         # pattern = re.compile('<a[\s|\S]*?>([\s|\S]*?)</a>', re.S)
#         items = re.findall(pattern, content)
#         for item in items:
#             path = 'qiubai'
#             if not os.path.exists(path):
#                 os.makedirs(path)
#             filepath = path+'/'+item[0].strip()+'-'+item[2].strip()+'.txt'
#             f = open(filepath, 'w')
#             # f.write(item[1].strip().replace('<br/>', '\r\n'))
#             # 正则替换
#             result, number = re.subn('<br.*?/>', '\r\n', item[1].strip())
#             f.write(result)
#             f.close()
# except urllib2.HTTPError as e:
#     print e
# except urllib2.URLError as e:
#     print e