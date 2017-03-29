# coding:utf-8

import urllib2
import re
from threading import *

'''
   多线程方式爬虫抓取麦子官网,所有老师信息
   注:
   要使用下列抓取方法,请示先学习面向对象和多线程
'''


class spiderMaizi(Thread):
    def __init__(self,group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(spiderMaizi,self).__init__(group, target, name,
                 args, kwargs, verbose)
        self.__args=args
        self.url = 'http://www.maiziedu.com/course/teachers/?page=%s'
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36'

    # 抓取网页内容
    def get_page(self,pageIndex):
        headers = {'User-Agent': self.user_agent}
        request = urllib2.Request(url=self.url % str(pageIndex), headers=headers)
        response = urllib2.urlopen(request)
        return response.read()

    def analysis(self,count):
        recmp = '<div class="teacherListR">[\s|\S]*?<p class="font20 color00 marginB14 t3out p">(.*)<a href="/[a-z]{0,}/[a-z]{0,}/[a-z]{0,}/[0-9]{0,}/" class="go font12">.*</a></p>[\s|\S]*?<p class="color66 marginB14"><span class="color99">.*</span></p>[\s|\S]*?<p class="color66"><span class="color99">.*</span>(.*)</p>[\s|\S]*?</div>'
        pattern =re.compile(recmp)
        return re.findall(pattern,count)

    # 保存内容
    def save(self, items):
        for item in items:
            self.saveFile('maizi.txt',item)

    def saveFile(self, path, item):
            f = open(path, 'a+')
            try:
                f.write(item[0]+':\n'+item[1]+'\n')
            except Exception as e:
                print e
            finally:
                f.close()

    def run(self):
        try:
            print u'开始抓取内容....'
            print self.__args[0]
            count = self.get_page(self.__args[0])
            items = self.analysis(count)
            self.save(items)
            print u'内容抓取完毕....'
        except urllib2.HTTPError as e:
            print e
        except urllib2.URLError as e:
            print e
        except Exception as e:
            print e
if __name__ == '__main__':
    for i in xrange(18):
        spider = spiderMaizi(args=(i,))
        spider.run()