# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import urllib
import os

class LanrenPipeline(object):
    def process_item(self, item, spider):

        print item
        # pass
        # if not os.path.exists(''):
        #     os.mkdir('')
        print item['items']
        print item['items'].xpath("img/@src").extract()
        # 第一种
        #urllib.urlretrieve(item['items'].xpath("img/@src").extract(), '1.jpg')
        # 第二种  二进制方式
        # 第三种 通过scrapy内置图片下载器


        # return item
        return {
             # 'url': item.urljoin(pic.xpath("@href")[0].extract()),
             # 'name': pic.xpath("text()")[0].extract(),
             'image_urls': item['items'].xpath("img/@src").extract()
        }
