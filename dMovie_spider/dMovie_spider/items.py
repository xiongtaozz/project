# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DmovieSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    rate = scrapy.Field()

    content_url = scrapy.Field()
    editor = scrapy.Field()
    director = scrapy.Field()
    info = scrapy.Field()

    img_url = scrapy.Field()
    pass
