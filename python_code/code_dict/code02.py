# coding:utf-8


# 方法1. 实现 __new__
# 绑定
# 如果 __instance 为None ,说明__instance没有实例化, -->实例化,并返回
# 反之 直接返回 __instance
class Singleton(object):

    # __instance = None

    def __new__(cls, *args, **kwargs):

        # if Singleton.__instance is None:
        #
        #     Singleton.__instance = object.__new__(cls, *args, **kwargs)
        #
        # return Singleton.__instance

        if not hasattr(cls, '_instance'):

            orig = super(Singleton, cls)

            cls._instance = orig.__new__(cls, *args, **kwargs)

        return cls._instance


class MyCLass(Singleton):
    a = 1

m1 = MyCLass()
m2 = MyCLass()

m1.a = 3
print m1.a
# id  == is
print id(m1)
print id(m2)
print m1 == m2


# 方法二 装饰器


def singleton(cls, *args, **kwargs):

    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
    return _singleton


@singleton
class MyClass2():
    a = 1


m1 = MyCLass()
m2 = MyCLass()

m1.a = 3
print m1.a
# id  == is
print id(m1)
print id(m2)
print m1 == m2