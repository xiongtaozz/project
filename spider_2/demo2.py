# coding:utf-8

import re
import urllib2
import os  # 文件管理 sys

if __name__ == '__main__':
    print u'开始'
    for i in range(1, 23):
        url = 'http://www.maiziedu.com/course/teachers/?page='+str(i)
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                                '(KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'}
        try:
            request = urllib2.Request(url=url, headers=headers)
            response = urllib2.urlopen(request)
            content = response.read()  # html 里面内容
        except urllib2.HTTPError as e:
            print e
            exit()
        except urllib2.URLError as e:
            print e
            exit()
        Pattern = re.compile('p">(.*?)<a href.*?简介：</span>(.*?)</p>.*?</div>', re.S)
        items = re.findall(Pattern, content)
        path = 'maizi'
        if not os.path.exists(path):
            os.makedirs(path)
        file_path = path+'/'+'teacher'+'.txt'  # maizi\teacher.txt
        f = open(file_path, 'a+')  # a a+
        for item in items:
            f.write(item[0]+':\n'+item[1] + '\n')  # 转义符 \r \t
            # 姓名:
            # 简介内容 \n
            # f.write('\n')
        f.close()
    print u'结束'

