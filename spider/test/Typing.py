#coding:utf-8
from Tkinter import *
from time import *
import string
import random

root = Tk ( )
root.title("Typing")

cvs = Canvas(root, width=400 , height=350 , background="White")

# s=random.sample("string.ascii_letters",5)
x,y=200,50
s=''
def strfunc():
    global s
    s=random.sample("string.ascii_letters",5)
    return s
def Start():
    s=strfunc()
    cvs.delete("rand")
    return cvs.create_text(200,50,text=s,tags='rand',font=('Courier New',36,'normal'))
def Down():
    for i in s:
        if i == text.get():
            s.remove(i)
            cvs.delete("rand")
            return cvs.create_text((x-100,y-20),text=s,tags='rand',font=('Courier New',36,'normal'))
        else:
            pass
Button(root,text="Start",command=Start,width=30).pack()
Button(root,text="Down",command=Down,width=30).pack()
text = Entry(root,foreground = 'red',)
text.pack()
def get_clickpoint(event):
    print event.x, event.y
cvs.bind('<s>',get_clickpoint)
cvs.bind('<s>',get_clickpoint)
cvs.pack()
root.mainloop()


