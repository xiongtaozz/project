#coding:utf-8
from Tkinter import *
import time
import random
import string

root = Tk()
root.title("Typing")
cvs = Canvas (root , width=900 , height=600 , background="White" )
def Start():
    s=random.sample("string.ascii_letters",5)
    cvs.delete('rand')
    return cvs.create_text(25,30,text=s,tags='rand')
br1=Button(root,text="Start",command=Start,width=30).pack()

# def printCoords(event):
#     print event.x,event.y
# # 创建第一个Button,并将它与左键事件绑定
# bt1 = Button(root,text = 'leftmost button')
# # bt1.bind(,printCoords)
def delete(s):
    string.replace('',s,'',1)
while Start():
    def move_s(s):
        s.move(50,30)
        x=0
        Score=0
        for i in s:
            if i == '<Key>':
                Score+=10
                i.pop()
            else:
                while x<10:
                    i.move(-3,0)
                    x+=1
                    time.sleep(5)
                    i.delete()
                    break
    cvs.bind('<Key>',move_s)
cvs.pack()
root.mainloop()