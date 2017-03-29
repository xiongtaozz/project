# -*- coding:utf-8 -*-
import re


"""
    观察者模式又称订阅模式:
    概念:它定义了一种一对多的依赖关系，让多个观察者对象同时鉴定某一个主题对象。这个主题对象在状态发生变化时，
    会通知所有的观察者对象，使它们能够自动更新自己
"""


# 抽象主题类
class Subject(object):
    _observers = []
    action = ''

    def Attach(self, observer):
        self._observers.append(observer)

    def Notfiy(self):
        for o in self._observers:
            o.Update()


# 掌握主题者 --->行使权力者
class Secretary(Subject):
    _observers = []
    action = '老板回来了'


class Boos(Subject):
    _observers = []
    action = '我是老板'
    update = []

    def addeventCB(self, eventCb):
        self.update.append(eventCb)

    def Notfiy(self):
        for o in self.update:
            o()


# 抽象观察者类
class Observer(object):
    name = ''
    sec = None

    def __init__(self, name, sec):
        self.name = name
        self.sec = sec


class StockObserver(Observer):

    def __init__(self, name, sec):
        super(StockObserver, self).__init__(name, sec)

    def Update(self):
        print ("%s, %s, 不要看股票了，继续工作" % (self.sec.action,self.name)).decode('utf-8')

    def CloseStock(self):
        print ("%s, %s, 不要看股票了，快点工作" % (self.sec.action,self.name)).decode('utf-8')


class ShoppingObserver(Observer):

    def __init__(self, name, sec):
        super(ShoppingObserver, self).__init__(name, sec)

    def Update(self):
        print ("%s, %s, 不要看网页了，继续工作" % (self.sec.action,self.name)).decode('utf-8')

    def CloseStock(self):
        print ("%s, %s, 不要看网页了，快点工作" % (self.sec.action,self.name)).decode('utf-8')

if __name__ == '__main__':
    s = Secretary()
    stockobserver = StockObserver('Tom', s)
    shopping = ShoppingObserver('Lily', s)
    s.Attach(stockobserver)
    s.Attach(shopping)
    s.Notfiy()
    print '------->'
    o = Boos()
    stockobserver1 = StockObserver('jeck', o)
    o.addeventCB(stockobserver1.CloseStock)
    shopping = ShoppingObserver('Lily', o)
    o.addeventCB(shopping.CloseStock)
    o.Notfiy()