import scrapy


class taobao_spider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['taobao.com']
    start_urls = ['https://s.taobao.com/search?spm=a21bo.50862.201856-fline.1.fv5FfZ&q='
                  '%E8%BF%9E%E8%A1%A3%E8%A3%99&refpid=420460_1006&source=tbsy&style=grid&'
                  'tab=all&pvid=d0f2ec2810bcec0d5a16d5283ce59f66']
    herders = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 '
                      'Safari/537.36',
    }

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], headers=self.herders, callback=self.parse)

    def parse(self, response):
       print response.body