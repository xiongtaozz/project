# -*- coding:utf-8 -*-
"""
    @date  : 2016-3-7 11:11:58
    协程，又称微线程，纤程。
    概念:协程是在一个线程执行过程中可以在一个子程序的预定或者随机位置中断，
    然后转而执行别的子程序，在适当的时候再返回来接着执行。
    他本身是一种特殊的子程序或者称作函数。
    1.协程的生成成本更低。其实就是一块内存，记录之前的调用的栈信息。
    你甚至可以通过控制函数调用的层次来进一步降低协程的大小。要生成一个
    协程，只需要申请一块内存并赋值。
    2.切换更快。基本是就是内存的拷贝的速度。
    3.没有线程安全问题。一个进程内可以同时存在多个协程，但是只有一个协程
    是激活的，而且协程的激活和休眠时程序员通过编程来控制，而不是内核来控制的。
    这样就没有了线程安全问题。
    4.可读性更好。相对于IO多路复用来说，你调用的服务接口或者IO接口是异步的，
    但是你的代码是流畅（顺序）的，并没有被异步和回调打乱。协程也是异步的，
    但是它会把异步的事件和回调封装起来，形成类似远程调用接口。
    参考资料:
    http://www.jianshu.com/p/343ffac6eae1
    http://www.cnblogs.com/hymenz/p/3488837.html
"""
# 进程 -- 线程  -- 协程
# 在线程里面 ,如果忘记唤醒,很有可能造成死锁


def A(b):
    print '1'
    print '2'
    b()
    print '3'


def B():
    print 'x'
    print 'y'
    print 'z'

# A(B)

import time
"""
    传统的生产者-消费者模型是一个线程写消息，一个线程取消息，
    通过锁机制控制队列和等待，但一不小心就可能死锁。
    如果改用协程，生产者生产消息后，直接通过yield跳转到消费者开始执行，
    待消费者执行完毕后，切换回生产者继续生产
"""


# 整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，
# 而非线程的抢占式多任务
def consumer():  # 生成器
    r = ''
    while True:
        n = yield r  # 交互口令
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        time.sleep(1)
        r = '200 OK'  # consumer通过yield拿到消息，处理，又通过yield把结果传回 # 5


def produce(c):
    c.next()  # 调用c.next()启动生成器 # 3
    n = 0
    while n < 5:
        n += 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)  # 然后，一旦生产了东西，通过c.send(n)切换到consumer执行 # 4
        print('[PRODUCER] Consumer return: %s' % r)  # produce拿到consumer处理的结果，继续生产下一条消息 # 6
    c.close()  # produce决定不生产了，通过c.close()关闭consumer，整个过程结束 # 7
#  #1 - #7 执行顺序
if __name__ == '__main__':
    # pass
    c = consumer()  # 注意到consumer函数是一个generator（生成器） # 1
    produce(c)  # 把一个consumer传入produce  # 2

