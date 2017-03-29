# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from maiziedu_grab.items import *
from scrapy import log


class MaizieduSpider(scrapy.Spider):
    name = "maiziedu"
    allowed_domains = ["http://www.maiziedu.com/course/"]
    start_urls = (
        'http://www.maiziedu.com/course/',
    )

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//span[@class="text"]/text()').extract()
        for site in sites:
            item = MaizieduGrabItem()
            item['name'] = site
            log.msg(site)
		