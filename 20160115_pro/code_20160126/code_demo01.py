# coding:utf-8
import random as r
# 双色球

red_ball = range(1, 33)
blue_ball = range(1, 17)
# end_list = []
# while len(end_list) < 7:
#     if len(end_list) < 6:
#         red = r.choice(red_ball)
#         end_list.append(red)
#         end_list.sort()
#         red_ball.remove(red)
#     else:
#         end_list.append(r.choice(blue_ball))
# print end_list


# 实现获取篮球业务
def find_blue_ball(bball):
    return r.sample(bball,1)


# 先实现获取红球业务
def find_red_ball(rball, bball):
     str_list = r.sample(rball, 6)
     str_list += find_blue_ball(bball)
     return str_list

# 课后作业
# 双舍球业务实现出来,把这个双色球写到txt文本里面,
# 存入格式,格式 :
# 29, 17, 18, 11, 8, 23, 8 ---->2016-1-26 21:29:18
# w 而且要用 a或者a+
# time
import time
print time.strftime()


print find_red_ball(red_ball, blue_ball)