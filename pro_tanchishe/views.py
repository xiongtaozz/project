# -*- coding:utf-8 -*-
from Tkinter import *
from tkMessageBox import showerror, askyesno, showinfo
from random import sample, choice


class Channel(object):
    def __init__(self, id, startx, free=True, bottomy=570):
        self.id=id
        self.startx=startx
        self.free=free
        self.bottomy=bottomy


class GofGame(object):

    def __init__(self):
        self.root = Tk()
        self.root.title(u'贪吃蛇')
        self.root.resizable(False, False)
        self.makemenu(self.root)
        self.canvas = Canvas(self.root, width=600, height=400, bg='#FFFFE0')
        self.canvas.pack()
        self.score = 0
        self.level = 1
        self.scoreboard = None

    def makemenu(self, win):
        top = Menu(win)
        win.config(menu=top)
        game = Menu(top, tearoff=False)
        game.add_command(label=u'开始新游戏', command=self.new_game, underline=0)
        game.add_command(label=u'暂停游戏', command=self.notdone, underline=0)
        game.add_command(label=u'恢复游戏', command=self.notdone, underline=0)
        game.add_command(label=u'退出游戏', command=self.root.destroy, underline=0)
        top.add_cascade(label=u'游戏', menu=game, underline=0)
        help_ = Menu(top, tearoff=False)
        help_.add_command(label=u'游戏玩法',
                          command=lambda: showinfo(u'游戏玩法', u'通过上下左右控制蛇的方向，游戏结束.'),
                          underline=0)
        help_.add_command(label=u'关于贪吃蛇',
                          command=lambda: showinfo(u'关于贪吃蛇', u'贪吃蛇1.0'),
                          underline=0)
        top.add_cascade(label=u'帮助', menu=help_, underline=0)

    def new_game(self):
        self.canvas.destroy()
        if self.scoreboard:
            self.scoreboard.destroy()
        # self.canvas = Canvas(master, width=self.width+2*self.offset, height=self.height+2*self.offset, bg=self.bg)
        self.canvas = Canvas(self.root, width=600+2*10, height=400+2*10, bg='#FFFFE0')
        self.canvas.pack()
        self.score = 0
        self.level = 1
        self.state = 'ing'
        self.item_dict = {}
        self.channel_list = [Channel(x, 25+50*x) for x in range(12)]
        self.start_fall()

    def notdone(self):
        pass


if __name__ == '__main__':
    GofGame()
    mainloop()