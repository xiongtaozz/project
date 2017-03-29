

import requests
import re

res = requests.get('http://tieba.baidu.com/bawu2/platform/listMemberInfo?word=python&pn=1&qq-pf-to=pcqq.group')
repx = '<img src="(.*?)" alt.*?'
patten = re.compile(repx, re.S)
items = re.findall(patten, res.content)
print items