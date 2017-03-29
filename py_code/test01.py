#coding= utf-8

# try:
#     int(raw_input('>'))
# except :
#     print 111


def singleton(cls, *args, **kwargs):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _singleton
# def singleton(cls, *args, **kw):
#     instances = {}
#
#     def _singleton():
#         if cls not in instances:
#             instances[cls] = cls(*args, **kw)
#         return instances[cls]
#     return _singleton


@singleton
class MyClass2(object):
    n = 1

    # def __init__(self, x=0):
    #     self.x = x
m3 = MyClass2()
m4 = MyClass2()
# print(id(m1))
# print(id(m2))


m4.n = 3
print(m4.n)