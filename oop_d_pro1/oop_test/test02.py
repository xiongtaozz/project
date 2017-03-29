# coding:utf-8


class Box(object):

    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        self.__tj = self.length * self.width * self.height
        # self._color = 'red'
        self.flag = False

    def info(self):
        print u'长度:%d * 高度:%d * 宽度:%d = 体积:%d'% (self.length, self.height, self.width, self.__tj)

    def print_tj(self):
        print self.__tj

    def add_col(self, color):
        self._color = color

    def print_col(self):
        print self._color

    def open_or_close(self):
        if self.flag:
            print u'盒子已经打开'
        else:
            print u'盒子是关闭状态'
if __name__ == '__main__':
    b = Box(1, 2, 3)
    b.flag = True  # 手动打开盒子
    if b.flag:
        b.print_tj()
        b.add_col('red')
        b.print_col()
    b.open_or_close()