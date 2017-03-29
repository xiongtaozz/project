# -*- coding:utf-8 -*-

import scrapy
from tu_scrapy.items import *


class DmozSpider(scrapy.spiders.Spider):

    name = 'dmoz'
    allowed_domains = ['http://www.dmoz.org/']
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        # filename = response.url.split('/')[-2]
        # # with open(filename, 'wb') as f:
        # #     f.write(response.body)
        for sel in response.xpath('//u/li'):
            # title =sel.xpath('a/text()').extract()
            # link = sel.xpath('a/@hear').extract()
            # desc = sel.xpath('text()').extract()
            # print title, link, desc
            item = DmozItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text').extract()
            yield item

