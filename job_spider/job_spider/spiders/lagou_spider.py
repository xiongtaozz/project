# -*- coding:utf-8 -*-
import scrapy
import json


class spiderLagou(scrapy.spiders.Spider):

    name = 'lagou'
    allowed_domains = ["lagou.com"]

    start_urls = ['http://www.lagou.com/jobs/list_python?city=%E6%88%90%E9%83%BD&cl=false&fromSearch=true&labelWords=&suginput=',]

    headers = {
        # 'Accept': 'application/json, text/javascript, */*; q=0.01',
        # 'Accept-Encoding': 'gzip, deflate',
        # 'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Content-Length': 25,
        # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'ctk=1472017673; JSESSIONID=C29F6DFEE958BB4A1DEB2649606010F8; '
                  'SEARCH_ID=a0eda64c3422485baa4e3a97c9e6ee57; LGMOID=20160824134753-B3A47833E738C8756B69748942398132; '
                  'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1472017678; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1472017747; '
                  '_ga=GA1.2.41341033.1472017678; _gat=1; user_trace_token=20160824134755-af200aa350e84123b68f6bcec590da40; '
                  'LGSID=20160824134755-4de39ede-69be-11e6-b646-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; '
                  'PRE_LAND=http%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_python%3Fcity%3D%25E6%2588%2590%25E9%2583%25BD%26cl'
                  '%3Dfalse%26fromSearch%3Dtrue%26labelWords%3D%26suginput%3D; LGRID=20160824134858-736fd466-69be-11e6-'
                  '8030-5254005c3644; LGUID=20160824134755-4de3a08b-69be-11e6-b646-525400f775ce; td_cookie=362084950; '
                  'index_location_city=%E6%88%90%E9%83%BD',
        'Host': 'www.lagou.com',
        'Referer': 'http://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
        'X-Anit-Forge-Code': 0,
        'X-Anit-Forge-Token': None,
        'X-Requested-With': 'XMLHttpRequest'
    }

    def start_requests(self):
        url = 'http://www.lagou.com/jobs/positionAjax.json?city=%E6%88%90%E9%83%BD&needAddtionalResult=false'
        yield scrapy.Request(url=url, meta={'first': True, 'kd': 'python', 'pn': 1},
                             callback=self.parse, headers=self.headers)

    def parse(self, response):

        list_json = json.loads(response.body)
        print list_json
        for result in list_json:
            print result
        print '-' * 60
        print list_json['success']
        print '-' * 60
        print list_json['content']['positionResult']['result']
        # yield scrapy.Request(ful_url, self.parse_question, headers=self.headers)

    # def parse_question(self, response):
    #     yield {
    #         'title': response.xpath('//div[@class="left_section"]/div/div[2]/h1/@title').extract()[0],
    #         'username': response.xpath('//div[@class="left_section"]/div[2]/div/div[2]/div/div/@author').extract()[0],
    #         'url': response.url
    #     }
