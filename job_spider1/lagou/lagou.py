# -*- coding:utf-8 -*-

import requests
import json
import os
"""
    抓取拉钩网上的python招聘信息
"""
url = 'http://www.lagou.com/jobs/positionAjax.json?city=%E6%88%90%E9%83%BD&needAddtionalResult=false'

res = requests.post(url=url)
json_list = json.loads(res.content)
print json_list['content']
print json_list['content']['positionResult']['result']
for l in json_list['content']['positionResult']['result']:
    print l['companyShortName']
    print l['createTime']
    print l['companyLogo']
    print l['salary']
    print l['companyLabelList']


class SpiderLaGo(object):

    def __init__(self):
        self.url = 'http://www.lagou.com/jobs/positionAjax.json?city=%E6%88%90%E9%83%BD&needAddtionalResult=false'
        self.page = 1
        self.size = 0
        self.headers = {}
        self.save_str = """
        公司名称:%s
        发布时间:%s
        薪资:%s
        福利:%s
        """

    def _get_content(self):
        response = requests.post(self.url)
        json_list = json.loads(response.content)
        if json_list:
            self.page = json_list['content']['pageNo']
            self.size = json_list['content']['pageSize']
        return json_list['content']['positionResult']['result']

    def _save_result(self):
        j_list = self._get_content()
        if j_list:
            for j in j_list:
                self.save_str % (j['companyShortName'], j['createTime'], j['salary'], self._sub_string(j['companyLabelList']))

    def _sub_string(self, string):
        ss = ''
        for s in range(len(string)):
            if s == 0:
                ss += s
            else:
                ss += "," + s
        return ss

    def _save_file(self, path):
        if os.path.exists(path):
            os.mkdir(path)