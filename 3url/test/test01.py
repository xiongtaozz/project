# coding:utf-8
# import urllib.request


# from urllib import request
#
# res = request.urlopen('https://www.baidu.com').read()
#
# print(res)

# import os
#
# print(os.path.join('a', 'b'))

# import matplotlib.pyplot as plt
#
# # Create your tests here.
#
# plt.plot([1, 2, 3, 4], [-4, -3, -2, -1])
# plt.show()

# Flag = False
# while Flag == False:
#     f = open("record.log","a+")
#     print u"文件内容为：\n%s" % f.read()
#     str = raw_input(u"请输入：")
#     print str
#     if str != 'exit' or str != 'quit':
#         f.write(str)

# from tkinter import *
# import tkinter.simpledialog as dl
# import tkinter.messagebox as mb
import random

# root = Tk()
# w = Label(root,text="Guess Number Game")
# w.pack()
#
# mb.showinfo("Welcome","Welcome to Guess Number Game")
# number = random.uniform(100,150)
#
# while True:
#     guess = dl.askinteger("Number","What`s your guess?")
#     if guess == number:
#        output="Bing!,You get the right number!"
#        mb.showinfo("Hint:",output)
#        break
#     elif 100<guess<number:
#        output="What a pity!Your number is almostly right!"
#        mb.showinfo("Hint:",output)
#     elif number<guess<150:
#        output="What a pity!Your number is almostly right!"
#        mb.showinfo("Hint:",output)
#     else:
#        output="Sorry!Please try again!"
#        mb.showinfo("Hint:",output)
#
# print ("Done")

# import time
#
# print time.mktime('2016-5-6 14:24:42') - time.mktime(time.strftime('%Y-%m-%d %X',time.localtime(time.time())))