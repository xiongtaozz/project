# coding:utf-8
import scrapy
import json


class Douban(scrapy.Spider):
    name = 'douban'
    start_urls = []
    headers = {
        'Cookie':'''ll="118318"; bid=AiNYP-6n8fo; _vwo_uuid_v2=9EB3F812B8A9118EB94027474CD47890|34b194f862e885047a4be33273d0a69a; __utma=30149280.919998915.1473339758.1479371226.1481682169.4; __utmz=30149280.1481682169.4.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.537797129.1473773069.1473773069.1481682169.2; __utmz=223695111.1481682169.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1481721609%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.4cf6=a8794bebd6acb6d7.1471944856.7.1481721614.1481682619.; _pk_ses.100001.4cf6=*''',
        'Host': 'movie.douban.com',
        'Upgrade-Insecure-Requests':1,
        'User-Agent': '''Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36
        (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'''
    }

    def start_requests(self):
        url = 'https://movie.douban.com/j/search_subjects?' \
              'type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0'
        yield scrapy.Request(url=url, headers=self.headers, callback=self.parse)

    def parse(self, response):
        json_dict = json.loads(response.body)
        for di in json_dict['subjects']:
            print di['rate']
            print di['title']
            print di['cover']
            yield {
                'image_urls': [di['cover']]
            }
