#coding=utf-8

import scrapy
from collectips.items import CollectipsItem


class XiciSpider(scrapy.Spider):
    name = "xici"
    allowed_domains = ["xicidaili.com"]
    start_urls = (
        'http://www.xicidaili.com/nn',
    )
    
    # def start_requests(self):
    #     reqs=[]
    #
    #     for i in range(1, 2):
    #         req = scrapy.Request("http://www.xicidaili.com/nn/%s"%i)
    #         reqs.append(req)
    #
    #     return reqs
    
    def parse(self, response):
        ip_list=response.xpath('//table[@id="ip_list"]')
        
        trs = ip_list[0].xpath('tr')
        
        # items=[]
        
        for ip in trs[1:]:
            pre_item=CollectipsItem()
            
            pre_item['IP'] = ip.xpath('td[2]/text()')[0].extract()
            
            pre_item['PORT'] = ip.xpath('td[3]/text()')[0].extract()
            
            pre_item['POSITION'] = ip.xpath('td[4]/a/text()')[0].extract()
            
            pre_item['TYPE'] = ip.xpath('td[6]/text()')[0].extract()
            
            pre_item['SPEED'] = ip.xpath(
                'td[7]/div[@class="bar"]/@title').re('\d{0,2}\.\d{0,}')[0]
                
            pre_item['LAST_CHECK_TIME'] = ip.xpath('td[9]/text()')[0].extract()

            yield pre_item
            # items.append(pre_item)
            
        # return items
    