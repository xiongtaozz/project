# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem


class DownloadImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for img_url in item['img_url']:
            yield scrapy.Request(img_url,meta={'item':item})

    def file_path(self, request, response=None, info=None):
        return 'full/%s/%s.jpg' % (request.meta["item"]["name"], request.meta["item"]["name"])

    def item_completed(self, results, item, info):

        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item


class DownloadInfoPipeline(object):

    def process_item(self, item, spider):
        if not os.path.exists("full/%s" % (item["name"])):
            os.mkdir("full/%s" % (item["name"]))
        with open("full/%s/%s.txt" % (item["name"], item["name"]), "wt") as f:
            f.write(str(item["description"]))
        return item