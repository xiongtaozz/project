# -*- coding: utf-8 -*-
# 导入PIL库中的Image类
from PIL import Image


def get_chars(pi):
    # 像素对应的原始字符，分为8个颜色级别，白色为空字符，黑色为M，从空字符到M颜色深度逐渐递增
    chars = [' ', ',', '1', '+', 'n', 'D', '@', 'M']
    for k in range(0, 8):
        if pi < (k + 1) * 32:
            return chars[7 - k]


def save(image_name, data):
    # 把像素字符列表中的内容保存到文件
    output = open(image_name+'.txt', 'w')
    for d in data:
        # 思考，这里为什么使用write方法写入文件会显示不正常,而使用print就可以
        print(d, file=output)
    output.close()

if __name__ == '__main__':
    # 图片名字
    image_name = 'logo.jpg'
    # 实例化Image，得到img对象
    img = Image.open(image_name)
    # 将图片对象转换为灰度的图片
    img = img.convert('L')
    # 得到图片的大小尺寸
    w, h = img.size
    # 如果图片太大了，高和宽等比例缩小图片
    if w > 100:
        h = int(((100/w) * h)/2)
        w = 100
    # 使用滤镜防止在缩放的时候图像质量下降
    img = img.resize((w, h), Image.ANTIALIAS)
    # 保存像素字符的列表
    data = []
    # 根据图片宽度和高度遍历像素点并取出每个像素点的颜色值
    for i in range(0, h):
        line = ''
        for j in range(0, w):
            # 取出像素点的颜色值
            pi = img.getpixel((j, i))
            # 根据颜色值取出对应的字符
            line += get_chars(pi)
        # 把每行的字符最加到像素字符的列表
        data.append(line)

    # 保存文件
    save(image_name, data)
    print("转换成功！")

