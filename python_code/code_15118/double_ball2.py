# coding: utf-8
import random

red_bool = range(1,33)

blue_bool = range(1,17)


def shake_bool(red_bool, blue_bool):

     read_bool = []

     while True:
          if len(read_bool) < 6:
               re=random.choice(red_bool)
               read_bool.append(re)
               red_bool.remove(re)
          else:
               break
          
     blue_shake_bool(read_bool, blue_bool)      

     #print '----',read_bool

     return read_bool

def  blue_shake_bool(read_bool,blue_bool):
     if len(read_bool) == 6:
          r=random.choice(blue_bool)
          read_bool.append(r)
          print 'blue:',r
          #blue_bool.remove(re)
     #print '本期开出的结果是：',read_bool
     return read_bool

 
read_bool=shake_bool(red_bool,blue_bool)
print '本期开出的结果是：',read_bool