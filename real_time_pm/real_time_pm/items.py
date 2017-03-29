# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ExecuteSql(scrapy.Item):
    pass

class RealTimePmItem(scrapy.Item):
    # define the fields for your item here like:
    run_time = scrapy.Field()
    real_time = scrapy.Field()
    city = scrapy.Field()
    monitor_station = scrapy.Field()
    AQI = scrapy.Field()
    lev = scrapy.Field()
    top_pm = scrapy.Field()
    pm25 = scrapy.Field()
    pm10 = scrapy.Field()
    CO = scrapy.Field()
    NO2 = scrapy.Field()
    O3_1h = scrapy.Field()
    O3_8h = scrapy.Field()
    SO2 = scrapy.Field()
