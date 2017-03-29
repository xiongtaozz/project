# -*- coding: utf-8 -*-
'''Tkinter教程之Event篇(1)'''
# 事件的使用方法
'''1.测试鼠标点击(Click)事件'''
# <Button-1>：鼠标左击事件
# <Button-2>：鼠标中击事件
# <Button-3>：鼠标右击事件
# <Double-Button-1>：双击事件
# <Triple-Button-1>：三击事件
from Tkinter import *
root = Tk()
def printCoords(event):
    print event.x,event.y
# 创建第一个Button,并将它与左键事件绑定
bt1 = Button(root,text = 'leftmost button')
bt1.bind('<Button-1>',printCoords)

# 创建二个Button，并将它与中键事件绑定
bt2 = Button(root,text = 'middle button')
bt2.bind('<Button-2>',printCoords)

# 创建第三个Button，并将它与右击事件绑定
bt3 = Button(root,text = 'rightmost button')
bt3.bind('<Button-3>',printCoords)

# 创建第四个Button,并将它与双击事件绑定
bt4 = Button(root,text = 'double click')
bt4.bind('<Double-Button-1>',printCoords)

# 创建第五个Button，并将它与三击事件绑定
bt5 = Button(root, text = 'triple click')
bt5.bind('<Triple-Button-1>',printCoords)

bt1.grid()
bt2.grid()
bt3.grid()
bt4.grid()
bt5.grid()

root.mainloop()
# 分别测试鼠标的事件，回调函数的参数event中(x,y)表示当前点击的坐标值
'''2.测试鼠标的移动(Motion)事件'''
# -*- coding: cp936 -*-
# <Bx-Motion>：鼠标移动事件,x=[1,2,3]分别表示左、中、右鼠标操作。
from Tkinter import *
root = Tk()
def printCoords(event):
    print event.x,event.y
# 创建第一个Button,并将它与左键移动事件绑定
bt1 = Button(root,text = 'leftmost button')
bt1.bind('<B1-Motion>',printCoords)

# 创建二个Button，并将它与中键移动事件绑定
bt2 = Button(root,text = 'middle button')
bt2.bind('<B2-Motion>',printCoords)

# 创建第三个Button，并将它与右击移动事件绑定
bt3 = Button(root,text = 'rightmost button')
bt3.bind('<B3-Motion>',printCoords)


bt1.grid()
bt2.grid()
bt3.grid()

root.mainloop()
# 分别测试鼠标的移动事件，只有当鼠标被按下后移动才回产生事件
'''3.测试鼠标的释放(Relase)事件'''
# -*- coding: cp936 -*-
# <ButtonRelease-x>鼠标释放事件,x=[1,2,3],分别表示鼠标的左、中、右键操作
from Tkinter import *
root = Tk()
def printCoords(event):
    print event.x,event.y
# 创建第一个Button,并将它与左键释放事件绑定
bt1 = Button(root,text = 'leftmost button')
bt1.bind('<ButtonRelease-1>',printCoords)

# 创建二个Button，并将它与中键释放事件绑定
bt2 = Button(root,text = 'middle button')
bt2.bind('<ButtonRelease-2>',printCoords)

# 创建第三个Button，并将它与右击释放事件绑定
bt3 = Button(root,text = 'rightmost button')
bt3.bind('<ButtonRelease-3>',printCoords)


bt1.grid()
bt2.grid()
bt3.grid()

root.mainloop()
# 分别测试鼠标的Relase事件，只有当鼠标被Relase后移动才回产生Relase事件
'''4.进入(Enter)事件'''
# -*- coding: cp936 -*-
# <Enter>：鼠标释放事件
from Tkinter import *
root = Tk()
def printCoords(event):
    print event.x,event.y
# 创建第一个Button,并将它与Enter事件绑定
bt1 = Button(root,text = 'leftmost button')
bt1.bind('<Enter>',printCoords)

bt1.grid()

root.mainloop()
# 分别测试Enter事件，只是在第一次进入进回产生事件，在组件中移动不会产生Enter事件。