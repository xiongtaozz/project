# -*- coding: utf-8 -*-

from Tkinter import *
import os
from PIL import ImageTk, Image

BASE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static\\img')


class Index(object):

    def __init__(self):
        self.root = Tk()
        self.root.title('飞机大战')
        self.canvas = Canvas(self.root, width=300, height=400, bg='white')

    def run(self):
        image = Image.open('D:\\parcms\\workbase\\new_pro\\static\\img\\background_1.png')
        im = ImageTk.PhotoImage(image)
        self.canvas.create_image(145, 200, image=im)
        self.canvas.create_text(145, 200, text='开始游戏', fill='blue')
        # self.canvas.create_text()
        self.canvas.pack()
        self.root.mainloop()

if __name__ == '__main__':
    Index().run()