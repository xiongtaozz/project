# coding:utf-8


def decorator(args):
    def _deco(func):
        def _func(self):
            # 注意 self 是作为参数传进来的
            self.i = args
            func(self)
        return _func
    return _deco


class Foo(object):
    @decorator(123)
    def bar(self):
        # 输出 123
        print('i:', self.i)

Foo().bar()


