# -*- coding: utf-8 -*-
import scrapy
from Dbmovie.items import DbmovieItem
import json

class DbmoviesSpiderSpider(scrapy.Spider):
	name = "Dbmovies_spider"
    #allowed_domains = ["https://movie.douban.com"]
	#定义头部headers
	headers = {
		"Cookie": 'bid=yKurw_5oTk0; __utma=30149280.1845303472.1466746720.1466746720.1466747385.2;	__utmz=30149280.1466747385.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ll="118318"; ap=1',
		'Host': 'movie.douban.com',
		'Referer': 'https://www.douban.com/explore',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
	}
	#自定义scrapy抓取方法，并将定义的headers传入方法
	def parse(self, response):
		url='https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0'
		return [scrapy.Request(url,headers=self.headers,callback=self.parse)]
		
	#解析json数剧  获得对应页面的url
	def parse_detail(self,response):
		cookies = response.headers["Set-Cookie"].decode(response.encoding).split(';')
		y = [{cookie.split('=')[0]: cookie.split('=')[1]} for cookie in cookies]
		cookies = {}
		[cookies.update(item) for item in y]
		data = json.loads(response.body)
		ur = data["subjects"]
		for item in ur:
			movie = DbmovieItem()
			movie['name'] = item('title')
			movie['img_url'] = item('cover')
			movie['movie_url'] = item('url')
			yield scrapy.Request(url=movie["movie_url"], headers=self.headers,
                                 callback=self.parse_movie_info, meta={"item": movie}, cookies=cookies)
	#解析电影简介
	def parse_movie_info(self, response):
		movie = response.meta["item"]
		movie['description'] = response.xpath("//span[@property='v:summary']/text()").extract()[0].encode('utf-8')
		print movie
		return movie
