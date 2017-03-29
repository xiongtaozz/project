# coding:utf-8

import requests

response = requests.get('http://so.gushiwen.org/gushi/songsan.aspx')
print response.content
