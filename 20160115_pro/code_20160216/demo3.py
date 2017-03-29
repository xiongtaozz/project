# -*- coding:utf-8 -*-

import urllib2, re

'''
   函数方式抓取麦子官网所有教师信息
'''


# 抓取网页内容
def get_page(pageIndex):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36'}
    request = urllib2.Request(url='http://www.maiziedu.com/course/teachers/?page=%s' % str(pageIndex), headers=headers)
    response = urllib2.urlopen(request)
    return response.read()


# 筛选内容
def analysis(html):
    recmp = '<div class="teacherListR">[\s|\S]*?<p class="font20 color00 marginB14 t3out p">' \
            '(.*)<a href="/[a-z]{0,}/[a-z]{0,}/[a-z]{0,}/[0-9]{0,}/" class="go font12">.*' \
            '</a></p>[\s|\S]*?<p class="color66 marginB14"><span class="color99">.*</span></p>[\s|\S]*?' \
            '<p class="color66"><span class="color99">.*</span>(.*)</p>[\s|\S]*?</div>'
    pattern = re.compile(recmp)
    return re.findall(pattern, html)


# 保存内容
def save(items):
    for item in items:
        save_file('maizi.txt',item)


# 存放地址
def save_file(path, item):
        f = open(path, 'a+')
        try:
            f.write(item[0]+':\n'+item[1]+'\n')
        except Exception as e:
            print e
        else:
            f.close()
        finally:
            pass


def run(page):
    try:
        print u'开始从%d抓取内容....'% page
        # count = 所有的html
        # items = 筛选
        save(analysis(get_page(page)))
        print u'内容第%d抓取完毕....'% page
    except urllib2.HTTPError as e:
        print e
    except urllib2.URLError as e:
        print e
    except Exception as e:
        print e


if __name__ == '__main__':
    for x in range(1, 21):
        run(x)
