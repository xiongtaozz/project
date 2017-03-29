# coding: utf-8
# from threading import *
# from time import *

# condi = Condition()
# def t1():
#     condi.acquire() #加锁
#     try:
#         for i in range(10):
#             print currentThread().name, i
#             sleep(1)
#             if (i == 4): condi.wait() #等待，将当前线程暂停，同时唤醒其他线程
#     finally:
#         condi.release()
#
# def t2():
#     condi.acquire()
#     try:
#         for i in range(10):
#             print currentThread().name, i
#             sleep(1)
#     finally:
#         condi.notify() # 唤醒其他线程
#         condi.release() # 释放锁
#
# Thread(target=t1).start()
# Thread(target=t2).start()

# ---- 捉迷藏的游戏
import threading, time

class Seeker(threading.Thread):
    def __init__(self, cond, name):
        super(Seeker, self).__init__()
        self.cond = cond
        self.name = name

    def run(self):
        self.cond.acquire()
        print self.name + u': 我已经把眼睛蒙上了'

        """
        notify源码解析：
            __waiters = self.__waiters
            waiters = __waiters[:n] # 获取等待队列中的n个等待锁
            for waiter in waiters:
            waiter.release() # 释放Hider的等待锁
            try:
                __waiters.remove(waiter)
            except ValueError:
                pass
        """
        # 释放n个waiter锁，waiter线程准备执行
        self.cond.notify()

        print(u'notifyed...')

        # 释放condition条件锁，waiter线程Hider真正开始执行
        self.cond.wait()
        print('waited...')

        print self.name + u': 我找到你了 ~_~'
        self.cond.notify()
        self.cond.release()

        print self.name + u': 我赢了'

class Hider(threading.Thread):
    def __init__(self, cond, name):
        super(Hider, self).__init__()
        self.cond = cond
        self.name = name
    def run(self):
        self.cond.acquire()

        """
        wait()源码解析：
            waiter = _allocate_lock() # 创建一把等待锁，加入waiters队列，等待notify唤醒
            waiter.acquire() # 获取锁
            self.__waiters.append(waiter)
            saved_state = self._release_save() # 释放condition.lock全局条件锁，以便其他等待线程执行
            if timeout is None:
                waiter.acquire() # 再次获取锁，因为已经锁定无法继续，等待notify执行release
        """
        # wait()释放对琐的占用，同时线程挂起在这里，直到被notify并重新占有琐。
        self.cond.wait()

        print self.name + u': 我已经藏好了，你快来找我吧'
        self.cond.notify()
        self.cond.wait()
        self.cond.release()
        print self.name + u': 被你找到了，哎~~~'

cond = threading.Condition()

hider = Hider(cond, 'hider')
seeker = Seeker(cond, 'seeker')
hider.start()
seeker.start()

hider.join()
seeker.join()
print('end...')
