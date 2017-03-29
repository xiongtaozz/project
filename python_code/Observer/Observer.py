
#coding=utf-8

#主题
class Subject:
    def registerObserver(self, observer):
        pass
    def removeObserver(self, observer):
        pass
    def notifyObservers(self):
        pass

#订阅
class Observer:
    def update(self, who):
        pass
    def display(self):
        pass

#主题
class QQInfo(Subject):
    def __init__(self):
        #订阅者 python7月班所有同学
        self.observers = []
    #注册订阅者
    def registerObserver(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
    #注销订阅者
    def removeObserver(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)
    #通知
    def notifyObservers(self):
        for o in self.observers:
            o.update(self.whichTeacher)

    def whichOneCome(self, who):
        #来的是谁？
        self.whichTeacher = who
        self.notifyObservers()
class Student(Observer):
    def __init__(self, name):
        self.name = name
    def update(self, who):
        self.whichTeacher = who
        self.display()
    def display(self):
        if self.whichTeacher == u"蒋老师":
            print(u"%s：小蒋老师！"%self.name)
        elif self.whichTeacher == u"胡老师":
            print(u"%s：咱们这边后端用Django前端用bootstrp吗？"%self.name)
        else:
            print(u"%s：%s，这是哪位老师？"  % (self.name, self.whichTeacher))


if __name__ == "__main__":
    print(u"\n使用观察者模式实现大家对于不同老师上线的不同反应，哈哈！")
    newinfo = QQInfo()
    zy = Student(u"邹一")
    md = Student(u"马东")
    zs = Student(u"张三")
    newinfo.registerObserver(zy)
    newinfo.registerObserver(md)
    print(u"\n蒋老师上线了，看看大家什么反应？")
    newinfo.whichOneCome(u"蒋老师")
    print(u"\n胡老师上线了，看看大家什么反应？")
    newinfo.whichOneCome(u"胡老师")
    print(u"\n助教美女上线了，看看大家什么反应？")
    newinfo.whichOneCome(u"助教美女")
