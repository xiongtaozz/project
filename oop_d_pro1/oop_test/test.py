# coding:utf-8


class Box(object):

    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        self.__tj = self.length * self.width * self.height

    def info(self):
        print u'长度:%d * 高度:%d * 宽度:%d = 体积:%d'% (self.length, self.height, self.width, self.__tj)

if __name__ == '__main__':
    b = Box(1, 2, 3)
    for x in range(1, 6):
        if x ==1:
            b.info()
        else:
            b.__init__(x+1, x+2, x+3)
            b.info()
    # b1 = Box(3, 5, 6)
    # b1.info()