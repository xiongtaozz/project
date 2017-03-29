# -*- coding:utf-8 -*-
import scrapy
from mypro_scrapy.items import MyproScrapyItem

class spiderBaidu(scrapy.spiders.Spider):

    name = 'tieba'
    # allowed_domains = ["tieba.csv"]

    start_urls = ['http://tieba.baidu.com/f?kw=python&fr=ala0&tpl=5',]

    headers = {
        'Referer': 'http://tieba.baidu.com/f?kw=python&fr=ala0&tpl=5',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0'
    }

    # def start_requests(self):
    #     yield scrapy.Request(url='', callback=parse)

    def parse(self, response):
        res_url = response.xpath('//div/ul/li/div[@class="t_con cleafix"]/div[2]/div/div/a[@class="j_th_tit "]/@href').extract()
        for url in res_url:
            print url
            ful_url = 'http://tieba.baidu.com/'+url
            yield scrapy.Request(ful_url, self.parse_question, headers=self.headers)

    def parse_question(self, response):
        items = []
        for i in range(3):
            item = MyproScrapyItem()
            item['title'] = response.xpath('//div[@class="left_section"]/div/div[2]/h1/@title').extract()[0]
            item['username'] = response.xpath('//div[@class="left_section"]/div[2]/div/div[2]/div/div/@author').extract()[0]
            item['url'] = response.url
            items.append(item)
        print '-------------1111111111------->', items
        # yield items
        # yield {
        #     'title': response.xpath('//div[@class="left_section"]/div/div[2]/h1/@title').extract()[0],
        #     'username': response.xpath('//div[@class="left_section"]/div[2]/div/div[2]/div/div/@author').extract()[0],
        #     'url': response.url
        # }
        yield {
            'items': items
        }
