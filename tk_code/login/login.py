# -*- coding:utf-8 -*-

from Tkinter import *


top = Tk()
top.title('hello Tkinter')
lable = Label(top, bitmap='error')
text = Entry(top)
text.pack()
lable.pack()
mainloop()

