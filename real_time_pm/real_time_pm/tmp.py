#!/usr/bin/env python
#coding:utf-8
import requests
from lxml import etree

# def get_cont(url):
#     headers = {
#         'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#         'Upgrade-Insecure-Requests':1,
#         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
#     }
#     r = requests.get(url,headers=headers)
#     # print r.content
#     return r.content
#
# def parsePage(cont):
#     doc = etree.HTML(cont)
#     trs = doc.xpath('//*[@id="detail-data"]/tbody/tr')
#
#     for i in trs:
#         s = etree.tostring(i)
#         print s.xpath('/td/text()')
#
#
# if __name__ == '__main__':
#     url = 'http://pm25.in/beijing'
#     cont = get_cont(url)
#     parsePage(cont)
str = '''
            <tr>
              <td>万寿西宫</td>
              <td>39</td>
              <td>优</td>
              <td>_</td>
              <td>10</td>
              <td>28</td>
              <td>0.3</td>
              <td>12</td>
              <td>123</td>
              <td class="O3_8h_dn">67</td>
              <td>2</td>
            </tr>
            <tr>
              <td>万寿西宫</td>
              <td>39</td>
              <td>优</td>
              <td>_</td>
              <td>10</td>
              <td>28</td>
              <td>0.3</td>
              <td>12</td>
              <td>123</td>
              <td class="O3_8h_dn">67</td>
              <td>2</td>
            </tr>
'''
doc = etree.HTML(str)
trs = doc.xpath('tr/td/text()')
print trs

for i in trs:
    print i
    # d = etree.HTML(i)
    # print d.xpath('tr/td/text()')
