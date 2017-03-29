# coding:utf-8

import scrapy
from scrapy_redis.spiders import RedisSpider


class YunVs(RedisSpider):
    name = 'yunv'
    redis_key = 'spider:yunvs'

