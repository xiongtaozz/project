# coding:utf-8
from PIL import Image
import os

image_name = 'this.jpg'
# print os.listdir(image_name)
print os.path.join(os.path.dirname(__file__), image_name)


# 根据像素点的颜色值获取字符的函数
def get_chars(pi):
	chars = [' ', ',', '1', '+', 'n', 'D', '@', 'M']
	for k in range(0, 9):
		if pi < (k+1) * 32:
			return chars[7-k]
# 保存文件的函数


def save(image_name, data):
	f = open(image_name+'.txt', 'a+')
	for d in data:
		# print(d)
		f.write(d+'\n')
	f.close()

#入口代码
if __name__ == '__main__':
	# for image_name in os.listdir():
	image_name = 'this.jpg'
	img = Image.open(image_name)
	img = img.convert('L')
	w,h = img.size
	if w > 100:
		h = int((100/w) * h/2)
		w = 100
	img = img.resize((w,h),Image.ANTIALIAS)
	data = []
	for i in range(0,h):
		line = ' '
		for j in range(0,w):
			pi = img.getpixel((j,i))
			line += get_chars(pi)
		data.append(line)
	save(image_name, data)
	print(u'转换成功！')

# print (os.listdir())
