# -*- coding:utf-8 -*-

import requests


res = requests.get('http://tianqi.2345.com/t/wea_history/js/58321_20162.js')
print res.content