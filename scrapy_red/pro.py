# coding:utf-8

import requests
import os
import pytesseract
from PIL import Image
import urllib
import math
import random
import xlutils


# 获取图片
def img2str(pic_url):
    # 将验证码图片先临时保存到电脑上
    urllib.urlretrieve(pic_url, 'varcode.jpg')
    # print os.path.dirname(__file__)+'\\'+'varcode.jpg'
    # 读取验证码图片
    img = Image.open('varcode.jpg')
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

yzm_url = 'http://202.118.88.140:8088/validateCodeAction.do?random='+str(random.random())
login_url = 'http://202.118.88.140:8088/loginAction.do'
# html = requests.get('http://202.118.88.140/')
loginer = requests.session()

# print html.content
while True:
    varcode = img2str(yzm_url)
    data = {
    'mm': '1111',
    'v_yzm': '1111',
    'zjh': '1111'
    }
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'
    referer = 'http://202.118.88.140:8088/'
    host = 'www.guahao.com'
    html = loginer.post(url=login_url, data=data, headers={'User-Agent': user_agent, 'Referer': referer, 'host': host})
    with open('test.html', 'w') as f:
        f.write(str(html.content))
        f.close()
    break