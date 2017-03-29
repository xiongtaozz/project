# -*- coding:utf-8 -*-
import scrapy
import json
from douban_scrapy.items import DoubanScrapyItem


class spiderBaidu(scrapy.spiders.Spider):

    name = 'douban'
    # allowed_domains = ["tieba.csv"]

    # start_urls = ['http://tieba.baidu.com/f?kw=python&fr=ala0&tpl=5',]

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,en-US;q=0.7,en;q=0.3',
        'Connection' : 'keep-alive',
        'Host': 'movie.douban.com',
        'Referer': 'http://movie.douban.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'
    }

    def start_requests(self):
        # url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=' \
        #       '%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0'
        # url = 'https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&' \
        #       'page_limit=20&page_start=0'
        url = 'https://movie.douban.com/subject/25977027/?tag=%E7%83%AD%E9%97%A8&from=gaia'
        yield scrapy.Request(url=url, callback=self.parse, headers=self.headers)

    def parse(self, response):
        content = response.body
        with open('douban_html.txt', 'a') as f:
            f.write(str(content))
            f.close()
        print content
        # print response.xpath('//div[@class="list-wp"/]/div/a[@class="item"]')  # none
        # res = json.loads(response.body)   # ---> 字典
        # print res
        # if res:
        #     for r in res['subjects']:
        #         dou = DoubanScrapyItem()
        #         dou['name'] = r['title']
        #         dou['img'] = r['cover']
        #         yield dou


