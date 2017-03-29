# coding:utf-8
from Tkinter import *
import tkMessageBox,sys
from random import randint
import time
import random

gx, gy = 15, 15  # 棋盘大小
EMPTY, SNAKE, FRUIT = 1, 2, 3  # 网格状态
g = [[EMPTY for x in range(gx)] for y in range(gy)]  # 棋盘
snake = []
# 列表中每一个 (y,x) 二元组表示蛇的身体在坐标 (y,x) 中
# snake[0]是蛇尾，snake[-1]是蛇头


UP, DOWN, LEFT, RIGHT = 1, 2, 3, 4
position = DOWN


class Die(Exception):  # 死了的时候抛出这个异常
    pass


def spawnfruit(): # 生成一个食物
    available = [(y, x) for y in range(gy) for x in range(gx) if g[y][x] == EMPTY]  # 所有空的网格
    if available:
        y, x = random.choice(available) # 任选一个放置食物
        g[y][x] = FRUIT
    else:  # 这种情况应该不会发生……
        raise Die


def delchunk():  # 删除蛇尾
    y, x = snake[0]
    g[y][x] = EMPTY
    del snake[0]


def moveto(y, x):  # 把蛇移动到 (y,x) 位置
    fruit_flag = False  # 碰到食物的flag

    if not ((0 <= y < gy) and (0 <= x < gx)):  # 碰到边界就会死
        raise Die()
    if g[y][x] == SNAKE:  # 碰到自己就会死
        raise Die()
    if g[y][x] == FRUIT:
        fruit_flag = True

    snake.append((y, x))
    g[y][x] = SNAKE

    if fruit_flag:
        spawnfruit()  # 吃到食物时生成新的
    else:
        delchunk()  # 吃到食物时蛇尾不往前缩


def push():  # 蛇头往当前方向增长一格
    now_y, now_x = snake[-1]  # 蛇头原本的位置
    if position == UP:
        moveto(now_y-1, now_x)
    elif position == DOWN:
        moveto(now_y+1, now_x)
    elif position == LEFT:
        moveto(now_y, now_x-1)
    else:  # position==RIGHT
        moveto(now_y, now_x+1)


def init():  # 初始化
    # 清空棋盘
    while snake:
        delchunk()
    for y in range(gy):
        for x in range(gx):
            g[y][x] = EMPTY

    # 生成一条蛇和一个食物
    for y, x in [(1,0),(2,0),(3,0)]:
        snake.append((y,x))
        g[y][x] = SNAKE
    spawnfruit()


def game_controller():  # 整个游戏的流程
    init()
    while True:
        try:
            push()
            time.sleep(.5)
        except Die:
            init()

EMPTY = '#0000FF'
SNAKE = '#FFFF00'
FRUIT = '#00FF00'

tk = Tk()
labels = [[None for x in range() for y in range()]]

for y in range(gy):
    for x in range(gx):
        labels[y][x] = Label(tk, text='  ', font='-size 10',background=EMPTY)
        labels[y][x].grid(row=y, column=x)

