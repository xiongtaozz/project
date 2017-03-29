# coding:utf-8
import datetime

t1 = datetime.datetime.strptime('2016-03-15 10:09:01', '%Y-%m-%d %H:%M:%S')
t2 = datetime.datetime.now()
print (t2-t1).days