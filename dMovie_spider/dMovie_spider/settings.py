# -*- coding: utf-8 -*-

BOT_NAME = 'dMovie_spider'

SPIDER_MODULES = ['dMovie_spider.spiders']
NEWSPIDER_MODULE = 'dMovie_spider.spiders'



# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 301,
# }

ITEM_PIPELINES = {
   'dMovie_spider.pipelines.DmovieSpiderPipeline': 300,
   'scrapy.pipelines.images.ImagesPipeline': 301,
}
IMAGES_URLS_FIELD = 'img_url'
IMAGES_STORE = 'images'
