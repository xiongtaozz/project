# -*- coding: utf-8 -*-
"""
需求：记录一个函数运行的日志
"""
import logging
import datetime
import inspect
from rest_framework import utils

logging.basicConfig(level=logging.DEBUG, filename='python31.log')


# 最初的代码
def func1():
    print 'i am func1'
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logging.debug('函数名：func1, 参数：无，调用时间：'+now)


def func2():
    print 'i am func2'
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logging.debug('函数名：func2, 参数：无，调用时间：'+now)

# func1()
# func2()


# 改进一： 函数嵌套
def write_log(func):
    func()
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logging.debug('函数名：'+func.func_name+', 参数：无，调用时间：'+now)


def func1():
    print 'i am func1'


def func2():
    print 'i am func2'

# write_log(func1)
# write_log(func2)


# 改进二：
def write_log(func):   # 函数嵌套 --加闭包
    def wrapper():
        func()
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logging.debug('函数名：'+func.func_name+', 参数：无，调用时间：'+now)
    return wrapper


def func1():
    print 'i am func1'


def func2():
    print 'i am func2'

# write_log(func1)()
# write_log(func2)()
# print func1, func2
# func1()
# func2()


# 改进三：
def write_log(func):
    def wrapper():
        func()
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logging.debug('函数名：'+func.func_name+', 参数：无，调用时间：'+now)
    return wrapper


@write_log
def func1():
    print 'i am func1'


@write_log
def func2():
    print 'i am func2'

# func1()
# func2()

# 新的问题：有些函数是有参数的，怎么办？


def write_log(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        all_args = inspect.getargspec(func)  # 参数结果
        logging.debug('函数名：'+func.func_name+', 参数：'+str(all_args)+'，调用时间：'+now)
    return wrapper


@write_log
def func1():
    print 'i am func1'


@write_log
def func2():
    print 'i am func2'


@write_log
def func3(arg):
    print 'i am func3, args:'+str(arg)


@write_log
def func4(arg1, arg2=None):
    print 'i am func3, args:', str(arg1)+','+str(arg2)


@write_log
def func5(*args, **kwargs):
    print 'i am func3, args:'+str(args)+','+str(kwargs)
# func1()
# func2()
# func3(3)
# func4(arg1=4)
# func5(1, 2, 3, 4, a=3, b=2, c=1)

# 再进一步，给装饰器设定参数。调用时间设为可选


def write_log(call_time):
    def wrapper2(func):
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            all_args = inspect.getargspec(func)
            log_info = '函数名：'+func.func_name+', 参数：'+str(all_args)
            if call_time:
                log_info += '，调用时间：'+now
            logging.debug(log_info)
        return wrapper
    return wrapper2

''.strip()

@write_log(call_time=False)
def func1():
    print 'i am func1'


@write_log(call_time=True)
def func2():
    print 'i am func1'

func1()
func2()

# 再进一步，封装整理装饰器，写成单独的模块