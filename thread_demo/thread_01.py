# coding:utf-8

from threading import *

# 驼峰输入法
# PEP8
# 'activeCount', 'active_count', 'Condition', 'currentThread',
#         'current_thread', 'enumerate', 'Event',
#         'Lock', 'RLock', 'Semaphore', 'BoundedSemaphore', 'Thread',
#         'Timer', 'setprofile', 'settrace', 'local', 'stack_size'

import time


# 函数的方式 多线程
# def hello():
#     time.sleep(1)  # 睡眠1秒
#     # print 'hello'
#     # print dir(current_thread())
#     print current_thread().name  # 主线程 MainThread
#     # print active_count()  # PEP8 (下划线命名)
#     # print activeCount()   # 小驼峰
#
# if __name__ == '__main__':
#     # hello()
#     # for x in xrange(5):
#     #     hello()
#     start = time.time()
#     for i in xrange(5):  # 5个子线程(不包含主线程) iter
#         # hello()
#          t = Thread(target=hello)  # 函数名称
#          t.start()
#     print 'end', time.time() - start
#     print currentThread().name
#     print activeCount()  # 返回线程数量
#     print enumerate()  # 枚举 返回所有线程的列表


# 类的方式---> 多线程
class Hello(Thread):
    def run(self):
        time.sleep(1)
        print 'hello'
        print currentThread().name

if __name__ == '__main__':
    for i in xrange(5):
        t = Hello()  # Thread(target=hello) 错误
        t.start()
    print activeCount()  #
    print enumerate()   # 所有线程的集合,且包含主线程






