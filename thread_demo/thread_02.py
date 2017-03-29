# coding:utf-8
from threading import *


cnt = Condition()  # theading.lock 


def t1():
    cnt.acquire()  # 枷锁  枷锁之后一定要释放锁.. (死锁)
    try:
        for i in xrange(5):
            print current_thread().name, i
            if i == 2:
                cnt.wait()  # 等待线程,并唤醒其他线程
    finally:
        print 't1'
        cnt.release()  # 释放锁


def t2():
    cnt.acquire()
    try:
        for i in xrange(3):
            print currentThread().name, i
        cnt.notify()  # 结束,唤醒
    finally:
        print 't2'
        cnt.release()

Thread(target=t1).start()
Thread(target=t2).start()


