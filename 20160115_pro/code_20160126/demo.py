#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
多线程查询网页是否进入百度倒排索引或者正排索引及是否收录
"""

from time import localtime
import threading
import urllib2
import json
import random
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


lock = threading.RLock()


class Query(object):
    def __init__(self, save_file_name):
        self.filename = save_file_name
        self.threadpool = []

    def query(self, urllist, thnum):
        i = 0
        total = 0
        s = len(urllist)
        print "The urllist length is",len(urllist),s
        while i < s:
            j = 0
            while j < thnum and i+j < s:
                total += 1
                data = QueryThread(urllist[i+j], self.filename)
                self.threadpool.append(data)
                data.start()
                j += 1
            i += j
            for thread in self.threadpool:
                thread.join(30)
            self.threadpool = []
        return total


class QueryThread(threading.Thread):
    def __init__(self, url, save_file_name):
        super(QueryThread, self).__init__()
        self.url = "https://www.baidu.com/s?ie=UTF-8&wd={0}&tn=json".format(url)
        self.rawurl = url
        self.user_agent = [
            "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30",
            "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
            "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; "
            ".NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET4.0E; .NET CLR "
            "3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR "
            "3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
            "Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 Version/11.50",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 "
            "Safari/533.21.1",
            "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; "
            ".NET CLR 3.5.21022; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)"
        ]
        self.req_header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive',
            'Host': 'www.baidu.com',
            'Upgrade-Insecure-Requests': 1,
        }
        self.filename = save_file_name
        self._result = {}

    def get_data(self):
        self.req_header['User-Agent'] = random.choice(self.user_agent)
        try:
            lock.acquire()
            req = urllib2.Request(self.url, data=None,headers=self.req_header)
            content = urllib2.urlopen(req,timeout=10).read()
            data = json.loads(content)
            lock.release()
            return data
        except Exception as e:
            print self.rawurl,e

    def save(self,filename, result):
        try:
            savefile = open(filename, 'a+')
            resultnum = result['feed']['all']
            if resultnum > 0:
                serp = result['feed']['entry'][0]
                self._result['title'] = serp['title']
                self._result['desc'] = serp['abs']
                self._result['url'] = serp['url']
                ctime = serp['time']
                t = localtime(ctime)
                if ctime == '':
                    self._result['index'] = '未索引'
                elif ctime == 0:
                    self._result['index'] = '正排索引'
                    self._result['snaptime'] = '未建立快照'
                else:
                    self._result['index'] = '倒排索引'
                    self._result['snaptime'] = '%d年%d月%d日%d时%d分%d秒' % (t[0],t[1],t[2],t[3],t[4],t[5])
                self._result['rank'] = '第%s位' % str(serp['pn'])
                savefile.write('查询链接：'+self._result['url']+'\n')
                savefile.write('页面标题：'+self._result['title']+'\n')
                savefile.write('页面描述：'+self._result['desc']+'\n')
                savefile.write('快照时间：'+self._result['snaptime']+'\n')
                savefile.write('出现位置：'+self._result['rank']+'\n')
                savefile.write('索引类型：'+self._result['index']+'\n')
                savefile.write('\n')
                savefile.flush()
            else:
                savefile.write('查询链接：'+self.rawurl+'\n')
                self._result['include'] = "未收录!"
                savefile.write('是否收录：'+self._result['include']+'\n')
                savefile.write('\n')
                savefile.flush()
        except Exception as e:
            self._result['error'] = '查询出错!'
            savefile.write('查询错误：'+self._result['error']+'\n')
            savefile.write('\n')
            savefile.flush()
            print e
        finally:
            savefile.close()

    def run(self):
        result = self.get_data()
        self.save(self.filename, result)


if __name__ == '__main__':
    url_file = open('anli.txt', 'r')
    urllist = [url.strip('\n') for url in url_file]
    thread_num = 10
    print 'start....'
    q = Query('rs.txt')
    total = q.query(urllist,thread_num)
    url_file.close()
    print 'end.Total check',total
