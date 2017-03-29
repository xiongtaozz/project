#!/bin/env
# coding:utf-8

import scrapy
from dMovie_spider.items import DmovieSpiderItem
import json
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import urllib

class DoubanMovieSpider(scrapy.Spider):
    name="DoubanMovieSpider"
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,en-US;q=0.7,en;q=0.3',
        'Connection': 'keep-alive',
        'Host': 'movie.douban.com',
        'Referer': 'http://movie.douban.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'
    }

    def start_requests(self):
        url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0'
        yield scrapy.Request(url=url, callback=self.parse, headers=self.headers)
        pass

    def parse(self,response):
        content = response.body

        res = json.loads(content)

        if res:
            for res in res['subjects']:
                item = DmovieSpiderItem()
                item['name'] = res['title']
                item['rate'] = res['rate']
                item['content_url'] = res['url']
                item['img_url']= [res['cover']]
                item['editor']=''
                item['director']=''
                item['info']=''

                yield scrapy.Request(url=item["content_url"], headers= self.headers, meta={'item': item}, callback=self.parse_content,
                             dont_filter=True)

    def parse_content(self, response):
        item = response.meta['item']

        a_s_director = response.xpath("//*[@id='info']/span[1]/span[2]/a")
        a_s_editor = response.xpath("//*[@id='info']/span[2]/span[2]/a")
        info = response.xpath("//*[@id='link-report']/span[@property='v:summary']/text()|""//*[@id='link-report']/span[1]/span/text()")[0].extract().strip()

        for a in a_s_director:
            item['director'] += (a.xpath("text()")[0].extract()+'\t')

        for a in a_s_editor:
            item['editor'] += (a.xpath("text()")[0].extract()+'\t')

        item['info'] = info
        yield item
        # if not os.path.exists(item['name']):
        #     os.mkdir(item['name'])
        # #进入创建的目录
        # os.chdir(item['name'])
        # path='content.txt'
        # f=open(path,'w')

        # 写入电影的信息
        # content= '电影名称: '+str(item["name"])+'\t'+'电影评分: '+str(item["rate"])\
        # +'\n'+'导演: '+str(item["director"])+'\n'+'编剧: '+str(item["editor"])+'\n'\
        # +'海报链接: '+str(item["img_url"])+'\n'+'电影简介: '+str(item["info"])
        # f.write(content)
        # 下载电影海报
        # print("#downloading poster from %s"%item['img_url'])
        # urllib.urlretrieve(item["img_url"],'%s.jpg'%item['name'])
        # 返回上一层目录
        # os.chdir('../')
        # f.close()

