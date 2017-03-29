#!/usr/bin/env python
# -*- coding:utf-8 -*-

from Tkinter import *
from tkMessageBox import showerror, askyesno, showinfo
from random import sample, choice


class CanvasItem(object):
    def __init__(self,x,y,channel,state='down'):
        self.x=x
        self.y=y
        self.channel=channel
        self.state=state


class Channel(object):
    def __init__(self, id, startx, free=True, bottomy=570):
        self.id=id
        self.startx=startx
        self.free=free
        self.bottomy=bottomy


class ScoreBoard(Frame):
    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.pack(side=TOP, fill=X)
        self.label1=Label(self, text=u'得分: 0'+' '*9, fg='red')
        self.label2=Label(self, text=u'等级: 1'+' '*5, fg='red')
        self.label3=Label(self, text=u'  请用键盘敲击图中对应字符',fg='red')
        self.label2.pack(side=RIGHT)
        self.label1.pack(side=RIGHT)
        self.label3.pack(side=LEFT)

    def update(self, score, level):
        self.label1.config(text=u'得分: '+str(score)+' '*(10-len(str(score))))
        self.label2.config(text=u'等级: '+str(level)+' '*(6-len(str(level))))
        

class TypingGame(object):
    def __init__(self):
        self.root= Tk()
        self.root.title(u'打字游戏1.0')
        self.root.resizable(False,False)
        self.makemenu(self.root)
        self.canvas=Canvas(self.root, width=600, height=600, bg='white')
        self.canvas.pack()
        self.score=0
        self.level=1
        self.scoreboard=None
        for x in ['A','B','C','D','E','F','G','H']:
            self.root.bind('<KeyPress-'+x.lower()+'>', lambda event, x=x: self.move_up_choose(x))
  
    def notdone(self):
        showerror(u'警告', u'该模块尚未完成')

    def makemenu(self, win):
        top=Menu(win)
        win.config(menu=top)
        game=Menu(top,tearoff=False)
        game.add_command(label=u'开始新游戏',command=self.new_game,underline=0)
        game.add_command(label=u'暂停游戏',command=self.notdone,underline=0)
        game.add_command(label=u'恢复游戏',command=self.notdone,underline=0)
        game.add_command(label=u'退出游戏',command=self.root.destroy,underline=0)
        top.add_cascade(label=u'游戏',menu=game,underline=0)
        help_=Menu(top,tearoff=False)
        help_.add_command(label=u'游戏玩法',
                          command=lambda: showinfo(u'游戏玩法', u'请用键盘敲击图中对应字符，每击中一个得10分，每得200分等级加1，下落速度变快，字符堆积到窗口顶部时，游戏结束.'),
                          underline=0)
        help_.add_command(label=u'关于打字游戏',
                          command=lambda: showinfo(u'关于打字游戏', u'打字游戏1.0'),
                          underline=0)
        top.add_cascade(label=u'帮助', menu=help_, underline=0)

    def move_down(self,item_id):
        if self.item_dict[item_id].state == 'up' or self.state == 'pause':
            return
        elif self.item_dict[item_id].y<self.item_dict[item_id].channel.bottomy:
            self.canvas.move(item_id,0,10)
            self.item_dict[item_id].y+=10
            # print self.item_dict[item_id].y
            self.canvas.after(int(400/pow(1.3,self.level-1)),self.move_down,item_id)
        else:
            self.item_dict[item_id].channel.bottomy-=60
            print str(self.item_dict[item_id].channel.id)+u'号管道bottomy is: '+str(self.item_dict[item_id].channel.bottomy)
            if self.item_dict[item_id].channel.bottomy==-30:
                self.pause_game()
                if askyesno(u'游戏结束', u'游戏结束，是否开始新游戏'):
                    self.new_game()
                else:
                    self.root.destroy()
            self.canvas.itemconfig(item_id,tag='Del')

    def move_up_choose(self,tag):
        if self.state=='pause':
            return
        try:
            item_id=self.canvas.find_withtag(tag)[0]
        except Exception:
            item_id=0
        if item_id:
            self.canvas.itemconfig(item_id,image=self.photo1_list[ord(tag)-65])
            self.canvas.itemconfig(item_id,tags='Del')
            self.item_dict[item_id].state='up'
            self.score+=10
            if not self.score%200:
                self.level+=1
            print u'击中的item_id,标签,channel_id:  '+str(item_id)+'  '+tag+'  '+str(self.item_dict[item_id].channel.id)
            print u'当前得分,等级:  '+str(self.score)+'  '+str(self.level)
            self.scoreboard.update(self.score,self.level)
            self.move_up(item_id)
        
    def move_up(self, item_id, n=0):
        if n<60:
            self.canvas.move(item_id,0,-10)
            self.canvas.after(20,self.move_up,item_id,n+1)
        
    def start_fall(self):
        if self.state=='pause':
            return
        for channel_id in sample(range(12),5):
            tag_=choice(range(8))
            item_id=self.canvas.create_image(self.channel_list[channel_id].startx,0,image=self.photo_list[tag_],tag=chr(tag_+65))
            self.item_dict[item_id]=CanvasItem(self.channel_list[channel_id].startx,0,self.channel_list[channel_id])
            self.move_down(item_id)
            # print self.canvas.find_all()
        self.canvas.after(int(5000/pow(1.1,self.level-1)),self.start_fall)
            
    def new_game(self):
        self.canvas.destroy()
        if self.scoreboard:
            self.scoreboard.destroy()
        self.canvas = Canvas(self.root,width=600,height=600,bg='white')
        self.canvas.pack()
        self.score = 0
        self.level = 1
        self.state = 'ing'
        self.scoreboard = ScoreBoard(self.root)
        self.photo_list = [PhotoImage(file=x+'.gif') for x in['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']]
        self.photo1_list = [PhotoImage(file=x+'1.gif') for x in['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']]
        self.item_dict = {}
        self.channel_list = [Channel(x, 25+50*x) for x in range(12)]
        self.start_fall()

    def pause_game(self):
        self.state='pause'
        # if askyesno(u'游戏暂停',u'游戏暂停，是否恢复游戏？'):
        #    self.state='ing'
        #    self.start_fall()
        #    [self.move_down(id) for id in self.item_dict.keys() if self.item_dict[id].state=='down']
            

if __name__ == '__main__':
    TypingGame()
    mainloop()

