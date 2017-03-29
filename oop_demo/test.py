# -*- coding:utf-8 -*-


# class A:
#     __a = 1
#
#     def __init__(self):
#         self.b = 2
#
#     def add(self):
#
#         print self.__a, self.b
# x = A()
# x.add()

import time
import threading
# class ThreadClass(threading.Thread):
#
#      def __init__(self, fun):
#         threading.Thread.__init__(self)
#         self.fun = fun()
#
#      def run(self):
#         self.fun
#
#
# def loop():
#     # print 'start loop ',time.strftime("%H:%M:%S")+"\n";
#     time.sleep(1)
#
#     # print 'end loop ',time.strftime("%H:%M:%S")+"\n";
#
#
# def main():
#     threads=[]
#     for i in range(10):
#         t = ThreadClass(loop)
#         # threads.append(t)
#         # t.start()
#     for i in range(10):
#         threads[i].start()
#     for i in range(10):
#         threads[i].join()
# print 'all start time ', time.strftime("%H:%M:%S")+"\n"
# main()
# print 'all end time ', time.strftime("%H:%M:%S")+"\n"

import random
import concurrent.futures, multiprocessing


def read(q):
        print('Get %s from queue.' % q)
        time.sleep(random.random())


def main():
    futures = set()
    with concurrent.futures.ThreadPoolExecutor(multiprocessing.cpu_count()*4) as executor:
        for q in (chr(ord('A')+i) for i in range(26)):
            future = executor.submit(read, q)
            futures.add(future)
    try:
        for future in concurrent.futures.as_completed(futures):
            err = future.exception()
            if err is not None:
                raise err
    except KeyboardInterrupt:
        print("stopped by hand")

if __name__ == '__main__':
    main()