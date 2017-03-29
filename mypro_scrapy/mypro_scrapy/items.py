# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# j_th_tit
# s98b6e68ad  clearfix <a href="/p/4608150249" title="新书强烈推荐《从零开始学python》，
# 手把手教你，从小白到专家" target="_blank" class="j_th_tit ">新书强烈推荐《从零开始学python》，手把手教你，从小白到专家</a>
class MyproScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    username = scrapy.Field()
    url = scrapy.Field()

