# coding:utf-8

"""
    工厂模式
    概念:简单工厂模式属于类的创建型模式，适合用来对大量具有共同接口的类进行实例化，
    它可以推迟到运行的时候才动态决定要创建哪个类的实例，而不是在编译时就必须知道要实例化哪个类。
    http://www.cnblogs.com/wuyuegb2312/archive/2013/04/09/3008320.html
"""


class Circle(object):

    def draw(self):
        print 'draw circle'


class Rectangle(object):
    def draw(self):
        print 'draw Rectangle'


class ShapeFactory(object):

    def create(self, shape):
        if shape == 'Circle':
              return Circle()
        elif shape == 'Rectangle':
              return Rectangle()
        else:
              return None

fac = ShapeFactory()
obj = fac.create('Circle')
obj.draw()