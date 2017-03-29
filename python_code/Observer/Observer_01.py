#coding:utf-8

#观察者模式

# 模式特点：定义了一种一对多的关系，让多个观察对象同时监听一个主题对象，
# 当主题对象状态发生变化时会通知所有观察者。

# 程序实例：公司里有两种上班时趁老板不在时偷懒的员工：
# 看NBA的和看股票行情的，并且事先让老板秘书当老板出现时通知他们继续做手头上的工作。

#观察者
class Observer:
    def __init__(self,strname,strsub):
        self.name = strname
        self.sub = strsub
    def Update(self):
        pass

class StockObserver(Observer):
    #no need to rewrite __init__()
    def Update(self):
        print u"%s:%s,停止看股票，继续工作!" %(self.name,self.sub.action)
class NBAObserver(Observer):
    def Update(self):
        print u"%s:%s,停止看视频，继续工作" %(self.name,self.sub.action)

#主题
class SecretaryBase:
    def __init__(self):
        self.observers = []
    def Attach(self,new_observer):
        pass 
    def Notify(self):
        pass
#观察者detail
class Secretary(SecretaryBase):
    def Attach(self,new_observer):
        self.observers.append(new_observer)
    def Notify(self):
        for p in self.observers:
            p.Update()

if __name__ == "__main__":
    p = Secretary()
    # p2= Secretary()
    s1 = StockObserver("tom",p)
    s2 = NBAObserver("jack",p)
    p.Attach(s1);
    p.Attach(s2);
    p.action = "WARNING:BOSS ";
    p.Notify()