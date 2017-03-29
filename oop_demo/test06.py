# coding:utf-8
# 2017.2.15  简单网络爬虫
import urllib2
import re
import os
# from pip.download import user_agent

if __name__ == '__main__':  # 程序入口
    #  抓取过程
    # 1、访问网页地址，获取网页源代码
    for x in range(1, 36):
        url = 'http://www.qiushibaike.com/8hr/page/%d/?s=4959141' % x    #把访问网页赋值给ur1
    # 设置头部信息
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
    # 头部以下
        headers = {'User-Agent': user_agent}
    # urllib2.urlopen(ur1=ur1,header=headers)打开网页的方法
        request = urllib2.Request(url=url, headers=headers) # 请求的对象
        response = urllib2.urlopen(request)   # 响应传回response

        content = response.read()             # 把网页原代码赋值给content

        # print content                         #打印代码
    # 文件  写入
    #    with open('spdier.html', 'w') as f:
    #        f.write(str(content))
    # 2、根据抓取到的网页源代码去提取想要的数据

    # 用正则表达式对内容进行匹配
    # pattern = re.compile('''class="content">.*?<span>(.*?)</span>', re. S)   #re.s用来匹配换行符
        pattern = re.compile('<a href="(.*?)".*?class="content">.*?<span>(.*?)</sp', re.S)  # [(xx,xx)]
    # 使用findall方法去找代码中的内容    items = re.findall(pattern, content)

        result = re.findall(pattern, content)
    #    print result[1][0].split('/')[-1]

    #    print result[1][1].decode('utf-8')
    #    print items[0].decode('utf-8')
    #    print items[1].decode('utf-8')
        items = result
        # re.rur()
        for item in items:
            print item[1].decode('utf-8')
            print '---------------------'
        # #3、保存抓取的数据

        # path = 'qiubai'
        # if not os.path.exists(path):
        #     os.makedirs(path)
        # file_path = path+'/'+item[1]+'i,txt'
        # f = open(file_path, 'w')
        # f.write(item[0])
        # f.close()
        #4、抓取其他剩下页面的