# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanScrapyPipeline(object):
    def process_item(self, item, spider):
        print 'item', item
        with open('douban.txt', 'a') as f:
            f.write(str(item))
            f.close()
        return item
