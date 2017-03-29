# coding:utf-8
import scrapy
import os
import re
import json
import time
import csv
import urllib2
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class lfqCls(scrapy.Spider):
    name = 'tao_flq'
    start_urls = []
    for page in range(0, 44*100, 44):
        start_urls.append("https://s.taobao.com/search?q=%E8%BF%9E%E8%A1%A3%E8%A3%99&imgfile="
                          "&js=1&stats_click=search_radio_all%3A1&initiative_id="
                          "staobaoz_20160908&ie=utf8&fs=1&filter_tianmao=tmall&bcoffset=0&p4ppushleft=%2C44&s="+str(page))
    driver = webdriver.PhantomJS(executable_path=r"D:\Python27\phantomjs-2.1.1-windows\bin\phantomjs.exe")

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        regex = 'g_page_config = (.+)'
        items = re.findall(regex, str(response.body))
        items = items.pop().strip()
        items = items[0:-1]
        items = json.loads(items)
        items = items['mods']['itemlist']['data']['auctions']
        for (i, item) in enumerate(items):
            # raw_title: 宝贝标题
            # pic_url：宝贝图片地址
            # detail_url: 宝贝地址
            title = item['raw_title']
            pic_url = 'http:'+item['pic_url']
            detail_url = 'http:'+item['detail_url']
            print('saving: '+title)
            print(detail_url)
            try:
                self.driver.get(detail_url)
                # 价格
                price = self.driver.find_element_by_xpath('//*[@id="J_StrPriceModBox"]/dd').find_element_by_tag_name('span').text
                # 销量
                sales_count = self.driver.find_element_by_xpath('//*[@id="J_DetailMeta"]/div[1]/div[1]/div/ul/li[1]/div/span[2]').text
                # 评价数量
                message_count = self.driver.find_element_by_xpath('//*[@id="J_ItemRates"]/div/span[2]').text
                # 让浏览器滚动条向下滚动
                self.driver.execute_script("window.scrollTo(0,600)")
                # 模拟点击评价的选项卡
                self.driver.find_element_by_xpath('//*[@id="J_TabBar"]/li[2]').find_element_by_tag_name('a').click()
                time.sleep(10)
                self.driver.save_screenshot('1.png')
                # 描述相符度
                desc_score = self.driver.find_element_by_xpath('//*[@id="J_Reviews"]/div/div[1]/div[1]/strong').text
                impress_list = self.driver.find_elements_by_xpath('//*[@id="J_Reviews"]/div/div[1]/div[3]/div[2]/div/span/a')
                print(price, sales_count, message_count, desc_score)
                impress_good = ""
                impress_bad = ""
                for imp in impress_list:
                    color = imp.value_of_css_property('color')
                    if color == 'rgba(177, 0, 0, 1)':
                        impress_good += imp.text + "|"
                    else:
                        impress_bad += imp.text + "|"
                print(impress_good)
                print(impress_bad)
                print("="*50)

                # 保存图片
                f = open('images/'+str(i)+'.jpg', 'wb')
                content = urllib2.urlopen(pic_url).read()
                f.write(content)
                f.close()

                # 存入excel
                with open('taobao.csv', 'a', newline='') as f:
                    writer = csv.writer(f, dialect='excel')
                    writer.writerow(['宝贝标题', '宝贝价格', '宝贝销量', '评价数量', '好的印象','坏的印象', '宝贝地址'])
                    writer.writerow([title, price, sales_count, message_count, impress_good, impress_bad, detail_url])
            except Exception as e:
                print(e)
        time.sleep(3)
        self.driver.close()