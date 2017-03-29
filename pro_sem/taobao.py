# coding: utf-8

# 引入网络访问库
import urllib
import urllib2

# 引入正则表达式的库
import re

# 引入json的解析库
import json

import os

import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


if not os.path.exists('images'):
    os.mkdir('images')

for page in range(0,44*100, 44):
    print page
    url = "https://s.taobao.com/search?q=%E8%BF%9E%E8%A1%A3%E8%A3%99&imgfile=" \
          "&js=1&stats_click=search_radio_all%3A1&initiative_id" \
          "=staobaoz_20160908&ie=utf8&fs=1&filter_tianmao=tmall&bcoffset=0&p4ppushleft=%2C44&s="+str(page)

    response = urllib2.urlopen(url)
    content = response.read()

    regex = 'g_page_config = (.+)'
    items = re.findall(regex, content)

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
        print 'saving: '+title
        # f = open('images/'+str(i)+'.jpg', 'wb')
        # content = urllib2.urlopen(pic_url).read()
        # f.write(content)
        # f.close()
        print title
        print detail_url

        try:

            driver = webdriver.PhantomJS(executable_path=r"C:\phantomjs-2.1.1-windows\bin\phantomjs.exe")
            driver.get(detail_url)
            # 价格
            price = driver.find_element_by_xpath('//*[@id="J_PromoPrice"]/dd/div/span').text
            # 销量
            sales_count = driver.find_element_by_xpath('//*[@id="J_DetailMeta"]/div[1]/div[1]/div/ul/li[1]/div/span[2]').text
            # 评价数量
            message_count = driver.find_element_by_xpath('//*[@id="J_ItemRates"]/div/span[2]').text
            print price, sales_count, message_count
            # 让浏览器滚动条向下滚动
            driver.execute_script("window.scrollTo(0,600)")
            # 模拟点击评价的选项卡
            driver.find_element_by_xpath('//*[@id="J_TabBar"]/li[2]').find_element_by_tag_name('a').click()
            time.sleep(5)
            driver.save_screenshot('1.png')
            # 描述相符度
            desc_score = driver.find_element_by_xpath('//*[@id="J_Reviews"]/div/div[1]/div[1]/strong').text
            impress_list = driver.find_elements_by_xpath('//*[@id="J_Reviews"]/div/div[1]/div[3]/div[2]/div/span')
            print desc_score
            for imp in impress_list:
                print imp.text
            print "="*50
        except Exception as e:
            pass
        else:
            driver.close()
        exit()
    time.sleep(5)
