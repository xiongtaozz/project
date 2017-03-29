# coding:utf-8
import requests
from lxml import etree
from bs4 import BeautifulSoup
import os
import urllib

# url = 'http://www.nongyao001.com/sell/list-9-1.html'
# response = requests.get(url)
# # print response.content
# soup = BeautifulSoup(response.content, 'lxml')
# # print soup
# # string = etree.fromstring(str(soup))
# # print len(string.xpath('//div[@class="sel_conrig"]/div[2]/ul/li'))
# nl_list = soup.select('.sel_conrig div.poili_rpx_1 ul li.companr_li2 p a img')
# print nl_list[0].attrs['src']
# print nl_list[0].attrs['alt']


class nlPro(object):
    def __init__(self):
        self.url = 'http://www.nongyao001.com/sell/list-9-%d.html'
        self.cn = 0

    def get_cotent(self, url):
        response = requests.get(url)
        return response.content

    def syaiy(self, content):
        soup = BeautifulSoup(str(content), 'lxml')
        return soup.select('.sel_conrig div.poili_rpx_1 ul li.companr_li2 p a img')

    def saveFile(self, attrs):
        if not os.path.exists('农药'.decode('utf-8')):
            os.mkdir('农药'.decode('utf-8'))
        urllib.urlretrieve(attrs['src'], '农药'.decode('utf-8')+"/"+attrs['alt']+".jpg")

    def run(self):
        for x in range(1, 22):
            nl_list = self.syaiy(self.get_cotent(self.url % x))
            for nl in nl_list:
                self.saveFile(nl.attrs)

if __name__ == "__main__":
    nlPro().run()

