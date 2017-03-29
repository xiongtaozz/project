# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy import log
from sundygen.items import *


class MaizieduSpider(scrapy.Spider):
    name = "maiziedu"
    allowed_domains = ["www.maiziedu.com/course/"]
    start_urls = (
        'http://www.maiziedu.com/course/',
    )

    def parse(self, response):

        log.msg('hello sundy')
        sel = Selector(response)
        sites = sel.xpath('//li//@href').extract()
        for site in sites:
            log.msg(site)
            item = SundygenItem()
            item.name = site
            item.link = 'http://www.baidu.com'
            print site

        return item

