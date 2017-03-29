# coding:utf-8

import requests
import re
import os

'''
   xt
   2016-7-5
   抓取百度贴吧信息作业
'''


class SpiderBaidu(object):

    def __init__(self):
        self.url = 'http://tieba.baidu.com/'

    # 抓取一级页面
    def get_index(self):

        req = requests.get(self.url+'f?kw=python&fr=ala0&tpl=5', auth=('user', 'pass'))
        content = req.text
        pattern = re.compile('<a href="(.*?)".*?class="j_th_tit.*?">.*?</a>')
        return re.findall(pattern, content)

    # 抓取二级页面
    def get_index_down(self, index_url):
        req = requests.get(index_url)
        content = req.content
        print content
        # print content.decode('utf-8')
        pattern = re.compile('<ul class="p_author".*?<li class="icon">.*?<div class="icon_relative j_user_card".*?class="p_author_face.*?".*?img username="(.*?)".*?src="(.*?)".*?/>', re.S)
        return re.findall(pattern, content)

    # 存放文件
    def save_file(self, down_url):
        path = 'maizi'
        if not os.path.exists(path):
            os.makedirs(path)
        # data = urllib.urlopen(down_url).read()
        data = requests.get(down_url[1])
        # if not os.path.exists(path+'/'+down_url[0].decode('utf-8')):
        #     os.makedirs(path+'/'+down_url[0].decode('utf-8'))
        with file(path+'/'+down_url[0].decode('utf-8')+'.jpg', 'wb') as f:
            for chunk in data.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()
        f.close()

    def run(self):
        index_list = self.get_index()
        if index_list:
            for index_url in index_list:  # 查询到一级页面转跳2级页面
                down_list = self.get_index_down(self.url+index_url)
                print down_list
                if down_list:
                    for down_url in down_list:  # 遍历二级页面,并且将用户信息存放在文件夹内
                        self.save_file(down_url)

if __name__ == '__main__':
    spider = SpiderBaidu()
    spider.run()
    # # print spider.get_index()
    # print spider.get_index_down('http://tieba.baidu.com/p/4643593149')
    # http://tb.himg.baidu.com/sys/portrait/item/4f30e4b88de5ada6e4b9a0e6b2a1e69caae69da55a75