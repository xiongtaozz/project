# -*- coding: utf-8 -*-
import scrapy
from lanren.items import LanrenItem

class LanrenspiderSpider(scrapy.Spider):
    name = "lanrenspider"
    allowed_domains = ["lanrentuku.com"]
    start_urls = [
        'http://www.lanrentuku.com/tupian/beijingtupian/',
        # 'http://www.lanrentuku.com/tupian/beijingtupian/',
        # 'http://www.lanrentuku.com/tupian/beijingtupian/',
    ]
    headers ={

    }
    def start_requests(self):
        a = []
        return [scrapy.Request(url='', headers={}, meta={'a', a},callback=self.parse)]

    def parse(self, response):
        # response.meta['a']
        pics = response.xpath("//div[@class='list-pic']/dl/dd/a")
        # print pics
        for pic in pics:
            # item = LanrenItem()
            # item['url'] = response.urljoin(pic.xpath("@href")[0].extract())
            # item['name'] = pic.xpath("text()")[0].extract()
            # item['image_urls'] = pic.xpath("img/@src").extract()
            # print item
            # yield item

            yield {
                'url': response.urljoin(pic.xpath("@href")[0].extract()),
                'name': pic.xpath("text()")[0].extract(),
                'image_urls': pic.xpath("img/@src").extract()
            }
            ''.strip('\n').strip()

            # yield {
            #     'items': pic
            # }

