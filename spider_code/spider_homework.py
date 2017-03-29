# coding:utf-8
import requests
import re
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


from HTMLParser import HTMLParser


def _attr(attrs, attrname):
    for attr in attrs:
        if attr[0] == attrname:
            return attr[1]
    return None


class PoemParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.in_span = False
        self.in_a = False
        self.pattern = re.compile(r'.*')
        self.user_list = []
        self.current_poem = {}

    # def handle_starttag(self, tag, attrs):
    #     if tag == 'div' and _attr(attrs, 'class') == 'threadlist_author pull_right':
    #         self.in_div = True
    #
    #     if self.in_div and tag == 'a':
    #         self.in_a = True
    #         self.current_poem['url'] = _attr(attrs, 'href')

    def handle_starttag(self, tag, attrs):
        if tag == 'span' and _attr(attrs, 'class') == 'frs-author-name-wrap':
            self.in_span = True

        if self.in_span and tag == 'a':
            self.in_a = True
            self.current_poem['url'] = _attr(attrs, 'href')

    def handle_endtag(self, tag):
        if tag == 'span':
            self.in_span = False
        if tag == 'a':
            self.in_a = False

    def handle_data(self, data):
        if self.in_a:
            # print (data)
            m = self.pattern.match(data)
            if m:
                self.current_poem['name'] = m.group()
                self.user_list.append(self.current_poem)
                self.current_poem = {}


class PoemContentParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.in_a = False
        self.in_img = False
        self.content = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a' and _attr(attrs, 'class') == 'userinfo_head':
            self.in_div = True

        if self.in_a and tag == 'img':
            self.in_img = True
            self.current_poem['img'] = _attr(attrs, 'src')

    def handle_endtag(self, tag):
        if tag == 'a':
            self.in_div = False

        if tag == 'img':
            self.in_img = False


    def handle_data(self, data):
        if self.in_img:
            self.content.append(data)


def retrive_user_tieba():
    url = 'http://tieba.baidu.com/f?kw=python&fr=ala0&tpl=5'
    r = requests.get(url)
    p = PoemParser()
    p.feed(r.content.decode('utf-8'))
    # print p.user_list
    return p.user_list

def download_poem(poem):
    url = 'http://tieba.baidu.com' + poem['url']
    print (url)
    r = requests.get(url)
    # # print (r.url)
    parser = PoemContentParser()
    print r.content
    parser.feed(str(r.content).decode('gbk'))
    poem['content'] = parser.content
    # print (poem['content'])


if __name__ == '__main__':
    l = retrive_user_tieba()
    # download_poem()
    # for i in range(len(l)):
    #     print (i, l[i]['url'])

    #download all poem
    for i in range(len(l)):
        # print ('http://tieba.baidu.com' + l[i]['url'])
        download_poem(l[i])
        # print (download_poem(l[i]))
        # print (i, l[i]['url'])
    # print('total %d poems.' % len(l))
    # for i in range(10):


