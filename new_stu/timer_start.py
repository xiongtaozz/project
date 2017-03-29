import threading
import stu_back
import time
from lxml import etree


def fun_timer():
    stu_back.stuBack().run()
    global timer
    timer = threading.Timer(7200, fun_timer)
    timer.start()
if __name__ == '__main__':
    timer = threading.Timer(1, fun_timer)
    timer.start()
# print time.time()
# print time.localtime(time.time())
