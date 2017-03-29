# -*- coding:utf-8 -*-
import requests
import json
'''
  json处理
'''

url = 'http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip='
ip = '27.13.206.48'

response = requests.get(url+ip)  # json
# j = json.loads(response.content)
# print j  # 字典 ,json是不支持list
# print j['province']
# print j['city']
# print j['country']
print response.content
