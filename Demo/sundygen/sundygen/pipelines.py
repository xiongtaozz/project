# -*- coding: utf-8 -*-

import sqlite3

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SundygenPipeline(object):
    def process_item(self, item, spider):
        f = open('dfd.txt','w')
        f.write(item['name'])
        f.close()
        return item
