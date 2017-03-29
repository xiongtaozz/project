# coding:utf-8
import re
import json
import requests
import urllib,urllib2
# 报ssl错误可以打开这些注释试试
# import requests.packages.urllib3.util.ssl_
# requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'

url = 'https://s.taobao.com/search?q=连衣裙'

# resp = requests.get(url)
# html = resp.text
# print html
# req = urllib2.Request(url)
html = urllib2.urlopen(url).read()
# print res.read()

regex = r'g_page_config =(.+)'
items = re.findall(regex, html)

items = items.pop().strip()
print items
items = items[0:-1]
print items
items = json.loads(items)
item_list = items['mods']['itemlist']['data']['auctions']

for item in item_list:
    print item['raw_title']
    print item['nick']
    print item['view_price']
    print item['pic_url']
    print '=' * 30
