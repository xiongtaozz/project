#!/usr/bin/python
#-*- coding:utf-8 -*-
import os
filePath = os.path.join(os.path.dirname(__file__),'text.txt')
file = open(filePath)
for f in file:
    '''doc'''
    print f.upper()
