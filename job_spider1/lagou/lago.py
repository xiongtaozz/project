# -*- coding:utf-8 -*-

import requests
import json
import os
import urllib


# url = 'http://www.lagou.com/jobs/positionAjax.json?city=成都&needAddtionalResult=false'
# response = requests.get(url)
# json_list = json.loads(response.content)
# # # 解析结果
# for j in json_list['content']['positionResult']['result']:
#     print type(j['companyShortName'].encode('utf-8'))
#     # print j['companyShortName'] + + j['createTime']
#     print j['salary']
#     print j['companyLabelList']
#     print j['companyLogo']
#     print '='*30 + '>'
#     print """
#         公司名称:%s
#         发布时间:%s
#         薪资:%s
#         福利:%s
#     """.decode('utf-8') % (j['companyShortName'], j['companyShortName'], j['salary'], j['positionAdvantage'])

class LaGo(object):
    def __init__(self):
        self.url = 'http://www.lagou.com/jobs/positionAjax.json?city=成都&needAddtionalResult=false'
        self.pageSize = 0
        self.countPage = 0
        self.totalCount = 0
        self.headers = {'Referer': 'http://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0'}
        self.data = {'first': True, 'kd': 'python', 'pn': 1}
        self.string = """
        公司名称:%s
        发布时间:%s
        薪资:%s
        福利:%s
        """
        self.img = 'http://www.lgstatic.com/thumbnail_120x120/'

    # 抓取某一页网页信息
    def _get_content(self):
        response = requests.post(url=self.url, data=self.data)
        json_list = json.loads(response.content)
        if json_list:
            self.pageSize = json_list['content']['pageSize']
            self.totalCount = json_list['content']['positionResult']['totalCount']
        return json_list['content']['positionResult']['result']

    def _formatStr(self, complist):
        string = ''
        if complist:
            for c in range(len(complist)):
                if c == 0:
                    string += complist[c]
                else:
                    string += "," + complist[c]
        return string

    def _saveFile(self, path, string, imgurl):
        if not os.path.exists(path):
            os.mkdir(path)
        urllib.urlretrieve(imgurl, path+'/'+path+".jpg")
        with open(path+'/'+path+".txt", 'w') as f:
            f.write(string.encode('utf-8'))
            f.close()
        # with open(path+'/'+path+".jpg", 'wb') as f:

    def _result(self, j_list):
        for j in j_list:
            string = self.string.decode('utf-8') % (j['companyShortName'],
                                   j['createTime'],
                                   j['salary'],
                                   j['positionAdvantage'])
            # string = [(j['companyShortName'].encode('utf-8')).decode('utf-8'), j['createTime'].encode('utf-8')]
            # print j['companyLogo']
            # //www.lgstatic.com/thumbnail_120x120/i/image/M00/2E/03/CgqKkVc9jmCAI8DpAAD09YLPnBk157.png
            self._saveFile(j['companyShortName'], string, self.img+j['companyLogo'])

    def run(self):
        json_list = self._get_content()
        self._result(json_list)
        page = self.totalCount/self.pageSize
        if self.totalCount % self.pageSize > 1:
            page += 1
        if page > 1:
            for x in range(2, page+1):
                json_list = self._get_content()
                self.data = {'first': True, 'kd': 'python', 'pn': x}
                self._result(json_list)

if __name__ == '__main__':
    LaGo().run()
