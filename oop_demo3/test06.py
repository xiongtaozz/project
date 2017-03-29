#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys,os


# list_s=raw_input()
#
# # 中文
# def tj_zm():
#  t=0
#  for i in range (0,len(list_s)):
#  # print list_s[i]
#   if list_s[i].isalpha():
#    t=t+1
#  return t;
#
#
# def tj_sz():
#  a=0
#  for i in range (0,len(list_s)):
#   if list_s[i].isdigit():
#    a=a+1
#  return a
#
# def tj_kg():
#  b=0
#  for i in range (0,len(list_s)):
#   if list_s[i].isspace():
#    b=b+1
#
#  return b
#
# print tj_sz(),tj_kg(),tj_zm


def mult():
    return [lambda x: i * x for i in xrange(4)]  # 0 1 2 3

# print mult()
# 0 2 4 6
print [m(2) for m in mult()]


def mus():
    return lambda x: x * 2

print mus()(2)