# -*- coding:utf-8 -*-

from types import MethodType

s = None


def set_age(self, age):
     self.age = age

s.set_age = MethodType(set_age,s)
s.set_age(25)
print s.age