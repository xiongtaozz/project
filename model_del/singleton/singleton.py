# coding:utf-8

# 单例模式


class Singleton1(object):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance1 = super(Singleton1, cls).__new__(cls, *args, **kwargs)
            # return _instance1
        return cls._instance

sin1 = Singleton1()
sin2 = Singleton1()

print (id(sin1))
print (id(sin2))