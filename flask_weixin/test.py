# !/usr/bin/env python
# encoding: utf-8

# tieba_spider.py
# Author     : jirui
# Version    : 1.0
# Date       : 2016/6/21

import requests
from HTMLParser import HTMLParser

url = "http://tieba.baidu.com/f?kw=python&fr=ala0&tpl=5"


def _attr(attrlist, attrname):
    for attr in attrlist:
        if attr[0] == attrname:
            return attr[1]
    return None


# 解析帖子url中的编号
class TiebaParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.in_div = None
        self.num = None
        self.url_list = list()

    def handle_starttag(self, tag, attrs):
        if tag == 'div' and _attr(attrs, 'class') == 't_con cleafix':

            self.in_div = True
        if self.in_div and tag == 'a' and _attr(attrs, 'class') == 'j_th_tit ':
            self.num = _attr(attrs, 'href')
            self.url_list.append(self.num)


# 解析用户名和头像
class UserParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.user_id = None
        self.user_img = None
        self.in_li = None
        self.current_user = {}
        self.userinfo = []

    def handle_starttag(self, tag, attrs):
        if tag == 'li' and _attr(attrs, 'class') == 'icon':
            self.in_li = True
        if self.in_li and tag == 'img':
            self.user_id = (_attr(attrs, 'username'))
            self.user_img = (_attr(attrs, 'src'))
            self.current_user[self.user_id] = self.user_img
            # self.userinfo.append(self.current_user['user'], self.current_user['img'])

    def handle_endtag(self, tag):
        if tag == 'li':
            self.in_li = False


# 通过首页获取帖子编号
class GetUrl():
    def __init__(self):
        self.url = 'http://tieba.baidu.com/f?kw=python&fr=ala0&tpl=5'

    def get_url_num(self):
        # 通过贴吧首页获取当前所有帖子的编号
        r = requests.get(self.url)
        P = TiebaParser()
        P.feed(r.content.decode('utf-8'))
        return P.url_list


# 通过帖子编号获取用户头像链接
class GetPic():
     def __init__(self):
         li = GetUrl().get_url_num()
         for i in li:
            self.url = 'http://tieba.baidu.com/%s' % i

     def get_user_pic(self):
         req = requests.get(self.url)
         P = UserParser()
         P.feed(req.content.decode('utf-8'))
         return P.current_user

# class download_img():

if __name__ == '__main__':

    T = GetPic().get_user_pic()
    print T



