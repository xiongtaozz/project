# -*- coding:utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider


class pro58Spider(RedisSpider):
    name = 'spider58'
    redis_key = 'spider:58_urls'
    pass
