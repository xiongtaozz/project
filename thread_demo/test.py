from PIL import Image

def aaa(pi):
    chars = [' ', ',', '+', '1', 'n', 'D', '&', 'M']
    for k in range(0, 8):
        if pi < (k + 1) * 32:
            return chars[7 - k]

img = Image.open('this.jpg')
if img.mode == 'P' or img.mode == 'RGBA':
    im = Image.new('RGB', img.size, 'white')
    im.paste(img.convert('RGBA'), img.convert('RGBA'))
    img = im
img = img.convert('L')
resize = 0.2
w, h = img.size
h /= 2
w = int(w * resize)
h = int(h * resize)
img = img.resize((w, h), Image.ANTIALIAS)
data = []
pixs = img.load()

for i in range(0, h):
    line = ''
    for j in range(0, w):
        pi = pixs[j, i]
        chars = [' ', ',', '+', '1', 'n', 'D', '&', 'M']
        for k in range(0, 8):
            if pi < (k + 1) * 32:
                line += chars[7 - k]
        # line += aaa(pi)
    data.append(line)

output = open('a.txt', 'w')
for d in data:
    # print(d, file=output)
    # print d
    output.write(d)
output.close()

