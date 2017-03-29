# -*- coding:utf-8 -*-

import scrapy
import json
from douban_scrapy.items import DouBanScrapyItem

class DouBan(scrapy.spiders.Spider):
    name = 'dou_ban'
    start_urls = [
        'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0',
        # 'https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0'
    ]
    headers = {
        'Host': 'movie.douban.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
        'Cookie': '''ll="118290"; bid=hOEc5dN4WBk; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1474545194%2C%22https%3A%2F%2Fwww
                .douban.com%2F%22%5D; _pk_id.100001.4cf6=97fb9066dab25001.1473339736.3.1474545259.1473773152.; __utma
                =30149280.1694731471.1473339736.1473773131.1474545196.3; __utmz=30149280.1473339736.1.1.utmcsr=douban
                .com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.1663571623.1473339736.1473773132.1474545197
                .3; __utmz=223695111.1473339736.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _vwo_uuid_v2
                =F4E0F054B75A2C0F195D7776399E0AC4|f584e07b108527d659e887618d98f6b2; ap=1; _pk_ses.100001.4cf6=*; __utmb
                =30149280.0.10.1474545196; __utmc=30149280; __utmb=223695111.0.10.1474545197; __utmc=223695111'''
    }

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], headers=self.headers, callback=self.parse)

    def parse(self, response):
        print response.body
        # print response.xpath('//div[@class="list-wp"]/div/a/div[@class="cover-wp"]/img')
        # json_list = json.loads(response.body)
        # # print json_list
        # # print json_list['subjects'][0]['title']
        # # print json_list['subjects'][0]['cover']
        # # print json_list['subjects'][0]['url']
        # for js in json_list['subjects']:
        #     item = DouBanScrapyItem()
        #     item['name'] = js['title']
        #     item['img'] = js['cover']
        #     item['url'] = js['url']
        #     yield scrapy.Request(url=js['url'], headers=self.headers, meta={'item': item}, callback=self.parse_content)

    def parse_content(self, response):

        pass