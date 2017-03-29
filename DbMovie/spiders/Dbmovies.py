# -*- coding: utf-8 -*-
import scrapy
from DbMovie.items import DbmovieItem


class DbmoviesSpider(scrapy.Spider):
    name = "Dbmovies"
    # allowed_domains = ["http://movie.douban.com"]
    start_urls = (
        'https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0',
    )

    def parse(self, response):
        for href in response.xpath('//*[@id="gaia"]/div[4]/div/a/@href'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_movie_info)

    def parse_movie_info(self, response):
        item = DbmovieItem()
        item['name'] = response.xpath('//*[@id="content"]/h1/span[1]/text()').extract()
        item['desc'] = response.xpath('//*[@id="link-report"]/span/text()').extract()
        item['pic_url'] = response.xpath('//*[@id="mainpic"]/a/img/@src').extract()
        yield item







