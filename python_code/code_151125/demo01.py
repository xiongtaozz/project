#coding:utf-8

class student():
    def get_age(self):
        return self.__age

    def set_age(self,val):
        if not isinstance(val,int):
            raise ValueError('age must be an integer')
        if val <0 or val >100:
            raise ValueError('age must butween 1~100')
        self.__age=val
s =student()
s.set_age(20)
print s.get_age()
print '--------------------------------'
class student1():
    @property
    def sorce(self):
        return self.__age
    @sorce.setter
    def sorce(self,val):
        if not isinstance(val,int):
            raise ValueError('age must be an integer')
        if val <0 or val >100:
            raise ValueError('age ust butween 1~100')
        self.__age=val

s1=student1()
s1.sorce=90
print s1.sorce
s1.sorce=30
s2=student1()
print s2.sorce