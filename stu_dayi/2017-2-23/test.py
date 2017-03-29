# coding:utf-8
# 2017.2.15  简单网络爬虫
import urllib2
import re
import os
# from pip.download import user_agent

if __name__ == '__main__':                          # 程序入口
    print '开始抓取内容'.decode('utf-8')
    for i in range(1, 35):                          # 4、抓取其他剩下页面的
          # 1、访问网页地址，获取网页源代码
        url = 'http://www.qiushibaike.com/8hr/page/'+str(i)+'/?s=4957471'    # 把访问网页赋值给ur1
# 设置头部信息
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
        headers = {'User-Agent': user_agent}        # 模拟浏览器
        try:                                        # 异常处理
            request = urllib2.Request(url=url, headers=headers)  # 请求的对象
            # urllib2.urlopen(ur1=ur1,header=headers)  打开网页的方法
            response = urllib2.urlopen(request)     # 响应传回response
        except urllib2.HTTPError as e:              # 异常处理语句
            print e                                 # e为异常对象
            exit()                                  # 出现异常停止程序
        except urllib2.URLErr as e:
            # print e
            print '网络无法访问'.decode('utf-8')
            exit()
        content = response.read()                   # 把网页原代码赋值给content

    # 2 .根据抓取到的网页源代码去提取想要的数据
    # 用正则表达式对内容进行匹配
        pattern = re.compile('<a href="(.*?)".*?class="content">.*?<span>(.*?)</sp', re.S)  # [(xx,xx)]
    # 使用findall方法去找代码中的内容，生成一个二维元组    items = re.findall(pattern, content)
        result = re.findall(pattern, content)       # 元组
#    print result[1][0].split('/')[-1]
#    print result[0][1].decode('utf-8')

        for item in result:
    # print item[1].decode('utf-8')      # 通过元组下标，来获取文内容   [0]是时间
    # 把多余的字符换掉
            item_new = item[1].replace('\n', '').replace('<br/>', '\n')
    # 3、保存抓取的数据
# 判断是否有zyysg这个文件的路径
            zyysg = 'D:\\'
            if not os.path.exists(zyysg):            #' 判断是否有这个文件
                os.makedirs(zyysg)                   # 如果没有就创建一个
            file_path = zyysg+item[0].split('/')[-1]+'.txt'    # 创建文件，并以时间作为文件的名字
            f = open(file_path, 'w')                  # ‘w’以写入的方式打开文件
            f.write(item_new)                        # 写入文件内容
            f.close()                                # 写入后关闭文件
    # 4、抓取其他剩下页面的
print '抓取完成'.decode('utf-8')
