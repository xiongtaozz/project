# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse
import re
import os
if __name__ == "__main__":
    # 抓取过程
    # 1、访问其中一个的网页地址，获取网页源代码
    for i in range(1, 36):
        url = "http://www.qiushibaike.com/textnew/page/" + str(i) + "/?s=4846622"
        user_agent ='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.87 Safari/537.36 QQBrowser/9.2.5748.400'
        headers = {'User-Agent': user_agent}
        request = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(request)
        content = response.read().decode('utf-8')
        # 2、根据抓取到的网页源代码去提取数据
        s = '<div class="content">(.*?)<!--(.*?)-->.*?</div>'
        pattern = re.compile(s, re.S)
        items = re.findall(pattern, content)
        js = 0
        for item in items:
            print(item[1], item[0])
            js += 1
            # 保存之前先把多余的换行符去掉，再把<br/>换成\n
            item_new = item[0].replace('\n', '').replace('<br/>', '\n')
            # 3、保存抓取的数据
            path = 'qiubai4'
            if not os.path.exists(path):
                os.makedirs(path)
            file_path = path + '/'+item[1] + '.txt'
            f = open(file_path, 'w')
            f.write(item_new)
            f.close()
        print('js', js)
        # 4、把剩下所有的网页的内容
    print('OVER')
