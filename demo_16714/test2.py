#coding=utf-8
import random
# 先把共有属性合方法写成一类
# 再把蚂蚁和老鼠的类写出来，用继承重写的特性
# 然后再把场景写出来，关联蚂蚁和老鼠的对象


class com(object):

    step=[+2,-2,+3,-3]

    def __init__(self, gs, point=None):
         self.gs=gs
         if point!=None:
            self.point=random.randint(0,40)
         else:
             self.point=point


     # 同一个类的不同函数参数可以用
    def move(self):

        addstep=random.choice(self.step)

        if 0<addstep+self.point<40:
            self.point+=addstep

    def set_point(self, gs):
        self.gs = gs


class mayi(com):

    def mayige(self, gs, point=None):
        super(mayi, self).__init__(gs, point)
        # self.gs.set_point = ("mayi", self.point)
        self.set_point('mayi')

    def mayige_move(self):
        super(mayi,self).move()
        self.move()


class laoshu(com):
    def laoshuge(self,gs,point=None):
        super(laoshu, self).__init__(gs, point)
        self.gs.set_point=("laoshu", self.point)

    def laoshu_move(self):
        super(laoshu,self).move()
        self.move()

# 场景的本身属性和方法和实例化的老鼠蚂蚁一样，就多1个入场条件

class Run():

    laoshu=laoshu('laoshu')
    mayi=mayi('mayi')
    print "mayi", mayi.mayige(gs='mayi'), "laoshu", laoshu.laoshuge(gs="laoshu")
    if laoshu.laoshuge(gs="laoshu")!=mayi.mayige(gs="mayi") and mayi.mayige(gs="mayi") and laoshu.laoshuge(gs="laoshu") is not None:
          laoshu.move(), mayi.mayige_move()


if __name__ == "__main__":
    Run()
