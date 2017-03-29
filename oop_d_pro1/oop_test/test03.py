# coding:utf-8
from weakref import WeakKeyDictionary


class NonNegative(object):
    """A descriptor that forbids negative values"""
    def __init__(self, default):
        if default < 7:
            self.default = default
        else:
            self.default = 1
        self.data = WeakKeyDictionary()

    def __get__(self, instance, owner):
        # we get here when someone calls x.d, and d is a NonNegative instance
        # instance = x
        # owner = type(x)
        return self.data.get(instance, self.default)

    def __set__(self, instance, value):
        # we get here when someone calls x.d = val, and d is a NonNegative instance
        # instance = x
        # value = val
        if value < 0:
            raise ValueError("Negative value not allowed: %s" % value)
            # self.data[instance] = 1
        self.data[instance] = value


class Box(object):
    length = NonNegative(0)
    width = NonNegative(0)
    height = NonNegative(0)
    mian = NonNegative(0)

    def __init__(self, length, width, height, mian):
        self.length = length
        self.width = width
        self.height = height
        self.mian = NonNegative(mian)
        self.__tj = self.length * self.width * self.height
        self._color = 'red'
        self.flag = False

    def info(self):
        print u'长度:%d * 高度:%d * 宽度:%d = 体积:%d'% (self.length, self.height, self.width, self.__tj)

    def print_tj(self):
        print self.__tj

    # def add_col(self, color):
    #     self._color = color
    #
    # def print_col(self):
    #     print self._color

    def open_or_close(self):
        if self.flag:
            print u'盒子已经打开'
        else:
            print u'盒子是关闭状态'

    @property
    def color(self):
        print self._color

    @color.setter
    def color(self, col):
        self._color = col

    def __call__(self, *args, **kwargs):
        return self.__tj
if __name__ == '__main__':
    b = Box(1, 2, 3, 10)
    print b.mian.default
    print b()
