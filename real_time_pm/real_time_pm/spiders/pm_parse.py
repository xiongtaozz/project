#!/usr/bin/env python
#encoding:utf-8
import scrapy
from real_time_pm.items import RealTimePmItem
from real_time_pm.items import ExecuteSql
from lxml import etree
import datetime
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class RealTimePm(scrapy.Spider):
    name = 'pm_value'
    start_urls = ['http://pm25.in/']

    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Upgrade-Insecure-Requests':1,
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
    }
    def start_requests(self):
        for i in self.start_urls:
            yield scrapy.Request(url=i,headers=self.headers,callback=self.parse)

    def parse(self, response):
        list = response.xpath('/html/body/div[2]/div[2]/div[2]/div[2]/ul/div[2]/li/a/text()')
        urls = response.xpath('/html/body/div[2]/div[2]/div[2]/div[2]/ul/div[2]/li/a/@href')

        for i in list:
            city = i.extract()
            url = urls[list.index(i)].extract()
            url = response.urljoin(url)
            yield scrapy.Request(url=url,meta={'city':city},callback=self.parse_page)

    def parse_page(self,response):
        items = RealTimePmItem()
        print response.url
        trs = response.xpath('//*[@id="detail-data"]/tbody/tr')
        time = response.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/p/text()').extract()[0][7:]
        print time
        items_list = []
        for tr in trs:
            s = tr.extract()
            doc = etree.HTML(s)
            list = doc.xpath('//tr/td/text()')  # 注：这里如果写td/text()没用,或者使用descendant::*/text()
            print list
            items = RealTimePmItem()
            items['city'] = response.meta['city']
            items['real_time'] = time
            items['run_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
            items['monitor_station'] = list[0]
            items['AQI'] = list[1]
            items['lev'] = list[2]
            items['top_pm'] = list[3]
            items['pm25'] = list[4]
            items['pm10'] = list[5]
            items['CO'] = list[6]
            items['NO2'] = list[7]
            items['O3_1h'] = list[8]
            items['O3_8h'] = list[9]
            items['SO2'] = list[10]
            items_list.append(items)
            #yield items
        yield items_list
        # yield ExecuteSql()

        print '=============================================='
