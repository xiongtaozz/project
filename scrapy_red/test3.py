# coding:utf-8
from PIL import Image
import pytesseract
import urllib2
import urllib
import json
import time
import cookielib
import re
import os

def img2str(pic_url):
    # 将验证码图片先临时保存到电脑上
    # urllib.urlretrieve(pic_url, 'varcode.jpg')
    print os.path.dirname(__file__)+'\\'+'varcode.jpg'
    # 读取验证码图片
    img = Image.open(os.path.dirname(__file__)+'\\'+'varcode.jpg')
    # 转为灰度图片
    img = img.convert('L')
    # 二值化处理（去噪）
    threshold = 130  # 阈值
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    img = img.point(table, '1')
    print pytesseract.image_to_string(img)
    # 读取图片上的值
    return pytesseract.image_to_string(img)

login_url = 'http://202.118.88.140/loginAction.do'
pic_url = 'http://www.guahao.com/validcode/genimage/2188407'

while True:
    # varcode = img2str(pic_url)
    # print '猜测的验证码是:', varcode
    cj = cookielib.LWPCookieJar()
    cookie_support = urllib2.HTTPCookieProcessor(cj)
    opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    varcode = raw_input('>')
    urllib2.urlopen('http://202.118.88.140/')
    urllib.urlretrieve('')
    values = {'zjh': '20051084', 'mm': '980608', 'v_yzm': varcode.strip()}
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'
    referer = 'http://202.118.88.140/'
    host = 'http://202.118.88.140/'
    origin = 'http://202.118.88.140/'
    upgrade_insecure_requests = '1'
    headers = {'User-Agent': user_agent, 'Referer': referer, 'Host': host, 'Origin': origin,
               'Upgrade-Insecure-Requests': upgrade_insecure_requests}
    data = urllib.urlencode(values).encode('utf-8')
    request = urllib2.Request(url=login_url, data=data, headers=headers)
    response = urllib2.urlopen(request)
    with open('test3.html', 'w') as f:
        f.write(str(response.read()))
        f.close()
    break
    # content = json.loads(response.read().decode('utf-8'))
    # print(content)
    # if content['message'] == '登录成功':
    #     print('登录成功')
    #     break
    # time.sleep(5)

# 抓取登录后的页面内容
# address_url = 'http://www.guahao.com/my/goods/list'
# content = urllib2.urlopen(url=address_url).read().decode('utf-8')
# f = open('t.html', 'w', encoding='utf-8')
# f.write(content)
# f.close()
# print('保存成功')
#
#
# # 解析抓取到的内容
# regex = re.compile('<tr>.*?<td class="name J_MyName">(.*?)</td>.*?<td class='+
#    '"J_MyTel">(.*?)</td>.*?<td class="addr J_MyAddress"><p>(.*?)</p>.*?</tr>',
#    re.S)
# items = regex.findall(content)
# for item in items:
#     print("姓名:%s, 电话:%s, 地址:%s"%(item[0],item[1],item[2]
#         .replace(' &nbsp;','').replace('<label>','').replace('</label>','')))
# print('解析完毕')


# 后续处理，数据分析及索引入库，数据展示等内容值得期待。


