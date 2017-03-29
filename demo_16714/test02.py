# coding:utf-8


class Box(object):

    def __init__(self, width, height, length):
        self.width = width
        self.height = height
        self.length = length
        self._open = True
        self._color = None
        self.tj = self.width * self.height * self.length

    def set_cl(self, cl):
        self._color = cl
        print self._color

    def open_box(self):
        if self._open:
            self._open = True
        return self._open

    def close_box(self):
        self._open = False
        return self._open

    def run(self):
        if self.open_box():   # 判断盒子是否是代开状态
            self.set_cl('red')  # 修改颜色
            self.close_box()  # 关闭盒子
        else:
            print u'盒子是关闭状态'

if __name__ == "__main__":
    box = Box(1, 2, 3)
    box.run()  # 第一次调用
    box.run()  # 尝试第二次调用,则为关闭状态



