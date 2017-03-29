# -*- coding:utf-8 -*-
import requests
import re
import json

url = 'https://s.taobao.com/search?q=连衣裙'

res = requests.get(url)
con = res.content
g_page = re.findall(re.compile('g_page_config =(.+)'), con)
# print g_page[0]
# print g_page[0][0:-1]
dict_json = json.loads(g_page[0][0:-1])
# print dict_json
item_list = dict_json['mods']['itemlist']['data']['auctions']
for item in item_list:
    if int(item['reserve_price'])<100:
        print item['raw_title']
        print item['nick']
        print item['view_price']
        print item['pic_url']
        print '=' * 30