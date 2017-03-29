# coding:utf-8
import requests
import re
from lxml import etree
from bs4 import BeautifulSoup
from email_l import em_cls


# data = {
#     'account_l': 'xt@maiziedu.com',
#     'password_l': 'xiongtao1123'
# }
# url = 'http://www.maiziedu.com/user/login/'
# headers = {
#     'Host': 'www.maiziedu.com',
#     'Referer': 'http://www.maiziedu.com/',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0'
# }
# req = requests.session()
# res = req.post(url=url, data=data, headers=headers)
# print res.content
# con = req.get('http://www.maiziedu.com/home/t/onevone_service/')
#
# stup = BeautifulSoup(con.content, 'lxml')
# sp_all = stup.select('span.newinfo em')
# if sp_all is not None:
#     for sp in sp_all:
#         if sp.text:
#             print sp.text


class stuBack(object):

    def __init__(self):
        self.data = {
        'account_l': 'xt@maiziedu.com',
        'password_l': 'xiongtao1123'
        }
        self.url = 'http://www.maiziedu.com/user/login/'
        self.headers = {
            'Host': 'www.maiziedu.com',
            'Referer': 'http://www.maiziedu.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0'
        }
        self.count = 0

    def analysis(self):
        req = requests.session()
        res = req.post(url=self.url, data=self.data, headers=self.headers)
        con = req.get('http://www.maiziedu.com/home/t/onevone_service/')
        return con.content

    def analyze(self, con):
        stup = BeautifulSoup(con, 'lxml')
        sp_all = stup.select('span.newinfo em')
        if sp_all is not None:
            for sp in sp_all:
                if sp.text:
                    self.count += 1

    def run(self):
        self.analyze(self.analysis())
        if self.count != 0:
            em_cls().run(self.count)

if __name__ == '__main__':
    stuBack().run()