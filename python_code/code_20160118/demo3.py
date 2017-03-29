# coding: utf-8
# import threading
import time
from threading import *

mydata = local()
mydata.x = 1

class HelloThread(Thread):
    def run(self):
        print "hello world"
        print current_thread()
        # print mydata.__dict__
        # mydata.x = 2
        # print mydata.__dict__
        time.sleep(1)

if __name__ == "__main__":
    start = time.clock()
    for i in xrange(5):
        t = HelloThread()
        t.start()
    end = time.clock()
    print "used:"+str(end-start)
    print current_thread()
    # print active_count()
    # print enumerate()
    # print mydata.__dict__

# def hello():
#     print "hello, world"
#     t = Timer(3, hello)
#     t.start()
#
# t = Timer(3, hello)
# t.start()