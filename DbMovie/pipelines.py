# -*- coding: utf-8 -*-
import urllib,os,logging

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DbmoviePipeline(object):
    def process_item(self, item, spider):
        # if item['pic_url']:
        #     try:
        #         path = os.getcwd() + '\\' +item['name'].split(' ')[0]
        #         if not os.path.exists(path):
        #             os.mkdir(path)
        #         pic_path = path + '\\' + item['name'].split(' ')[0] + '电影海报.jpg'
        #         info_path = path + '\\' + '电影简介.txt'
        #         with open(info_path,'wb') as info:
        #             info.write(item['name'])
        #             info.write('-'*30)
        #             info.write(item['desc'])
        #         info.close()
        #         urllib.urlretrieve(item['pic_url'],pic_path)
        #     except Exception as e:
        #         logging.info(e)
        return item

