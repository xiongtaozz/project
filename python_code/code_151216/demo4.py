# coding:utf-8
from threading import *
import time

# 'activeCount', 'active_count', 'Condition', 'currentThread',
#            'current_thread', 'enumerate', 'Event',
#            'Lock', 'RLock', 'Semaphore', 'BoundedSemaphore', 'Thread',
#            'Timer', 'setprofile', 'settrace', 'local', 'stack_size'

# 函数方式创建一个线程
# def hello():
#     print 'hello'
#     time.sleep(1)
#     print current_thread().name
#
# if __name__ == '__main__':
#     # print currentThread().name
#     print current_thread().name
#     for i in xrange(5):
#        t = Thread(target=hello)
#        t.start()
# 类方式常见一个线程

# class Hello(Thread):
#     def run(self):
#         print 'hello'
#         time.sleep(1)
#         print current_thread().name
#
# if __name__ == '__main__':
#     # print currentThread().name
#     print current_thread().name
#     # for i in xrange(5):
#     #    t = Thread(target=hello)
#     #    t.start()
#     for i in xrange(5):
#         t = Hello()
#         t.start()
#     print '\n---->',active_count() # 返回所有线程数
#     print '\n--->',enumerate()     # 返回所有线程的列表

cnt = Condition()  # theading.lock

def t1():
    cnt.acquire()  # 枷锁
    try:
        for i in xrange(10):
            print current_thread().name, i
            if i == 4:
                cnt.wait()  # 等待线程,并唤醒其他线程
    finally:
        cnt.release()  # 释放锁


def t2():
    cnt.acquire()
    try:
        for i in xrange(5):
            print currentThread().name, i
        cnt.notify()  # 结束,唤醒
    finally:
        cnt.release()

Thread(target=t1).start()
Thread(target=t2).start()


