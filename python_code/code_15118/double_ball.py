# coding:utf-8
import random

red_boll=range(1,33)
blue_boll=range(1,17)
print red_boll
print blue_boll
print random.choice(red_boll)
list =[]
while len(list)<7:
    if len(list)<6:
        red = random.choice(red_boll)
        list.append(red)
        red_boll.remove(red)
    else:
        list.append(random.choice(blue_boll))
print list
