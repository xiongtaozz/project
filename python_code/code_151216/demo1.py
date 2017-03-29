# coding:utf-8

from threading import *

# 'activeCount', 'active_count', 'Condition', 'currentThread',
#            'current_thread', 'enumerate', 'Event',
#            'Lock', 'RLock', 'Semaphore', 'BoundedSemaphore', 'Thread',
#            'Timer', 'setprofile', 'settrace', 'local', 'stack_size'


import time


def hello():
    print 'hello'
    time.sleep(1)
    print currentThread().name

if __name__ == '__main__':
    # print current_thread().name

    start = time.time()
    for i in xrange(5):
        t = Thread(target=hello)
        t.start()
    print 'end:', (time.time()-start)
    print currentThread().name
    print active_count()

# class Hello(Thread):
#     def run(self):
#         print 'hello'
#         time.sleep(1)
#         print currentThread().name
# if __name__ == '__main__':
#     for i in range(5):
#         t = Hello()
#         t.start()

# cnt = Condition() #lock
# print currentThread().name
# def t1():
#     cnt.acquire()
#     try:
#         for i in xrange(10):
#             print currentThread().name,i
#             if i == 4:
#                 cnt.wait()
#     finally:
#         cnt.release()
# def t2():
#     cnt.acquire()
#     try:
#         for i in xrange(5):
#             print currentThread().name,i
#             cnt.notify()
#     finally:
#         cnt.release()
#
# Thread(target=t1).start()
# Thread(target=t2).start()