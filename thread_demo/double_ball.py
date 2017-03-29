# -*- coding:utf-8 -*-
import random


class doubleBall(object):

    def __init__(self):
        self.red_ball = range(1, 33)
        self.blue_ball = range(1, 17)
        self.ball_all = []

    def shai_red(self):
        self.ball_all = random.sample(self.red_ball, 6)
        return

    def shai_blue(self):
        self.ball_all.append(random.choice(self.blue_ball))
        return self.ball_all

    def ben_ball(self):
        self.ke_ball = [1, 2, 3, 4, 5, 6, 7]

    def run(self):
        self.shai_red()
        self.shai_blue()
        print self.ball_all

if __name__ == '__main__':
    double = doubleBall()
    double.run()